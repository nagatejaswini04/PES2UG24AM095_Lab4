"""Command-line Hangman game with session statistics and difficulty modes."""

from dataclasses import dataclass, field
import random

WORDS = {
    "animals": [("elephant", "A large land mammal"), ("giraffe", "An animal with a very long neck"),
                ("penguin", "A flightless bird")],
    "technology": [("python", "A popular programming language"), ("keyboard", "An input device"),
                   ("database", "An organized collection of data")],
    "science": [("gravity", "The force that attracts objects"), ("atom", "A basic unit of matter"),
                ("planet", "An object orbiting a star")],
}

DIFFICULTIES = {
    "easy": {"lives": 10, "multiplier": 1},
    "medium": {"lives": 7, "multiplier": 2},
    "hard": {"lives": 5, "multiplier": 3},
}


@dataclass
class SessionStats:
    rounds_played: int = 0
    wins: int = 0
    current_streak: int = 0
    best_streak: int = 0
    total_score: int = 0

    def record_round(self, won: bool, score: int) -> None:
        self.rounds_played += 1
        self.total_score += score
        if won:
            self.wins += 1
            self.current_streak += 1
            self.best_streak = max(self.best_streak, self.current_streak)
        else:
            self.current_streak = 0


@dataclass
class HangmanGame:
    word: str
    hint: str
    difficulty: str = "medium"
    guessed_letters: set[str] = field(default_factory=set)
    lives: int = field(init=False)
    score: int = 0
    hint_used: bool = False
    finished: bool = False
    won: bool = False
    message: str = ""

    def __post_init__(self) -> None:
        self.word = self.word.lower()
        if self.difficulty not in DIFFICULTIES:
            raise ValueError("Difficulty must be easy, medium, or hard.")
        self.lives = DIFFICULTIES[self.difficulty]["lives"]

    @property
    def masked_word(self) -> str:
        return " ".join(ch if ch in self.guessed_letters else "_" for ch in self.word)

    def guess(self, raw_guess: str) -> str:
        """Process one letter guess and return a user-facing status."""
        guess = raw_guess.strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            self.message = "Enter exactly one alphabetic letter."
            return self.message
        if self.finished:
            self.message = "This round has finished."
            return self.message
        if guess in self.guessed_letters:
            self.message = f"You already guessed '{guess}'. No life was lost."
            return self.message

        self.guessed_letters.add(guess)
        if guess in self.word:
            self.message = f"Good guess: '{guess}' is in the word."
            if all(ch in self.guessed_letters for ch in self.word):
                self.finished = True
                self.won = True
                multiplier = DIFFICULTIES[self.difficulty]["multiplier"]
                self.score = max(0, self.lives * 10 * multiplier)
                self.message = f"You won! The word was {self.word}."
        else:
            self.lives -= 1
            self.message = f"'{guess}' is not in the word."
            if self.lives <= 0:
                self.finished = True
                self.won = False
                self.message = f"Out of lives. The word was {self.word}."
        return self.message

    def use_hint(self) -> str:
        if self.finished:
            return "This round has finished."
        if self.hint_used:
            return "The hint has already been used."
        hidden = [ch for ch in self.word if ch not in self.guessed_letters]
        if not hidden:
            return "No hint is needed."
        revealed = random.choice(hidden)
        self.guessed_letters.add(revealed)
        self.hint_used = True
        self.message = f"Hint: {self.hint} (revealed '{revealed}')."
        return self.message

    def apply_hint_penalty(self) -> None:
        if self.hint_used:
            self.score = max(0, self.score - 10)


def choose_word(category: str) -> tuple[str, str]:
    if category not in WORDS:
        raise ValueError("Unknown category.")
    return random.choice(WORDS[category])


def choose_difficulty(value: str) -> str:
    normalized = value.strip().lower()
    if normalized not in DIFFICULTIES:
        raise ValueError("Choose easy, medium, or hard.")
    return normalized


def play_round(input_fn=input, output_fn=print, word_pair=None, difficulty=None):
    """Run one round. Optional injected word/difficulty make it testable."""
    output_fn("Categories: " + ", ".join(WORDS))
    category = input_fn("Choose a category: ").strip().lower()
    while category not in WORDS:
        output_fn("Invalid category. Try again.")
        category = input_fn("Choose a category: ").strip().lower()

    output_fn("Difficulty: easy / medium / hard")
    difficulty = difficulty or input_fn("Choose difficulty: ")
    while True:
        try:
            difficulty = choose_difficulty(difficulty)
            break
        except ValueError as exc:
            output_fn(str(exc))
            difficulty = input_fn("Choose difficulty: ")

    word, hint = word_pair if word_pair else choose_word(category)
    game = HangmanGame(word, hint, difficulty)
    while not game.finished:
        output_fn(f"\nWord: {game.masked_word} | Lives: {game.lives} | Guessed: {', '.join(sorted(game.guessed_letters)) or '-'}")
        command = input_fn("Guess a letter, type 'hint', or 'quit': ").strip().lower()
        if command == "quit":
            game.finished = True
            game.won = False
            game.message = f"Round ended. The word was {game.word}."
        elif command == "hint":
            output_fn(game.use_hint())
        else:
            output_fn(game.guess(command))

    if game.won:
        multiplier = DIFFICULTIES[game.difficulty]["multiplier"]
        game.score = max(0, game.lives * 10 * multiplier - (10 if game.hint_used else 0))
    output_fn(game.message)
    output_fn(f"Round score: {game.score}")
    return game


def main() -> None:
    stats = SessionStats()
    print("=== HANGMAN ===")
    while True:
        game = play_round()
        stats.record_round(game.won, game.score)
        print("\n=== SESSION STATISTICS ===")
        print(f"Rounds played: {stats.rounds_played}")
        print(f"Wins: {stats.wins}")
        print(f"Best win streak: {stats.best_streak}")
        print(f"Total score: {stats.total_score}")
        again = input("\nPlay another round? (y/n): ").strip().lower()
        while again not in {"y", "n"}:
            print("Please enter y or n.")
            again = input("Play another round? (y/n): ").strip().lower()
        if again == "n":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

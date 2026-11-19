"""Illustrative pre-fix baseline: repeated wrong guesses incorrectly cost lives."""

class OriginalHangman:
    def __init__(self, word):
        self.word = word.lower()
        self.lives = 6
        self.guessed_letters = set()

    def guess(self, letter):
        letter = letter.lower()
        # Deliberate defect for demonstration: no repeated-guess check.
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.lives -= 1
        return self.lives


if __name__ == "__main__":
    game = OriginalHangman("python")
    print("Guess z:", game.guess("z"))
    print("Guess z again (bug: another life is lost):", game.guess("z"))

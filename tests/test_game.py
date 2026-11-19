import unittest

from hangman.game import HangmanGame, SessionStats, choose_difficulty


class TestHangmanGame(unittest.TestCase):
    def test_correct_guess_reveals_letter(self):
        game = HangmanGame("cat", "A pet", "easy")
        game.guess("c")
        self.assertEqual(game.masked_word, "c _ _")
        self.assertEqual(game.lives, 10)

    def test_wrong_guess_reduces_life(self):
        game = HangmanGame("cat", "A pet", "medium")
        game.guess("z")
        self.assertEqual(game.lives, 6)

    def test_repeated_wrong_guess_does_not_reduce_life_twice(self):
        game = HangmanGame("cat", "A pet", "medium")
        game.guess("z")
        game.guess("z")
        self.assertEqual(game.lives, 6)
        self.assertIn("No life was lost", game.message)

    def test_invalid_guess_does_not_change_lives(self):
        game = HangmanGame("cat", "A pet", "hard")
        game.guess("ab")
        self.assertEqual(game.lives, 5)

    def test_win_when_all_letters_guessed(self):
        game = HangmanGame("cat", "A pet", "easy")
        for letter in "cat":
            game.guess(letter)
        self.assertTrue(game.finished)
        self.assertTrue(game.won)

    def test_difficulty_validation(self):
        self.assertEqual(choose_difficulty(" HARD "), "hard")
        with self.assertRaises(ValueError):
            choose_difficulty("expert")

    def test_hint_reveals_letter_only_once(self):
        game = HangmanGame("cat", "A pet", "easy")
        first = game.use_hint()
        self.assertIn("Hint:", first)
        second = game.use_hint()
        self.assertIn("already been used", second)

    def test_session_statistics_and_streak(self):
        stats = SessionStats()
        stats.record_round(True, 20)
        stats.record_round(True, 30)
        stats.record_round(False, 0)
        stats.record_round(True, 10)
        self.assertEqual(stats.rounds_played, 4)
        self.assertEqual(stats.wins, 3)
        self.assertEqual(stats.best_streak, 2)
        self.assertEqual(stats.current_streak, 1)
        self.assertEqual(stats.total_score, 60)


if __name__ == "__main__":
    unittest.main()

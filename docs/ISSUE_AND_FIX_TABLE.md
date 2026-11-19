# Issue and Fix Table

| No. | Issue / requirement | Implementation | Verification |
|---|---|---|---|
| 1 | Repeated incorrect guesses can consume multiple lives | Check `guessed_letters` before processing a guess; duplicate input returns without changing lives | `test_repeated_wrong_guess_does_not_reduce_life_twice` |
| 2 | No session-level progress tracking | `SessionStats` tracks rounds, wins, current streak, best streak and total score | `test_session_statistics_and_streak` |
| 3 | One fixed difficulty level | Easy, medium and hard set different starting lives and score multipliers | `test_difficulty_validation` and game initialization |
| 4 | Input is not validated consistently | Require one alphabetic character; validate category and difficulty; validate replay choice | `test_invalid_guess_does_not_change_lives` |
| 5 | No hint mechanism / hint penalty | One-time hint reveals a hidden letter; score is reduced by 10 points | `test_hint_reveals_letter_only_once` and round scoring logic |

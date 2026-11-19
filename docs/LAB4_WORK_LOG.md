# Lab 4 – Vibe Coding Work Log

**Student:** SatyaTeju  
**SRN:** PES2UG24AM095  
**Section:** 5B

## Objective
Develop and improve a Python Hangman game through iterative, prompt-guided changes.

## Work completed
- Created a runnable Python Hangman implementation.
- Added duplicate-guess protection so a repeated letter does not cost another life.
- Added session statistics for rounds played, wins, and best consecutive-win streak.
- Added easy, medium, and hard modes with different lives and score multipliers.
- Added a one-time hint and a score penalty.
- Added input validation for guesses, categories, difficulty, and replay choice.
- Added automated unit tests for core behavior.

## Prompt / task log
1. Build a small Python Hangman game with a clean separation between game logic and command-line interaction.
2. Fix repeated-guess handling so an already-guessed letter never consumes another life.
3. Add session statistics for rounds played, wins, current streak, best streak, and total score.
4. Add difficulty levels that affect starting lives and scoring.
5. Add a one-time hint feature with a score penalty.
6. Validate user input and add unit tests for the key behaviors.

## Verification
Run:
```bash
python -m unittest discover -s tests -v
```

The tests cover correct guesses, incorrect guesses, duplicate guesses, invalid input, win detection, difficulty validation, one-time hints, and session statistics.

## Important evidence note
This work log summarizes the implementation tasks and prompts. It is not a verbatim export of the entire ChatGPT conversation. Any required official chat-history export should be downloaded separately from the ChatGPT conversation.

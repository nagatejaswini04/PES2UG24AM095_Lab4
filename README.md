# Software Engineering Lab 4 – Vibe Coding
## Hangman Challenge

**Student:** SatyaTeju  
**SRN:** PES2UG24AM095  
**Section:** 5B  
**Project:** Hangman – independent implementation

## Project overview
A command-line Hangman game in Python. The project demonstrates iterative code improvement and feature development. It includes repeat-guess protection, session statistics, difficulty levels, scoring, hints, and robust input validation.

## Requirements
- Python 3.10 or later
- No third-party packages required

## Run
```bash
python main.py
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Features implemented
1. Repeated guesses are detected and do not reduce remaining lives.
2. Session statistics track rounds played, wins, and the best consecutive-win streak.
3. Difficulty settings change starting lives and score multiplier.
4. Hints reveal one unrevealed letter and apply a score penalty.
5. Input validation handles invalid letters, repeated letters, unsupported commands, and invalid difficulty choices.
6. The game supports multiple rounds in one session.

## Project structure
```text
PES2UG24AM095_Lab4/
├── main.py
├── hangman/
│   ├── __init__.py
│   └── game.py
├── tests/
│   └── test_game.py
├── docs/
│   ├── LAB4_WORK_LOG.md
│   └── ISSUE_AND_FIX_TABLE.md
├── original_buggy_version.py
└── README.md
```

## Notes
`original_buggy_version.py` is a small illustrative baseline that intentionally contains the repeated-guess defect for comparison. `main.py` is the corrected playable implementation. This is a fresh implementation based on the feature list available from the reference submission; it is not a clone of the original assigned repository.

## Suggested Git commit sequence
1. `Fix repeated guess handling`
2. `Add session statistics`
3. `Add difficulty and scoring`
4. `Improve input validation and hints`

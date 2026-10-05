# Cricket Statistics Analyzer

A Python-based Cricket Statistics Analyzer using SQLite, Pandas and Matplotlib.

## Features

- SQL database for cricket statistics
- Pandas DataFrames
- Menu-driven interface
- Batting statistics comparison
- Bowling statistics comparison
- Matplotlib data visualization

## Technologies

- Python
- SQLite
- Pandas
- Matplotlib

## Project Structure

```text
cricket-stats-analyzer/
├── data/
│   └── cricket_stats.sql
├── cricket_stats.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python cricket_stats.py
```

The program automatically creates the SQLite database from `data/cricket_stats.sql`.

## Statistics

### Batting
- Runs
- Batting Average
- Strike Rate
- Highest Score
- Fours
- Sixes
- Fifties
- Hundreds

### Bowling
- Runs Conceded
- Wickets
- Economy Rate
- Bowling Average
- Bowling Strike Rate
- Four-Wicket Hauls

## Author

Anish Bandaru

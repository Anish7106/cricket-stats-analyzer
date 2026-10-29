# Cricket Statistics Analyzer

Explore and compare IPL batting and bowling statistics with a menu-driven Python app backed by SQLite, Pandas, and Matplotlib.

## At a glance

| Batting analysis | Bowling analysis |
| --- | --- |
| Runs, average, strike rate, and highest score | Runs conceded, wickets, economy, and bowling average |
| Fours, sixes, fifties, and hundreds | Bowling strike rate and four-wicket hauls |
| Matplotlib player comparison charts | Matplotlib player comparison charts |

## Sample data preview

The included SQL seed file contains IPL 2023 batting and bowling records. Here are two example entries:

| Player | Category | Runs | Average | Strike rate |
| --- | --- | ---: | ---: | ---: |
| Shubman Gill | Batting | 890 | 59.33 | 157.80 |

| Player | Category | Wickets | Economy | Bowling average |
| --- | --- | ---: | ---: | ---: |
| Mohammed Shami | Bowling | 28 | 8.03 | 18.64 |

## Run locally

Requires Python 3.

```bash
git clone https://github.com/Anish7106/cricket-stats-analyzer.git
cd cricket-stats-analyzer
pip install -r requirements.txt
python cricket_stats.py
```

Choose batting or bowling statistics from the menu, then select a metric to display a player comparison chart.

## Project layout

```text
cricket-stats-analyzer/
├── data/
│   └── cricket_stats.sql
├── cricket_stats.py
└── requirements.txt
```

**Stack:** Python · SQLite · Pandas · Matplotlib  
**Author:** Anish Bandaru

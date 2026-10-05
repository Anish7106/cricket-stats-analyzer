import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DATABASE = "cricket_stats.db"
SQL_FILE = "data/cricket_stats.sql"


def create_database():
    connection = sqlite3.connect(DATABASE)

    with open(SQL_FILE, "r") as file:
        sql = file.read()

    connection.executescript(sql)
    connection.commit()

    return connection


def load_data(connection):
    batting_df = pd.read_sql_query("SELECT * FROM batting", connection)
    bowling_df = pd.read_sql_query("SELECT * FROM bowling", connection)

    return batting_df, bowling_df


def plot_graph(df, column, title, ylabel):
    plt.figure(figsize=(12, 7))

    bars = plt.bar(df["Player"], df[column], edgecolor="black", linewidth=1.2)

    plt.title(title, fontsize=18, fontweight="bold", pad=15)
    plt.xlabel("Player", fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    plt.xticks(rotation=35, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    for bar in bars:
        value = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:g}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )

    plt.tight_layout()
    plt.show()


def batting_menu(df):
    while True:
        print()
        print("=" * 55)
        print("                 BATTING STATISTICS")
        print("=" * 55)
        print("  1. Runs")
        print("  2. Batting Average")
        print("  3. Strike Rate")
        print("  4. Highest Score")
        print("  5. Fours")
        print("  6. Sixes")
        print("  7. Fifties")
        print("  8. Hundreds")
        print("  9. Back to Main Menu")
        print("=" * 55)

        choice = input("  Enter your choice: ")

        if choice == "1":
            plot_graph(df, "Runs", "Runs Scored by Batsmen", "Runs")
        elif choice == "2":
            plot_graph(df, "Avg", "Batting Average", "Average")
        elif choice == "3":
            plot_graph(df, "SR", "Batting Strike Rate", "Strike Rate")
        elif choice == "4":
            plot_graph(df, "HS", "Highest Score", "Runs")
        elif choice == "5":
            plot_graph(df, "Fours", "Fours Hit", "Number of Fours")
        elif choice == "6":
            plot_graph(df, "Sixes", "Sixes Hit", "Number of Sixes")
        elif choice == "7":
            plot_graph(df, "Fifties", "Fifties Scored", "Number of Fifties")
        elif choice == "8":
            plot_graph(df, "Hundreds", "Hundreds Scored", "Number of Hundreds")
        elif choice == "9":
            break
        else:
            print("\nInvalid choice. Please try again.")


def bowling_menu(df):
    while True:
        print()
        print("=" * 55)
        print("                 BOWLING STATISTICS")
        print("=" * 55)
        print("  1. Runs Conceded")
        print("  2. Wickets")
        print("  3. Economy Rate")
        print("  4. Bowling Average")
        print("  5. Bowling Strike Rate")
        print("  6. Four-Wicket Hauls")
        print("  7. Back to Main Menu")
        print("=" * 55)

        choice = input("  Enter your choice: ")

        if choice == "1":
            plot_graph(df, "Runs", "Runs Conceded by Bowlers", "Runs")
        elif choice == "2":
            plot_graph(df, "Wickets", "Wickets Taken", "Wickets")
        elif choice == "3":
            plot_graph(df, "Econ", "Bowling Economy Rate", "Economy Rate")
        elif choice == "4":
            plot_graph(df, "Avg", "Bowling Average", "Average")
        elif choice == "5":
            plot_graph(df, "SR", "Bowling Strike Rate", "Strike Rate")
        elif choice == "6":
            plot_graph(df, "FourWickets", "Four-Wicket Hauls", "4-Wicket Hauls")
        elif choice == "7":
            break
        else:
            print("\nInvalid choice. Please try again.")


def main():
    connection = create_database()
    batting_df, bowling_df = load_data(connection)

    while True:
        print()
        print("=" * 60)
        print("             CRICKET STATISTICS ANALYZER")
        print("=" * 60)
        print("        Compare IPL Batting & Bowling Stats")
        print("=" * 60)
        print("  1. Batting Statistics")
        print("  2. Bowling Statistics")
        print("  3. Exit")
        print("=" * 60)

        choice = input("  Enter your choice: ")

        if choice == "1":
            batting_menu(batting_df)
        elif choice == "2":
            bowling_menu(bowling_df)
        elif choice == "3":
            print("\n  Thank you for using Cricket Statistics Analyzer!")
            break
        else:
            print("\n  Invalid choice. Please enter 1, 2 or 3.")

    connection.close()


if __name__ == "__main__":
    main()

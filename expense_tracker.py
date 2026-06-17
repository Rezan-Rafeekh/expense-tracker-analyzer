import pandas as pd


def analyze_expenses(file_path):
    df = pd.read_csv(file_path)

    print("\n========== EXPENSE ANALYSIS ==========\n")

    total_spent = df["Amount"].sum()

    print(f"Total Expenses: ₹{total_spent:.2f}")

    print("\nExpenses by Category")
    print("-" * 40)

    category_summary = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print(category_summary)

    print("\nHighest Expense Category")
    print("-" * 40)

    highest = category_summary.idxmax()

    print(
        f"{highest} : ₹{category_summary.max():.2f}"
    )

    avg_expense = df["Amount"].mean()

    print("\nAverage Expense")
    print("-" * 40)

    print(f"₹{avg_expense:.2f}")

    category_summary.to_csv(
        "expense_summary.csv"
    )

    print(
        "\nSummary exported to expense_summary.csv"
    )


if __name__ == "__main__":
    analyze_expenses("expenses.csv")

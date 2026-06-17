# Expense Tracker & Budget Analyzer

A Python-based finance management tool that records expenses, categorizes spending patterns, and generates budget insights.

---

## Features

- Expense tracking
- Category-wise spending analysis
- Monthly expense summaries
- Average spending calculation
- CSV report export
- Budget monitoring

---

## Technologies Used

- Python
- Pandas

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/expense-tracker-analyzer.git
```

Navigate into the project:

```bash
cd expense-tracker-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python expense_tracker.py
```

---

## Sample Dataset

```csv
Date,Category,Amount
2026-01-02,Food,250
2026-01-03,Transport,120
2026-01-04,Entertainment,500
2026-01-05,Food,300
2026-01-06,Shopping,1500
2026-01-07,Transport,100
```

---

## Example Output

```text
========== EXPENSE ANALYSIS ==========

Total Expenses: ₹2770.00

Expenses by Category
----------------------------------------

Shopping         1500
Food              550
Entertainment     500
Transport         220

Highest Expense Category
----------------------------------------

Shopping : ₹1500.00

Average Expense
----------------------------------------

₹461.67

Summary exported to expense_summary.csv
```

---

## Future Enhancements

- Interactive Dashboard using Streamlit
- Data Visualization using Matplotlib
- Budget Alerts
- Monthly Trend Analysis
- PDF Report Generation
- Expense Prediction using Machine Learning

---

## License

MIT License

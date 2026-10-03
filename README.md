# 💰 Personal Finance Intelligence System

An end-to-end **Personal Finance Intelligence System** built to manage financial transactions, analyze spending patterns, track budgets, generate automated financial reports, and visualize financial insights through an interactive Power BI dashboard.

The application combines **Python-based transaction management and data analysis** with **Excel data storage, automated PDF reporting, and Power BI visualization**.

---

## 📌 About the Application

The **Personal Finance Intelligence System** is a menu-driven Python application designed to help users manage and understand their personal financial data.

The application provides a complete workflow for handling financial transactions, from entering and validating data to analyzing expenses, tracking budgets, generating reports, and exploring interactive dashboards.

### The application allows users to:

- ➕ Add new financial transactions
- ✏️ Update existing transactions
- 🗑️ Delete transactions
- 🔎 Search financial records
- ✅ Validate transaction data
- 💰 Analyze income and expenses
- 🎯 Track and analyze budgets
- 📈 Analyze financial trends
- 🧠 Analyze spending behaviour
- 📄 Generate automated PDF reports
- 📊 Explore an interactive Power BI dashboard

The main objective is to transform raw financial transactions into **structured analysis, reports, and meaningful financial insights**.

---

## 🔄 Application Workflow

```text
Transaction Input
       ↓
Data Validation
       ↓
Transaction Management
(Add / Update / Delete / Search)
       ↓
Financial Analysis
       ↓
Budget Analysis
       ↓
Trend Analysis
       ↓
Spending Behaviour Analysis
       ↓
Automated PDF Report
       ↓
Power BI Dashboard
       ↓
Interactive Financial Insights
```

---

## ✨ Main Features

### 📝 Transaction Management

The application provides complete transaction management functionality.

Users can:

- Add new transactions
- Update existing transactions
- Delete transactions
- Search transactions
- Validate transaction data

Financial transaction data is stored in an Excel file and processed using Pandas.

---

### 💰 Expense & Income Analysis

The system analyzes financial transactions and calculates important financial metrics such as:

- Total Income
- Total Expenses
- Total Savings
- Savings Percentage
- Average Expense
- Highest Expense
- Lowest Expense
- Category-wise Spending
- Payment Method Analysis

This helps users understand their overall financial position and spending patterns.

---

### 🎯 Budget Analysis

The budget analysis module compares budgeted amounts with actual expenses.

It provides:

- Category-wise Budget
- Actual Expense
- Remaining Budget
- Budget Status
- Over-budget Categories
- Budget Variance

Example:

```text
Category        Budget        Actual        Remaining        Status
--------------------------------------------------------------------
Food            ₹5000         ₹4200         ₹800             Under budget
Shopping        ₹4000         ₹4700         -₹700            Over budget
```

---

### 📈 Trend Analysis

The system analyzes financial trends over time.

It provides:

- Monthly Income
- Monthly Expenses
- Monthly Savings
- Highest Spending Month
- Lowest Spending Month
- Highest Savings Month
- Monthly Spending Changes

This helps users understand how their financial activity changes over time.

---

### 🧠 Spending Behaviour Analysis

The spending behaviour module analyzes transaction patterns and spending habits.

It includes:

- Average Transaction Amount
- Median Transaction Amount
- Transactions Above Average
- Average Spending by Payment Method
- Most Used Payment Method
- Transaction Count by Category
- Transaction Count by Day of Week
- Transaction Amount by Day of Week
- Cashless Transaction Percentage

---

## 📄 Automated PDF Report

The application can automatically generate a structured financial report in PDF format.

The generated report combines important financial information and analysis into a single document.

The report includes analysis related to:

- Income
- Expenses
- Savings
- Budget
- Trends
- Spending Behaviour
- Financial Insights

PDF report generation is implemented using **FPDF**.

---

# 📊 Power BI Dashboard

The project includes an interactive **3-page Power BI dashboard** that converts financial data into KPIs, charts, and interactive insights.

---

## 📄 Page 1 — Financial Overview

Provides an overall view of the user's financial position.

### KPI Cards

- 💰 Total Income
- 💸 Total Expenses
- 🏦 Total Savings
- 📈 Savings %
- 🧾 Average Expense
- 🔄 Total Transactions

### Visualizations

- Income vs Expense
- Expense by Category
- Income by Category
- Monthly Income vs Expense
- Expense by Payment Method
- Savings by Month

### Filters

- Date
- Category
- Payment Method
- Type

---

## 🎯 Page 2 — Budget Analysis

Focuses on budget performance and spending against planned budgets.

### KPI Cards

- 🎯 Total Budget
- 💸 Actual Expense
- 💰 Remaining Budget
- 📊 Budget Utilization %
- ⚠️ Over Budget Categories
- 📈 Budget Variance

### Visualizations

- Budget vs Actual by Category
- Remaining Budget by Category
- Budget Utilization % by Category
- Over Budget vs Under Budget
- Monthly Budget vs Actual Expense
- Budget Variance by Category

### Filters

- Category
- Month
- Year
- Payment Method

---

## 🧠 Page 3 — Spending Behaviour & Trends

Focuses on transaction behaviour and spending patterns.

### KPI Cards

- Average Transaction Amount
- Median Transaction Amount
- Largest Transaction
- Transactions Above Average
- Cashless Transaction %
- Most Used Payment Method

### Visualizations

- Average Transaction Amount by Category
- Average Transaction Amount by Payment Method
- Transaction Count by Day of Week
- Transaction Amount by Day of Week
- Transaction Count by Category
- Average Expense by Day of Week

### Filters

- Category
- Payment Method
- Month
- Day of Week

---

# 🧮 DAX Analysis

Custom DAX measures were created in Power BI to calculate financial metrics dynamically.

### Total Income

```DAX
Total Income =
CALCULATE(
    SUM(Sheet1[amount]),
    Sheet1[type] = "income"
)
```

### Total Expense

```DAX
Total Expense =
CALCULATE(
    SUM(Sheet1[amount]),
    Sheet1[type] = "expense"
)
```

### Remaining Budget

```DAX
Remaining Budget =
[Total Budget] - [Actual Expense]
```

### Budget Utilization %

```DAX
Budget Utilization % =
DIVIDE(
    [Actual Expense],
    [Total Budget],
    0
) * 100
```

### Transactions Above Average

```DAX
Transactions Above Average =
VAR AvgAmount = [Average Transaction Amount]
RETURN
COUNTROWS(
    FILTER(
        Sheet1,
        Sheet1[amount] > AvgAmount
    )
)
```

These measures allow the dashboard to respond dynamically to slicers and filters.

---

# 📁 Project Structure

```text
Personal-Finance-Intelligence-System/
│
├── 01_data.xlsx
│
├── 02_data_input_and_validation.py
├── 03_delete_data.py
├── 04_update_data.py
├── 05_search_data.py
├── 06_expense_analysis.py
├── 07_budget_analysis.py
├── 08_trend_analysis.py
├── 09_spending_behaviour.py
├── 10_report_generation.py
│
├── 11_report.pdf
│
├── 12_data_visualization.pbix
├── 13_data_visualization.py
│
├── 14_main.py
│
└── README.md
```

---

## 📂 File Description

| File | Description |
|------|-------------|
| `01_data.xlsx` | Stores financial transaction data |
| `02_data_input_and_validation.py` | Handles transaction input and data validation |
| `03_delete_data.py` | Deletes selected transaction records |
| `04_update_data.py` | Updates existing transaction information |
| `05_search_data.py` | Searches financial transaction records |
| `06_expense_analysis.py` | Performs income and expense analysis |
| `07_budget_analysis.py` | Performs budget analysis |
| `08_trend_analysis.py` | Analyzes financial trends over time |
| `09_spending_behaviour.py` | Analyzes spending behaviour and transaction patterns |
| `10_report_generation.py` | Generates the automated PDF report |
| `11_report.pdf` | Generated financial report |
| `12_data_visualization.pbix` | Power BI dashboard |
| `13_data_visualization.py` | Handles the data visualization component |
| `14_main.py` | Main application and module integration |

---

# 🗃️ Data Structure

The Excel dataset contains the following fields:

```text
transaction_id
date
type
category
description
amount
payment_method
budget
```

### Transaction Types

```text
income
expense
```

### Categories

```text
salary
food
transport
shopping
entertainment
bills
education
healthcare
travel
investment
other
```

### Payment Methods

```text
upi
cash
credit card
debit card
bank transfer
net banking
```

---

# ⚙️ Python Module Integration

The project uses Python's `subprocess` functionality to integrate different components of the application.

For example:

```python
import subprocess

subprocess.run(["python", "06_expense_analysis.py"])
```

This allows the main application to execute individual modules when required.

The modular structure keeps transaction management, analysis, reporting, and visualization functionality separated and organized.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Application development and automation |
| Pandas | Data processing and analysis |
| Excel | Financial transaction storage |
| Power BI | Interactive dashboard development |
| DAX | Financial calculations and KPIs |
| FPDF | Automated PDF report generation |
| Subprocess | Module integration and application workflow |

---

# 📊 Skills Demonstrated

This project demonstrates practical experience with:

- Python programming
- Pandas
- Data validation
- CRUD operations
- Data analysis
- Financial analysis
- Excel data handling
- Data visualization
- Power BI
- DAX
- KPI development
- Dashboard design
- Report automation
- Modular programming
- Subprocess integration

---

# 🔗 Project Demo & Dashboard

## 🎥 Project Demonstration

A short video demonstrating the complete workflow of the **Personal Finance Intelligence System**, including transaction management, financial analysis, report generation, and Power BI visualization.

👉 [Watch Project Demonstration](https://lnkd.in/p/dKpeW4vK)

---

## 📊 Power BI Dashboard

Explore the interactive Power BI dashboard containing:

- Financial Overview
- Budget Analysis
- Spending Behaviour & Trends
- Interactive KPI cards
- Charts
- Slicers
- DAX-based calculations

👉 [View Power BI Dashboard](https://lnkd.in/p/d6PvgnhR)

---

# 🎬 Demonstration Workflow

The project demonstration follows this workflow:

```text
Launch Application
       ↓
Add Transaction
       ↓
Validate Data
       ↓
Perform Financial Analysis
       ↓
Analyze Budget
       ↓
Analyze Trends
       ↓
Analyze Spending Behaviour
       ↓
Generate PDF Report
       ↓
Open Power BI Dashboard
       ↓
Explore Interactive Insights
```

---

# 🎯 Project Objective

The main objective of this project is to build a complete personal finance analytics application that can manage financial data and transform it into meaningful information.

The project connects:

```text
Data Management
       ↓
Data Analysis
       ↓
Report Generation
       ↓
Data Visualization
       ↓
Financial Insights
```

Rather than creating only a dashboard, this project integrates **transaction management, analysis, reporting, and visualization** into a single workflow.

---

# 🔮 Future Improvements

Possible future improvements include:

- Predictive expense analysis
- Spending anomaly detection
- Database integration
- Automated email reports
- Financial forecasting
- User authentication
- Cloud-based data storage
- Automated Power BI data refresh
- More advanced financial KPIs

---

# 👨‍💻 Author

## Arnab Das

**B.Tech Computer Science & Engineering**

Interested in:

**Data Analytics | Python | SQL | Pandas | Power BI | DAX | Data Visualization**

---

## ⭐ Project

If you find this project useful or interesting, feel free to explore the repository and provide feedback.

**Thanks for checking out my Personal Finance Intelligence System! 🚀**

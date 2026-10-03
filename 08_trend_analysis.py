import pandas as pd

df = pd.read_excel("01_data.xlsx")
months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"Augest",9:"September",10:"October",11:"November",12:"December"}

def monthly_trend(df):
    print(f"{'Month':<18}{'Income':<15}{'Expense':<15}{'Savings':<18}")
    print("-" * 60)
    df["month"] = pd.to_datetime(df["date"]).dt.month
    for i in range(1,13,1):
        df1 = df[df["month"] == i]
        month = months[i]
        income = df1[df1["type"].str.lower() == "income"]["amount"].sum().round(2)
        expense = df1[df1["type"].str.lower() == "expense"]["amount"].sum().round(2)
        savings = income - expense
        print(f"{month:<18}RS. {income:<14.2f}RS. {expense:<14.2f}RS. {savings:<17.2f}")
    print("-" * 60)

def highest_spending_month(df):
    df1 = df[df["type"].str.lower() == "expense"]
    highest_month = 1
    highest_spending = df1[df1["month"] == 1]["amount"].sum()
    for i in range(2,13,1):
        month = i
        spending = df1[df1["month"] == i]["amount"].sum()
        if spending > highest_spending:
            highest_spending = spending
            highest_month = month
    print(f"Highest Spending Month: {months[highest_month]} with total spending RS. {highest_spending}")

def lowest_spending_month(df):
    df1 = df[df["type"].str.lower() == "expense"]
    lowest_month = 1
    lowest_spending = df1[df1["month"] == 1]["amount"].sum()
    for i in range(2,13,1):
        month = i
        spending = df1[df1["month"] == i]["amount"].sum()
        if spending != 0 and spending < lowest_spending:
            lowest_spending = spending
            lowest_month = month
    print(f"Lowest Spending Month: {months[lowest_month]} with total spending RS. {lowest_spending}")

def highest_savings_month(df):
    df1 = df[df["type"].str.lower() == "expense"]
    df2 = df[df["type"].str.lower() == "income"]
    highest_month = 1
    highest_savings = df2[df2["month"] == 1]["amount"].sum() - df1[df1["month"] == 1]["amount"].sum()
    for i in range(2,13,1):
        month = i
        savings = df2[df2["month"] == i]["amount"].sum() - df1[df1["month"] == i]["amount"].sum()
        if savings > highest_savings:
            highest_savings = savings
            highest_month = month
    print(f"Highest Savings Month: {months[highest_month]} with total spending RS. {highest_savings}")

def average_monthly_expense(df):
    df1 = df[df["type"].str.lower() == "expense"]
    average = 0
    for i in range(1,13,1):
        expense = df1[df1["month"] == 1]["amount"].sum()
        average += expense
    average = (average / 12)
    average = round(average,2)
    print(f"Average Monthly Spending: RS. {average}")

def trend_main():
    print("==================== MONTHLY TREND ====================")
    monthly_trend(df)
    print("\n")
    highest_spending_month(df)
    lowest_spending_month(df)
    highest_savings_month(df)
    average_monthly_expense(df)

trend_main()
from fpdf import FPDF
from contextlib import redirect_stdout
import io
import pandas as pd

df = pd.read_excel("01_data.xlsx")

def total_income(df):
    df1 = df[df['type'].str.lower() == "income"]
    result = df1["amount"].sum()
    return result
    
def total_expense(df):
    df1 = df[df['type'].str.lower() == "expense"]
    result = df1['amount'].sum()
    return result

def total_savings(df):
    result = total_income(df) - total_expense(df)
    return result

def percentage_savings(df):
    result = (total_savings(df)/total_income(df)) * 100
    return round(result,2)

def average_expense(df):
    df1 = df[df["type"].str.lower() == "expense"]
    result = df1["amount"].mean()
    return round(result,2)

def highest_expense(df):
    df1 = df[df["type"].str.lower() == "expense"]
    result = df1["amount"].max()
    return round(result,2)
    
def lowest_expense(df):
  df1 = df[df["type"].str.lower() == "expense"]
  result = df1["amount"].min()
  return round(result,2)

def food_expense(df):
    df1 = df[df["category"].str.lower() == "food"]
    result = df1["amount"].sum()
    return result

def shopping_expense(df):
    df1 = df[df["category"].str.lower() == "shopping"]
    result = df1["amount"].sum()
    return result

def transport_expense(df):
    df1 = df[df["category"].str.lower() == "transport"]
    result = df1["amount"].sum()
    return result

def bills_expense(df):
    df1 = df[df["category"].str.lower() == "bills"]
    result = df1["amount"].sum()
    return result

def entertainment_expense(df):
    df1 = df[df["category"].str.lower() == "entertainment"]
    result = df1["amount"].sum()
    return result

def education_expense(df):
    df1 = df[df["category"].str.lower() == "education"]
    result = df1["amount"].sum()
    return result

def travel_expense(df):
    df1 = df[df["category"].str.lower() == "travel"]
    result = df1["amount"].sum()
    return result

def highest_spending_category(df):
    df1 = df[df["type"].str.lower( )== "expense"]
    lst = df1["category"].unique()
    d = {}
    for ele in lst:
        df2 = df1[(df1["category"].str.lower() == ele.lower())]
        d[ele] = df2["amount"].sum()
    max_val = max(d.values())
    result = ""
    for key in d:
        if d[key] == max_val:
            result = key
    return result

def lowest_spending_category(df):
    df1 = df[df["type"].str.lower( )== "expense"]
    lst = df1["category"].unique()
    d = {}
    for ele in lst:
        df2 = df1[(df1["category"].str.lower() == ele.lower())]
        d[ele] = df2["amount"].sum()
    max_val = min(d.values())
    result = ""
    for key in d:
        if d[key] == max_val:
            result = key
    return result

def payment_amount(df,payment_mode):
    df1 = df[df["payment_method"].str.lower() == payment_mode.lower()]
    result = df1["amount"].sum()
    return result

def payment_analysis(df):
    lst = df["payment_method"].unique()
    lst1 = []
    for ele in lst:
        if ele.lower() not in lst1:
            lst1.append(ele.lower())
    for ele in lst1:
        print(f"{ele}: RS. {payment_amount(df,ele.lower())}")

def expense_main():
    print("========== FINANCIAL SUMMARY ==========")
    print(f"Total Income:  RS. {total_income(df)}")
    print(f"Total Expense: RS. {total_expense(df)}")
    print(f"Total Savings: RS. {total_savings(df)}")
    print(f"Savings Percentage: {percentage_savings(df)}%")
    print(f"Average Expense: RS. {average_expense(df)}")
    print(f"Highest Expense: RS. {highest_expense(df)}")
    print(f"Lowest Expense: RS. {lowest_expense(df)}")

    print("\n========== CATEGORY ANALYSIS ==========")
    print(f"Food: RS. {food_expense(df)}")
    print(f"Shopping: RS. {shopping_expense(df)}")
    print(f"Transport: RS. {transport_expense(df)}")
    print(f"Bills: RS. {bills_expense(df)}")
    print(f"Entertainment: RS. {entertainment_expense(df)}")
    print(f"Education: RS. {education_expense(df)}")
    print(f"Travel: RS. {travel_expense(df)}")
    print(f"Highest spending catgory: {highest_spending_category(df)}")
    print(f"Lowest spending catgory: {lowest_spending_category(df)}")

    print("\n========== PAYMENT ANALYSIS ==========")
    payment_analysis(df)

def total_budget(df):
    result = df['budget'].sum()
    return result

def total_expense(df):
    df1 = df[df["type"].str.lower() == "expense"]
    result = df1["amount"].sum()
    return result

def budget_used(df):
    result = (total_expense(df) / total_budget(df)) * 100
    return round(result,2)

def remaining_budget(df):
    result = total_budget(df) - total_expense(df)
    return result

def analysis(df):
    df1 = df[df['type'].str.lower() == "expense"]

    categories = list(df1['category'].unique())
    new_categories = []

    for c in categories:
        if c.lower() not in new_categories:
            new_categories.append(c.lower())

    print(f"{'Category':<18}{'Budget':<15}{'Actual':<15}{'Remaining':<18}{'Status'}")
    print("-" * 80)

    for c in new_categories:
        df2 = df1[df1["category"].str.lower() == c]

        cat = c
        budget = df2["budget"].sum()
        actual = df2["amount"].sum()
        remaining = budget - actual

        if remaining < 0:
            status = "Over budget"
        else:
            status = "Under budget"

        print(f"{cat:<18}RS. {budget:<14.2f}RS. {actual:<14.2f}RS.{remaining:<17.2f}{status}")

def budget_main():
    print("========== BUDGET ANALYSIS ==========")
    print(f"Total budget: RS. {total_budget(df)}")
    print(f"Total Expnese: RS. {total_expense(df)}")
    print(f"Remaining budget: RS. {remaining_budget(df)}")
    print(f"budget used: {budget_used(df)}%")
    print("\n")
    analysis(df)

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

def category_transaction_share(df):
    print("Category Transaction Share")
    print(30 * "-")
    category = df["category"].unique()
    new_category = []
    for cat in category:
        if cat.lower() not in new_category:
            new_category.append(cat.lower())
    for cat in new_category:
        df1 = df[df["category"].str.lower() == cat]
        total = df["amount"].sum()
        cat_total = df1["amount"].sum()
        percentage = (cat_total/total)*100
        percentage = round(percentage,2)
        print(f"{cat:<18}:    {percentage}%")

def category_spending_share(df):
    df1 = df[df["type"].str.lower() == "expense"]
    print("Category Spending Share")
    print(30 * "-")
    category = df1["category"].unique()
    new_category = []
    for cat in category:
        if cat.lower() not in new_category:
            new_category.append(cat.lower())
    for cat in new_category:
        df2 = df1[df1["category"].str.lower() == cat]
        total = df1["amount"].sum()
        cat_total = df2["amount"].sum()
        percentage = (cat_total/total)*100
        percentage = round(percentage,2)
        print(f"{cat:<18}:    {percentage}%")

def median_transation_amount(df):
    median_amount = df["amount"].median()
    median_amount = round(median_amount,2)
    print(f"Median transaction amount: RS. {median_amount}")

def above_average_transactions(df):
    mean_amount = df["amount"].mean()
    mean_amount = round(mean_amount,2)
    count_transaction = df[df["amount"] > mean_amount]["amount"].count()
    print(f"Above average transactions: {count_transaction}")

def average_spending_payment_method(df):
    df1 = df[df["type"].str.lower() == "expense"]
    payment_method = df1["payment_method"].unique()
    new_payment_method = []
    for pm in payment_method:
        if pm.lower() not in new_payment_method:
            new_payment_method.append(pm.lower())
    print("Average Spending By Payment Method")
    print("-" * 35)
    for pm in new_payment_method:
        amount = df1[df1["payment_method"].str.lower() == pm]["amount"].mean()
        amount = round(amount,2)
        print(f"{pm:<18}:    RS. {amount}")

def highest_average_trasaction_category(df):
    category = df["category"].unique()
    new_category = []
    for cat in category:
        if cat.lower() not in new_category:
            new_category.append(cat.lower())
    max_mean = -1
    max_cat = ""
    for cat in new_category:
        amount = df[df["category"].str.lower() == cat]["amount"].mean()
        if amount > max_mean:
            max_mean = amount
            max_cat = cat
    max_mean = round(max_mean,2)
    print("Highest Average Trasaction By Category")
    print("-" * 30)
    print(f"Category: {max_cat}")
    print(f"Average: RS. {max_mean}")

def smallest_category_by_transaction(df):
    category = df["category"].unique()
    new_category = []
    for cat in category:
        if cat.lower() not in new_category:
            new_category.append(cat.lower())
    min_count = df[df["category"].str.lower() == new_category[0]]["category"].count()
    min_cat = new_category[0]
    for cat in new_category:
        count = df[df["category"].str.lower() == cat]["category"].count()
        if count < min_count:
            min_count = count
            min_cat = cat
    print("Smallest Category By Transactions")
    print(30 * "-")
    print(f"Category: {min_cat}")
    print(f"Transactions: {min_count}")

def transaction_by_day(df):
    df["day"] = pd.to_datetime(df["date"]).dt.dayofweek
    days = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    print("Transactions by Day")
    print(25 * "-")
    for i in range(7):
        day = days[i]
        count = df[df["day"] == i]["transaction_id"].count()
        print(f"{day:<15}:    {count}")

def cashless_expesne_percentage(df):
    total = df[df["type"].str.lower() == "expense"]["transaction_id"].count()
    cashless_count = df[(df["type"].str.lower() == "expense") & (df["payment_method"].str.lower() != "cash")]["transaction_id"].count()
    percent = (cashless_count)/(total)
    percent = round(percent,2) * 100
    print(f"Cashless Expense percentage: {percent}%")

def income_transacions(df):
    count = df[df["type"].str.lower() == "income"]["transaction_id"].count()
    print(f"Income Transactions: {count}")

def expense_transaction(df):
    count = df[df["type"].str.lower() == "expense"]["transaction_id"].count()
    print(f"Expense Transactions: {count}")

def spending_main():
    print("========== SPENDING BEHAVIOUR ==========")
    category_transaction_share(df)
    print("\n")
    category_spending_share(df)
    print("\n")
    median_transation_amount(df)
    above_average_transactions(df)
    print("\n")
    average_spending_payment_method(df)
    print("\n")
    highest_average_trasaction_category(df)
    print("\n")
    smallest_category_by_transaction(df)
    print("\n")
    transaction_by_day(df)
    print("\n")
    cashless_expesne_percentage(df)
    print("\n")
    income_transacions(df)
    expense_transaction(df)
    print("\n")

def main():
    print("=============== ANALYSIS REPORT ===============")
    expense_main()
    trend_main()
    budget_main()
    spending_main()

f = io.StringIO()

with redirect_stdout(f):
    main()
output = f.getvalue()
pdf = FPDF()
pdf.set_auto_page_break(auto=True,margin = 15)
pdf.add_page()
pdf.set_font("Arial",size = 12)
pdf.multi_cell(0,10,output)
pdf.output("11_report.pdf")
print("Report is created successfully!")
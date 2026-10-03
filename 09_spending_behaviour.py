import pandas as pd

df = pd.read_excel("01_data.xlsx")

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

spending_main()
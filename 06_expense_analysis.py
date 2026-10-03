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

expense_main()
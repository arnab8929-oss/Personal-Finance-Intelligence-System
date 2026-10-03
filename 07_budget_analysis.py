import pandas as pd

df = pd.read_excel("01_data.xlsx")

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

budget_main()
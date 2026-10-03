import pandas as pd

df = pd.read_excel("01_data.xlsx")

def print_df(df):
    try:
        print("\n")
        print(
            f"{'transaction_id':<16}"
            f"{'date':<12}"
            f"{'type':<12}"
            f"{'category':<15}"
            f"{'description':<25}"
            f"{'amount':<12}"
            f"{'payment_method':<18}"
            f"{'budget':<12}"
        )

        print("-" * 120)
        df["date"] = pd.to_datetime(df["date"]).dt.date
        for i in range(len(df)):
            row = df.iloc[i]

            print(
                f"{str(row['transaction_id']):<15}"
                f"{str(row['date']):<14}"
                f"{str(row['type']):<12}"
                f"{str(row['category']):<15}"
                f"{str(row['description']):<25}"
                f"{str(row['amount']):<12}"
                f"{str(row['payment_method']):<18}"
                f"{str(row['budget']):<12}"
            )

    except Exception as e:
        print(f"error: {e}")

def search_by_transaction_id(df):
    try:
        transaction_id = int(input("Transaction ID: "))
        print("Number filters:")
        print("1.Equals\n2.Greater than\n3.Less than\n4.Greater than equals\n5.Less than equals\n")
        choice = int(input("choice: "))
        result = None
        match choice:
            case 1:
                result = df.loc[df["transaction_id"] == transaction_id]
            case 2:
                result = df.loc[df["transaction_id"] > transaction_id]
            case 3:
                result = df.loc[df["transaction_id"] < transaction_id]
            case 4:
                result = df.loc[df["transaction_id"] >= transaction_id]
            case 5:
                result = df.loc[df["transaction_id"] <= transaction_id]
        if not result.empty:
            print_df(result)
        else:
            print("No results found!")
    except Exception as e:
        print(f"error:{e}")

def search_by_date(df):
    try:
        date = input("date (YYYY-MM-DD): ")
        date = pd.to_datetime(date).date()
        print("Date filters:")
        print("1.Exact date\n2.Before date\n3.After date\n4.Before including current date\n5.After including current date\n")
        choice = int(input("choice: "))
        result = None

        df["date"] = pd.to_datetime(df["date"]).dt.date

        match choice:
            case 1:
                result = df.loc[df["date"] == date]
            case 2:
                result = df.loc[df["date"] < date]
            case 3:
                result = df.loc[df["date"] > date]
            case 4:
                result = df.loc[df["date"] <= date]
            case 5:
                result = df.loc[df["date"] >= date]

        if not result.empty:
            print_df(result)
        else:
            print("no results found!")
    except Exception as e:
        print(f"error{e}")

def search_by_type(df):
    try:
        df_type = input("Type: ")
        print(f"results for type = {df_type.lower()}:")
        result = df[df["type"].str.lower() == df_type.lower()]

        if not result.empty:
            print_df(result)
        else:
            print("no results found!")

    except Exception as e:
        print(f"error: {e}")

def search_by_category(df):
    try:
        category = input("Category: ")
        print(f"results for category = {category.lower()}:")
        result = df[df["category"].str.lower() == category.lower()]
        if not result.empty:
            print_df(result)
        else:
            print("no results found!")
    except Exception as e:
        print(f"error: {e}")

def search_by_amount(df):
    try:
        amount = int(input("amount: "))
        print("Number filters:")
        print("1.Equals\n2.Greater than\n3.Less than\n4.Greater than equals\n5.Less than equals\n")
        choice = int(input("choice: "))
        result = None
        match choice:
            case 1:
                result = df.loc[df["amount"] == amount]
            case 2:
                result = df.loc[df["amount"] > amount]
            case 3:
                result = df.loc[df["amount"] < amount]
            case 4:
                result = df.loc[df["amount"] >= amount]
            case 5:
                result = df.loc[df["amount"] <= amount]
        if not result.empty:
            print_df(result)
        else:
            print("No results found!")
    except Exception as e:
        print(f"error:{e}")

def search_by_payment_method(df):
    try:
        payment_method = input("payment method: ")
        print(f"results for payment method = {payment_method.lower()}")
        result = df[df["payment_method"].str.lower() == payment_method.lower()]

        if not result.empty:
            print_df(result)
        else:
            print("no results found!")
    except Exception as e:
        print(f"error:{e}")

def search_by_budget(df):
    try:
        budget = int(input("budget: "))
        print("Number filters:")
        print("1.Equals\n2.Greater than\n3.Less than\n4.Greater than equals\n5.Less than equals\n")
        choice = int(input("choice: "))
        result = None
        match choice:
            case 1:
                result = df.loc[df["budget"] == budget]
            case 2:
                result = df.loc[df["budget"] > budget]
            case 3:
                result = df.loc[df["budget"] < budget]
            case 4:
                result = df.loc[df["budget"] >= budget]
            case 5:
                result = df.loc[df["budget"] <= budget]
        if not result.empty:
            print_df(result)
        else:
            print("No results found!")
    except Exception as e:
        print(f"error:{e}")

def main():
   print("1.Search by transaction id\n2.Search by date\n3.Search by type\n4.Search by category\n5.Search by amount\n6.Search by payment method\n7.Search by budget\n")
   choice = int(input("choice: "))
   match choice:
       case 1:
           search_by_transaction_id(df)
       case 2:
           search_by_date(df)
       case 3:
           search_by_type(df)
       case 4:
           search_by_category(df)
       case 5:
           search_by_amount(df)
       case 6:
           search_by_payment_method(df)
       case 7:
           search_by_budget(df)
       case _:
           print("Invalid!")          
main()
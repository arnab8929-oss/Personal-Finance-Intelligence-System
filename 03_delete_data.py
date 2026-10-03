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

def delete_by_id(df):
    try:
        transaction_id = int(input("transaction_id: "))
        if transaction_id in df["transaction_id"].values:
             temp = df.loc[df["transaction_id"] == transaction_id]
             print_df(temp)
             print(f"\nDo you want to delete record with transaction ID {transaction_id}?")
             print("1.Yes\n2.No")
             choice = int(input("choice: "))
             if choice == 1:
                 df = df.loc[df["transaction_id"] != transaction_id]
                 df["date"] = pd.to_datetime(df["date"]).dt.date
                 df.to_excel("01_data.xlsx",index = False)
                 print(f"record with transaction ID {transaction_id} is deleted.")
             elif choice == 2:
                 print(f"no changes done.")
             else:
                 print(f"Invalid choice!")        
        else:
            print("no results found!")
    except Exception as e:
        print(f"error{e}")

def delete_by_date(df):
    try:
        print("Date range (YYYY-MM-DD):")
        date1 = input("first date: ")
        date2 = input("last date: ")
        date1 = pd.to_datetime(date1).date()
        date2 = pd.to_datetime(date2).date()
        df["date"] = pd.to_datetime(df["date"]).dt.date
        temp = df.loc[(df["date"] >= date1) & (df["date"] <= date2)]

        if temp.empty:
            print("No results found!")
            return
        
        print_df(temp)
        print("Are you confirm to delete?")
        print("1.Yes\n2.No")
        choice = int(input("choice: "))
        if choice == 1:
            df = df.loc[(df["date"] < date1) | (df["date"] > date2)]
            df.to_excel("01_data.xlsx",index=False)
            print(f"{len(temp)} records between {date1} and {date2} is deleted.")
        elif choice == 2:
            print("no changes done.")
        else:
            print("Invalid!")

    except Exception as e:
        print(f"error{e}")

def delete_by_category(df):
    try:
        category = input("category: ")
        temp = df.loc[df["category"].str.lower() == category.lower()]
        if temp.empty:
            print("No results found!")
            return
        print_df(temp)
        print("Are you confirm to delete?")
        print("1.Yes\n2.No")
        choice = int(input("choice: "))

        if choice == 1:
            df = df.loc[df["category"].str.lower() != category.lower()]
            df["date"] = pd.to_datetime(df["date"]).dt.date
            df.to_excel("01_data.xlsx",index=False)
            print(f"{len(temp)} records of category {category} is deleted.")
        elif choice == 2:
            print("no changes done.")
        else:
            print("Invalid!")
    except Exception as e:
        print(f"error:{e}")

def delete_by_amount(df):
    try:
        amount = int(input("amount: "))
        print("Number filters:")
        print("1.Equals\n2.Greater than\n3.Less than\n4.Greater than equals\n5.Less than equals\n")
        choice = int(input("choice: "))
        temp = None
        match choice:
            case 1:
                temp = df.loc[df["amount"] == amount]
                df1 = df.loc[df["amount"] != amount]
            case 2:
                temp = df.loc[df["amount"] > amount]
                df1 = df.loc[df["amount"] <= amount]
            case 3:
                temp = df.loc[df["amount"] < amount]
                df1 = df.loc[df["amount"] >= amount]
            case 4:
                temp = df.loc[df["amount"] >= amount]
                df1 = df.loc[df["amount"] < amount]
            case 5:
                temp = df.loc[df["amount"] <= amount]
                df1 = df.loc[df["amount"] > amount]
        if temp.empty:
            print("no results found.")
            return
        print_df(temp)
        print("Are you confirm to delete?")
        print("1.Yes\n2.No\n")
        choice = int(input("choice: "))
        if choice == 1:
            df = df1
            df["date"] = pd.to_datetime(df["date"]).dt.date
            df.to_excel("01_data.xlsx",index=False)
            print(f"{len(temp)} records are deleted.")
        elif choice == 2:
            print("no changes done.")
        else:
            print("Invalid.")
    except Exception as e:
        print(f"error:{e}")

def delete_by_payment_method(df):
    try:
        payment_method = input("payment_method: ")
        temp = df.loc[df["payment_method"].str.lower() == payment_method.lower()]
        if temp.empty:
            print("no results found!")
            return
        print_df(temp)
        print("Are you confirm to delete?")
        print("1.Yes\n2.No\n")
        choice = int(input("choice: "))
        if choice == 1:
            df = df.loc[df["payment_method"].str.lower() != payment_method.lower()]
            df.to_excel("01_data.xlsx",index=False)
            print(f"{len(temp)} records of payment_method {payment_method} is deleted.")    
        elif choice == 2:
            print(f"no changes done.")
        else:
            print(f"Invalid!")    
    except Exception as e:
        print(f"error:{e}")

def main():
    print("1.Delete by transaction ID\n2.Delete by date\n3.Delete by category\n4.Delete by amount\n5.Delete by payment method\n")
    choice = int(input("choice: "))
    match choice:
        case 1:
            delete_by_id(df)
        case 2:
            delete_by_date(df)
        case 3:
            delete_by_category(df)
        case 4:
            delete_by_amount(df)
        case 5:
            delete_by_payment_method(df)
        case _:
            print("Invalid!")

main()
import pandas as pd

df = pd.read_excel("01_data.xlsx")
categories = ['salary','food','transport','shopping','entertainment','bills','education','healthcare','travel','investment','other','bonus']

def update_amount(df):
    try:
        transaction_id = int(input("transaction_id: "))
        temp = df.loc[df["transaction_id"] == transaction_id]
        if temp.empty:
            print("no results found!")
            return
        new_amount = int(input("New amount: "))
        old_amount = temp["amount"].values
        status = ""
        budget = temp["budget"].values
        if new_amount > budget:
            status = "Over budget"
        else:
            status = "Under budget"
        typ = temp["type"].values
        if typ[0].lower() == 'income':
            status = 'Not applicable'
        temp["amount"] = new_amount
        temp["status"] = status
        df.loc[df["transaction_id"] == transaction_id,"amount"] = temp["amount"]
        df.loc[df["transaction_id"] == transaction_id,"status"] = temp["status"]
        df["date"] = pd.to_datetime(df["date"]).dt.date
        df.to_excel("01_data.xlsx",index=False)
        print(f"Amount is changed from ₹{old_amount[0]} to ₹{new_amount} for trasaction id {transaction_id}")
    except Exception as e:
        print(f"error:{e}")

def update_category(df):
    try:
        transaction_id = int(input("transaction_id: "))
        old_category = df.loc[df["transaction_id"] == transaction_id,"category"].values
        new_category = input("category: ")
        if new_category.lower() not in categories:
            print("Invalid category!")
            return
        df.loc[df["transaction_id"] == transaction_id,"category"] = new_category.lower()
        df["date"] = pd.to_datetime(df["date"]).dt.date
        df.to_excel("01_data.xlsx",index = False)
        print(f"Category is changed from {old_category[0]} to {new_category} for transaction id {transaction_id}")
    except Exception as e:
        print(f"error:{e}")

def update_description(df):
    try:
        transaction_id = int(input("transaction_id: "))
        old_description = df.loc[df["transaction_id"] == transaction_id,"description"].values
        new_description = input("New description: ")
        df.loc[df["transaction_id"] == transaction_id,"description"] = new_description
        df["date"] = pd.to_datetime(df["date"]).dt.date
        df.to_excel("01_data.xlsx",index = False)
        print(f"Description is changed from {old_description[0]} to {new_description} for transaction id {transaction_id}")
    except Exception as e:
        print(f"error:{e}")

def update_budget(df):
    try:
        transaction_id = int(input("transaction_id: "))
        old_budget = df.loc[df["transaction_id"] == transaction_id,"budget"].values
        temp = df.loc[df["transaction_id"] == transaction_id]
        if (temp["type"].values)[0].lower() == 'income':
            print("This Updation is not valid!")
            return
        new_budget = int(input("New budget: "))
        amount = temp["amount"].values
        status = ""
        if amount[0] > new_budget:
            status = "Over budget"
        else:
            status = "Under budget"
        df.loc[df["transaction_id"] == transaction_id,"budget"] = new_budget
        df.loc[df["transaction_id"] == transaction_id,"status"] = status
        df["date"] = pd.to_datetime(df["date"]).dt.date
        df.to_excel("01_data.xlsx",index = False)
        print(f"Budget is changed from {old_budget[0]} to {new_budget} for transaction id {transaction_id}")
    except Exception as e:
        print(f"error:{e}")

def main():
   print("1.Update amount\n2.Update category\n3.Update description\n4.Update budget\n")
   choice = int(input("choice: "))
   match choice:
       case 1:
           update_amount(df)
       case 2:
           update_category(df)
       case 3:
           update_description(df)
       case 4:
           update_budget(df)
       case _:
           print("Invalid!")          
main()
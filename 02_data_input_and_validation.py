import pandas as pd

def data_input_and_validation():
    try:
        transaction_id = int(input("transaction_id: "))
        date = input("date (YYYY-MM-DD): ")
        type1 = input("type: ")
        category = input("category: ")
        description = input("description: ")
        amount = float(input("amount: "))
        payment_method = input("payment_method: ")
        budget = float(input("budget: "))

        df = None
        types = ['income','expense']
        categories = ['salary','food','transport','shopping','entertainment','bills','education','healthcare','travel','investment','other','bonus']
        payment_methods = ['upi','cash','credit card','debit card','bank transfer','net banking']
        try:
            df = pd.read_excel("01_data.xlsx")
        except FileNotFoundError:
            print("file not found error!")
            return
        if transaction_id < 0:
            print("negative transaction id does not allowed!")
            return
        if transaction_id in df['transaction_id'].values:
            print("duplicate values is not allowed!")
            print(f"Last transtion id:{df['transaction_id'].values[-1]}")
            return
        if pd.notna(pd.to_datetime(date,errors='coerce')):
            date = pd.to_datetime(date).date()
        else:
            print("invalid date")
            return
        if type1.lower() not in types:
            print("Invalid type!")
            return
        else:
            type1 = type1.lower()
        if category.lower() not in categories:
            print("Invalid category")
            return
        else:
            category = category.lower()
        if amount <= 0:
            print("Invalid amount!")
            return
        if payment_method.lower() not in payment_methods:
            print("Invalid payment method!")
        else:
            payment_method = payment_method.lower()
        if len(description) == 0:
            print("description should not be empty!")
            return
        else:
            description = description.lower()
        if budget < 0:
            print("Invalid budget!")
            return
        amount = round(amount,2)
        budget = round(budget,2)
        status = ""
        if type1.lower() == "income":
            status = "Not applicable"
        else:
            if amount > budget:
                status = "Over budget"
            else:
                status = "Under budget"
        day_of_the_week = date.strftime("%A")
        new_transaction = {
            "transaction_id":transaction_id,
            "date":date,
            "type":type1,
            "category":category,
            "description":description,
            "amount":amount,
            "payment_method":payment_method,  
            "budget":budget,
            "status":status,
            "day of the week":day_of_the_week
        }
        df.loc[len(df)] = new_transaction
        df["date"] = pd.to_datetime(df['date']).dt.date
        df.to_excel("01_data.xlsx",index=False)
        print("transaction is stored in 01_data.xlsx")
        return
    except Exception as e:
        print(f"error:{e}")
        return

data_input_and_validation()
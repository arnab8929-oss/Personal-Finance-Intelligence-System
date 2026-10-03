import subprocess as sb

def main():
    while True:
        print("_______________PERSONAL FINANCE INTELLIGENCE SYSTEM_______________")
        print("1.Insert Data\n2.Delete Data\n3.Update Data\n4.Search Data\n5.Expense Analysis\n6.Budget Analysis\n7.Trend Analysis\n8.Spending Behaviour Analysis\n9.Report Generation\n10.Data Visualization\n11.Exit\n")
        print("___________________________________________________________________")
        choice = int(input("choice: "))
        file = ""
        match choice:
            case 1:
                file = "02_data_input_and_validation.py"
            case 2:
                file = "03_delete_data.py"
            case 3:
                file = "04_update_data.py"
            case 4:
                file = "05_search_data.py"
            case 5:
                file = "06_expense_analysis.py"
            case 6:
                file = "07_budget_analysis.py"
            case 7:
                file = "08_trend_analysis.py"
            case 8:
                file = "09_spending_behaviour.py"
            case 9:
                file = "10_report_generation.py"
            case 10:
                file = "13_data_visualization.py"
            case 11:
                print("Program Finished!")
                break
            case _:
                print("Invalid choice!")
        
        print("-------------------------------------------------------------------")
        sb.run(["python",file])
        print("-------------------------------------------------------------------")

main()
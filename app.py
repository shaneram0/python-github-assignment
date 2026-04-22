print("Welcome to Shane's USF Python Assignment!")
#Folder made, welcome message 

work_hours = input("How many hours did you work this week? ")
#User input for hours worked

work_hours = float(work_hours)
weekly_pay = work_hours * 16.50
#Calculating weekly pay based on user input

print("Your weekly pay is: $", "{:.2f}".format(weekly_pay))
#Formatted output to show weekly pay

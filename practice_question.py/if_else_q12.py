# program for employee bonus calculation
employee_service = int(input("Enter service years: "))
salary = int(input("Enter salary: "))

if employee_service >= 5:
    if salary < 50000:
        total_salary = salary + (salary * 5) / 100
        print("Total Salary with 5% bonus:", total_salary)
    else:
        total_salary = salary + (salary * 10) / 100
        print("Total Salary with 10% bonus:", total_salary)
else:
    print("No bonus, total salary:", salary)
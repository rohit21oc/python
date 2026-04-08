"""Q35. Take Salary as input from User and Update the salary of an employee.

salary less than 10,000, 5% increment

salary between 10,000 and 20, 000, 10% increment

⚫ salary between 20,000 and 50,000, 15% increment

⚫ salary more than 50,000, 20% increment

"""
emp_salary = int(input("Enter the salary: "));

if emp_salary<10000:
    increment = 5;
elif emp_salary>=10000 and emp_salary < 20000:
    increment = 10;
elif emp_salary>=20000 and emp_salary < 50000:
    increment = 15;
elif emp_salary>=50000:
    increment = 20;

print(f"Salary increament is {(emp_salary/100)*increment}")
final_salary = (emp_salary/100)*increment + emp_salary

print(f"Final salary: {final_salary}")

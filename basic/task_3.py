name = input("Enter your name: ")
salary = input("Enter your salary: ")
department = input("Enter your department: ")

employeeData  = {
    "name" : name,
    "salary" : int(salary),
    "department" : department
}

def calculate_salary(data):
    if data["salary"] > 20000:
        salaryStatus = "Good Salary"
    elif data["salary"] < 20000:
        salaryStatus = "basic Salary"
    else:
        salaryStatus = "salary"
    return salaryStatus
calculate_salary(employeeData)

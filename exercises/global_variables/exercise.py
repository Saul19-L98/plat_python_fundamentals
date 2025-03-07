EmployeesWithhigherSalaries = []

employees = [
    {"name": "Juan", "age": 28, "salary": 3500},
    {"name": "María", "age": 32, "salary": 4200},
    {"name": "Carlos", "age": 25, "salary": 3100},
    {"name": "Ana", "age": 40, "salary": 5000},
    {"name": "Luis", "age": 30, "salary": 3900},
]

for item in EmployeesWithhigherSalaries:
    print(item['name'])

def getEmployessBySalary(salary: float):
    global EmployeesWithhigherSalaries
    EmployeesWithhigherSalaries =  [ employee for employee in employees if employee['salary'] > salary]
    print(f"Employees with a higher salary than {salary} are {len(EmployeesWithhigherSalaries)}")

getEmployessBySalary(3500)
for item in EmployeesWithhigherSalaries:
    print(item['name'])



#This decorator validates if the employee has an specific role.
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            #Validate if the employee role has the required role
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f"ACCESS DENIED. Just employees with the role {required_role} can execute this action.")
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f"Saving employee {employee['name']} action.")
        return func(employee)
    return wrapper

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f"Employe {employee['name']}, has been deleted.")


admin = {'name':'Carlos','role':"admin"}
employee = {'name':'Ana','role':"employee"}

delete_employee(employee)

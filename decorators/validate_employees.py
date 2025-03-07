def check_access(func):
    def wrapper(employee):
        #Validated employee role 'admin'
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('ACCESS DENIED. Only the administrators can access.')
    return wrapper

@check_access
def delete_employee(employee):
    print(f"Employee {employee['name']} has been deleted.")

admin = {'name':'Carlos','role':'admin'}
employee = {'name':'Ana','role':'employee'}

delete_employee(admin)
delete_employee(employee)
# def log_employee_action(func):
#     def wrapper(employee):
#         with open('report.txt', 'w') as report_file:
#             for employee in employees:
#                 report_file.write(f"Employee: {employee['name']}, Action: {employee['action']}\n")        
#     return wrapper

# @log_employee_action
# def employee_execute(employee):
#     print(f"Employee: {employee['name']}, action executed.")

# employees = [
#     {'name':'Ana','action':'query db'},
#     {'name':'Eddie','action':'push to remote repository'},
#     {'name':'Susan','action':'query reports'}
# ]

# employee_execute(employees)
from collections import deque
from datetime import datetime
class Employee_Action:
    list_employees = dict # {name: {rol: "", job_title: ""}}
    log = dict # {name_employee: {date_change: "", text_added: ""}}

    def __init__(self, list_employees: dict):
        self.list_employees = list_employees
        self.log = {}

    def show_log(func):
        def wrapped(self, name_employee: str, text_file: str, posicion: str, new_text: str):
            now = datetime.now().date()
            self.log[name_employee] = {
                "date_change": now,
                "text_added": new_text,
            }
            print(self.log)
            return func(name_employee, text_file, posicion, new_text)

        return wrapped

    @show_log
    def add_text_to_file (name: str, text_file: str, posicion: str, new_text: str):
        deque_text = deque(text_file)
        if posicion == 'I' or posicion == 'i':
            deque_text.extendleft(new_text[::-1])
        elif posicion == 'F' or posicion == 'f':
            deque_text.extend(new_text)

        texto_final = ''.join(deque_text)
        return texto_final

lista = {
    "Cristian": {"rol": "admin", "job_title": "Senior Developer"},
    "David": {"rol": "employee", "job_title": "Mid Developer"},
    "Mora": {"rol": "employee", "job_title": "Mid Developer"},
    "Saenz": {"rol": "employee", "job_title": "Junior Developer"}
}   

st = True
text_file = "¡Hola mundo!"

while st == True:

    name = str(input("\n Escriba su nombre (El registrado): ")).lower()
    pos = str(input("\n Para escribir al inicio digite la letra [ I ] / Para escribir al final [ F ]: "))
    new_text = str(input("\n Escriba el texto que desea guardar: "))

    obj = Employee_Action(lista)
    print(obj.add_text_to_file(name, text_file, pos, new_text))

    des = str(input("Desea continuar digite [ Y ] / [ N ]: "))

    if des in ('y','Y'):
        st = True
    elif des in ('N', 'n'):
        st = False
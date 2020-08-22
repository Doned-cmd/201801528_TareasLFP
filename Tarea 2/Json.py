import json
def lectorJSON(archivo):
    print("==========JSON==========")
    with open(archivo) as file:
        data = json.load(file)
        for empleado in data['empleado']:
            print('nombre:', empleado['nombre'])
            print('edad:', empleado['edad'])
            print('username:', empleado['username'])
            print('password:', empleado['password'])
            print('\n')


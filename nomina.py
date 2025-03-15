##US1/Registrar empleado

usuarios = [[],[]]

def registrar_empleado():
    print("Registrar empleado")
    usuario = []
    id = int(input("ID: "))
    usuario.append(id)
    nombre = input("Nombre: ")
    usuario.append(nombre)
    apellido = input("Apellido: ")
    usuario.append(apellido)
    cedula = input("Cedula: ")
    usuario.append(cedula)
    edad = input("Edad: ")
    usuario.append(edad)
    genero = input("Genero: ")
    usuario.append(genero)
    salario = input("Salario: ")
    usuario.append(salario)
    usuarios.append(usuario)

    print("Empleado registrado con exito")

registrar_empleado()
print(usuarios)


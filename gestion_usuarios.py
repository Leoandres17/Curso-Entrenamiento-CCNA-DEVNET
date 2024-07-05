import hashlib
import sqlite3
from getpass import getpass

# Función para conectar y crear la base de datos SQLite
def crear_bd():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    # Crear tabla si no existe
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (nombre TEXT, apellido TEXT, usuario TEXT, hash_contrasena TEXT)''')

    conn.commit()
    conn.close()

# Función para generar hash de contraseña usando hashlib
def generar_hash(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = getpass("Ingrese su contraseña: ")

    hash_contrasena = generar_hash(contrasena)

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    # Insertar usuario en la base de datos
    c.execute("INSERT INTO usuarios (nombre, apellido, usuario, hash_contrasena) VALUES (?, ?, ?, ?)",
              (nombre, apellido, usuario, hash_contrasena))

    conn.commit()
    conn.close()

    print("Usuario registrado exitosamente.")

# Función para validar el usuario
def validar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    # Buscar usuario en la base de datos
    c.execute("SELECT * FROM usuarios WHERE nombre=? AND apellido=?", (nombre, apellido))
    usuario = c.fetchone()

    if usuario:
        print(f"Bienvenido, {nombre} {apellido}!")
    else:
        print("Usuario no encontrado.")

    conn.close()

# Crear la base de datos al inicio del script
crear_bd()

# Menú interactivo
while True:
    print("\n1. Registrar nuevo usuario")
    print("2. Validar usuario")
    print("3. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        validar_usuario()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

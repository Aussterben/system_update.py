#!/usr/bin/env python3

import os
import time
import sys

url_github = "https://github.com/Aussterben"

# Comprobación de permisos
if os.geteuid() != 0:
    print("\n[+] Debes ejecutar este script como root.")
    sys.exit(1)

def script_completo():
    print('''
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣀⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠈⣿⠁⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣋⡇⠀⠀⠀⠀⠀⢀⠟⡄⠀⠀⠀⠀⠀⣾⣯⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢠⠴⡄⠀⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⡸⠀⢧⠀⠀⠀⠀⠀⢀⣏⠁⠀⠀⠀⠀⠀⠀⣠⣦⡄
    ⠘⠓⠻⣤⡀⠀⠀⠀⠀⠀⡏⢣⠀⠀⠀⠀⢀⠇⠀⠸⡄⠀⠀⠀⠀⡜⢸⠀⠀⠀⠀⠀⠀⣠⡾⠟⠃
    ⠀⠀⠀⢣⠙⠦⡀⠀⠀⢠⠃⠈⢇⠀⠀⠀⡞⠀⠀⠀⢣⠀⠀⠀⡼⠁⢸⡄⠀⠀⢀⡴⠊⡞⠀⠀⠀
    ⠀⠀⠀⠈⡆⠀⠙⢦⠀⠸⠀⠀⠈⢆⠀⢰⠁⠀⠀⠀⠈⣇⠀⡰⠁⠀⠈⣇⠀⡰⠋⠀⢰⠀⠀⠀⠀
    ⠀⠀⠀⠀⢁⠀⠀⠀⠱⡇⠀⠀⠀⠈⢦⠇⠀⠀⠀⠀⠀⠘⡶⠁⠀⠀⠀⢸⠞⠀⠀⠀⡾⠀⠀⠀⠀
    ⠀⠀⠀⠀⢸⠀⠀⢀⣀⣀⣀⣤⣤⣤⣴⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⠀⠀⠀⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⣼⠶⢿⣟⠛⠉⠉⢩⡟⢧⠀⠀⠀⣴⠛⣦⠀⠀⢠⠞⢫⡉⠉⠙⢛⡟⠿⠶⡷⠀⠀⠀⠀
    ⠀⠀⠀⠀⠹⡄⠸⣽⣃⣀⣀⣈⣿⣯⣤⣤⣤⣬⣾⣥⣤⣤⣬⣷⣯⣀⣀⣀⣻⡼⠀⢰⠃⠀⠀⠀⠀
    ⠀⠀⠀⠀⢼⠗⠛⠋⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠛⠛⢻⡦⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⠉⠑⠒⠒⠂⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠒⠒⠒⠊⠉⠁⠀⠀⠀⠀
    ''')

script_completo()

while True:
    print("\n---------------\nMENÚ\n---------------")
    print("1. Actualizar sistema")
    print("2. Salir del programa")

    eleccion = input("\n[+] ¿Quieres actualizar el sistema?: ")

    if eleccion == "1":
        os.system("clear")
        os.system("sudo apt update 2>/dev/null && parrot-upgrade 2>/dev/null")
        time.sleep(0.5)
        print("\n[+] ¡Sistema actualizado!")
        print(f"[+] Más herramientas en github: {url_github}")
        break
    elif eleccion == "2":
        print("\n[+] No se actualizará el sistema")
        print(f"[+] Más herramientas en github: {url_github}")
        break

    else:
        print("\n[!] Elige entre '1' o '2'")
        print(f"[+] Más herramientas en github: {url_github}")


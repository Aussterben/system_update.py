#!/usr/bin/env python3

import subprocess
import os
import time
import sys
from termcolor import colored

url_github = "https://github.com/Aussterben"

# Comprobación de permisos
if os.geteuid() != 0:
    print("\n[+] Debes ejecutar este script como root.")
    sys.exit(1)

def script_completo():
    print(colored('''
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
    ''', 'red'))

script_completo()

while True:
    print(colored(f"\n---------------\nMENÚ\n---------------\n", 'white'))
    print(colored(f"1. Actualizar sistema", 'green'))
    print(colored(f"2. Salir del programa", 'blue'))

    eleccion = input(colored(f"\n[+] ¿Quieres actualizar el sistema?: ", 'yellow'))

    if eleccion == "1":
        os.system("clear")
        name = subprocess.getoutput("lsb_release -a | grep Description: | awk '{print $2}'")

        if "Arch" in name:
            print(colored(f"\n[+] Actualizando el sistema...", 'green'))
            os.system("sudo pacman -Syyu &>/dev/null")
            time.sleep(0.5)
            print(colored(f"\n[+] ¡Sistema actualizado!", 'green'))
            print(colored(f"[+] Más herramientas en github: {url_github}", 'yellow'))
            break

        elif "Parrot" in name:
            print(colored(f"\n[+] Actualizando el sistema...", 'green'))
            os.system("sudo parrot-upgrade &>/dev/null")
            time.sleep(0.5)
            print(colored(f"\n[+] ¡Sistema actualizado!", 'green'))
            print(colored(f"[+] Más herramientas en github: {url_github}", 'yellow'))
            break

        else:
            print(colored(f"\n[+] Actualizando el sistema...", 'green'))
            os.system("sudo apt update &>/dev/null")
            os.system("sudo apt upgrade &>/dev/null")
            time.sleep(0.5)
            print(colored(f"\n[+] ¡Sistema actualizado!", 'green'))
            print(colored(f"[+] Más herramientas en github: {url_github}", 'yellow'))
            break

    elif eleccion == "2":
        print(colored(f"\n[!] No se actualizará el sistema", 'red'))
        print(colored(f"[+] Más herramientas en github: {url_github}", 'yellow'))
        break

    else:
        print(colored(f"\n[!] Elige entre '1' o '2'", 'red'))
        print(colored(f"[+] Más herramientas en github: {url_github}", 'yellow'))


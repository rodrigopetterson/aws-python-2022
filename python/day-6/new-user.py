"""
Create New User
"""

"""
import os

def new_user(): 
    confirm = "N" 
    
    while confirm != "S": 
        username = input("Insira o nome do usuário a ser adicionado: ")
        print("Usar o nome de usuário '" + username + "'? (S/N)")
        confirm = input().upper()
        os.system("sudo adduser " + username)

new_user()
"""


import subprocess

# listar usuarios
subprocess.run(["cut", "-d:", "-f", "1", "/etc/passwd"])
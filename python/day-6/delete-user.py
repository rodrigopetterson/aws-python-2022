"""
Create New User
"""
import os

def delete_user(): 
    confirm = "N" 
    
    while confirm != "S": 
        username = input("Insira o nome do usuário a ser removido: ")
        print("Deseja remover o usuario: '" + username + "'? (S/N)")
        confirm = input().upper()
        os.system("sudo userdel -r " + username)
        print("Usuario removido com sucesso!")

delete_user()





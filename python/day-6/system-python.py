"""
System Python
"""

#import os

import subprocess

# listar arquivos do diretorio
#os.system("ls")

#subprocess.run(["ls"])

# listar arquivos do diretorio com infos
#subprocess.run(["ls","-l"])

# retornar informacoes de um arquivo especifico no diretorio
#subprocess.run(["ls","-l","README.md"])

"""
command="uname"
commandArgument="-a"

print(f'Gathering system information with command: {command} {commandArgument}')

subprocess.run([command,commandArgument])
"""


# retornar processos em execucao
command="ps"
commandArgument="-x"

print(f'Gathering active process information with command: {command} {commandArgument}')

subprocess.run([command,commandArgument])

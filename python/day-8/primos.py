# listar os numero primos de 1 a 250
numerosPrimos = []

for i in range(1, 250):
  if i > 1:
    for j in range(2, i):
      if(i % j == 0):
        break
    else:
      print(i)
      numerosPrimos.insert(0, i)

outfile = "./day-8/file.txt"

# escrever no arquivo
with open(outfile, "w") as file:
  file.write(str(numerosPrimos))

#ler o arquivo
with open(outfile, "r") as arquivo:
  print(arquivo.read())
  

        
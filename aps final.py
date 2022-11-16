import time
print ("Bem-vindo(a) ao sistema de cálculo da empresa GreenRouts Aviation, agora são: ",time.strftime('%I:%M:%S %p %Z'))
nome=str(input("Para começarmos, como podemos te chamar?:"))
x=nome.upper()
print("Parabens !!!,",x)
cargo=int(input("Agora nos informe seu cargo na nossa empresa: 1- Cliente, 2- Comissário(a) de Bordo, 3- Piloto, 4- Diretor(a), 5- Dono(a) da Companhia, 6- Outro : "))
if cargo == 6:
  print("Sentimos muito! Mas você não pode ter acesso à esses dados.")
  exit("sim" or "não")
if cargo == 5 or cargo <5:
  print("Tudo certo! Configuramos o sistema de acordo com seu cargo, agora podemos continuar!")

destino=int(input("Agora, escolha a opção desejada de acordo com nossos trajetos disponíveis: 1- Recife-Fernando de Noronha, 2- Porto Alegre-Manaus, 3- São Paulo-Orlando, 4- Rio de Janeiro-São Paulo, 5- São Paulo-Salvador, 6- São Paulo-Doha: "))
qtd = int(input("Digite quantas pessoas irão viajar junto com você: "))
if destino == 1:
  carbono = 53*qtd
if destino == 2:
  carbono = 205*qtd
if destino ==3:
  carbono = 476*qtd
if destino == 4:
  carbono = 53*qtd
if destino == 5:
  carbono = 110*qtd
if destino == 6:
  carbono = 878*qtd

arv = carbono // 7 

print("Seu vôo emitiu um total de",carbono,"kg de Co2. Para compensar sua emissão, você deverá plantar um total de",arv, "árvores nativas da Floresta Amazônica.")
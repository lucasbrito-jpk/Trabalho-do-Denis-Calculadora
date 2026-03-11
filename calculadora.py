#Calculadora de Aprovação Escolar

nome = input("Digite o nome do estudante: ")

soma_notas = 0
quantidade_trimestre = 3 
meta_aprovacão = 180

#Coletas as notas dos 3 Trimestre 
for i in range(1, quantidade_trimestre + 1 ):
    nota= float (input("Informe a nota{i}º período: "))
    soma_notas +=nota

print("-" * 30)
print (f"Estudante: { nome }")
print (f"Pontuação Total: {soma_notas}")

#Verifica o Status de Aprovação 
if soma_notas >= meta_aprovacão:
    print("Status: APROVADÃO! Parabes!! Finalmente!!")
else:
    pontos_faltantes = meta_aprovacão - soma_notas
    print ("Status: TENTE OUTRA VEZ!!!")
    print (f"Faltaram {pontos_faltante} pontos para atingir o mínimo de {meta_aprovação}.")
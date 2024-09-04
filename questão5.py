entrada = input("Insira seu nome: ")
entrada_ao_contrário = "" #está vazia para armazenar a entrada ao contrario

for i in range(len(entrada) -1, -1, -1): #percorre a entrada começando a leitura dos dados pelo fim e indo até o inicio. a iteração decrementa os valores para acessar a entrada ao contrário
    entrada_ao_contrário += entrada[i] #itera os valores da entrada lendo elas de trás para frente e armazena na variavel entrada_ao_contrário
    print(entrada_ao_contrário)


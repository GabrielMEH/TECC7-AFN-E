# bibliotecas
import copy

# funções
def preencher_tabela(estado_i, simb, estado_o):
    matriz_t[estados.index(estado_i)][alfabeto.index(simb)].append(estados.index(estado_o))

def imprime_matriz(matriz):
    """
    Função que imprime uma matriz onde cada linha é dividida por uma quebra de linha.
    :param matriz: lista de listas representando a matriz
    """
    for linha in matriz:
        print(" ".join(map(str, linha)))

def add_vazios(estados_atuais):
    stack = list(estados_atuais) #estados para percorrer
    fecho = set(estados_atuais) #estados que vão ser adicionados
    # percorre estados para percorrer
    while stack:
        estado = stack.pop() # remove estado sendo processado
        for e in matriz_t[estado][-1]:  # última coluna é a transição vazia
            if e not in fecho: # se o estado resultante não está na lista de resultados
                fecho.add(e) # adicione fecho ao resultado
                stack.append(e) #adiciona estado a lista de estados para percorrer
    
    return fecho

def percorre_afne(entrada):
    # Inicializar os estados ativos com o fecho-e dos estados iniciais
    estados_ativos = add_vazios([estados.index(estado_i)])
    
    # Processar cada símbolo da entrada
    for simb in entrada:
        novos_estados_ativos = set()
        
        for estado in estados_ativos:
            if simb in alfabeto:
                novos_estados_ativos.update(matriz_t[estado][alfabeto.index(simb)])
        
        # Atualizar os estados ativos com o fecho-e dos novos estados ativos
        estados_ativos = add_vazios(novos_estados_ativos)
    
    # Verificar se algum dos estados ativos é um estado final
    aceita = any(estados[e] == estado_f for e in estados_ativos)
    
    if aceita:
        return('Aceita')
    else:
        return('Rejeita')

# variáveis
alfabeto = []
estados = []
n_trans = 0
estado_i = ""
estado_f = ""

# entrada alfabeto
entrada = input("").strip()
alfabeto = entrada.split() # remover espaço no final da string
alfabeto.append('vazio')

# entrada estados
entrada = input("").strip() # remover espaço no final da string
estados = entrada.split()

# criando matriz de transição
# estados = Número de linhas
# alfabeto = Número de colunas
matriz_t = [[[] for _ in range(len(alfabeto))] for _ in range(len(estados))]

# entrada numero de transições
n_trans = input().strip()
n_trans = int(n_trans)

for i in range(n_trans):
    entrada = input("").strip()
    resultado = entrada.split()
    preencher_tabela(resultado[0], resultado[1], resultado[2])

# ler estado inicial e final
estado_i = input().strip()
estado_f = input().strip()

"""
# print teste
print(f"Lista de alfabeto: {alfabeto}")
print(len(alfabeto))
print(f"Lista de estados: {estados}")
print(len(estados))
print(n_trans)
imprime_matriz(matriz_t)
"""

# entrada número de testes
n_teste = input().strip()
n_teste = int(n_teste)

resultado_t = []
# entrada de testes
for i in range(n_teste):
    entrada = input().strip()
    # print(entrada)
    resultado_t.append(percorre_afne(entrada))

for r in resultado_t:
    print(r)
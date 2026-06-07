import math
import matplotlib.pyplot as plt

def gerar_grafico(x, y, titulo, xlabel, ylabel): # função para gerar gráficos

    plt.figure(figsize=(10, 6)) # tamanho do gráfico
    plt.plot(x, y, marker='o') 
    plt.title(titulo) 
    plt.xlabel(xlabel) # eixo x
    plt.ylabel(ylabel) # eixo y
    plt.grid(True) # grade do gráfico
    plt.show()

def perda_exponencial_poeira(): # função onde calcula a perda de eficiência da placa por acúmulo de poeira
    try:
            eficiencia_inicial = float(input("Eficiência inicial da placa (%): "))
            taxa_poeira = float(input("Taxa diária de perda por poeira (%): ")) 
            dias = int(input("Quantidade de dias sem limpeza: "))

            if eficiencia_inicial <= 0 or eficiencia_inicial > 100:
                print("A eficiência inicial deve ser um valor entre 0 e 100.")
                return
            
            if taxa_poeira < 0 or taxa_poeira > 100:
                print("A taxa de perda por poeira deve ser um valor entre 0 e 100.")
                return
            
            if dias < 0:
                print("A quantidade de dias deve ser um valor positivo.")
                return
            
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return
    
    lista_dias = list(range(dias + 1))
    eficiencias = [] # lista para guardar as eficiencias calculadas

    for d in lista_dias: 
        eficiencia = eficiencia_inicial * math.exp(-(taxa_poeira/100) * d) # calcula a eficiencia utilizando função exponencial
        eficiencias.append(eficiencia)

    eficiencia_final = eficiencias[-1]
    perda = eficiencia_inicial - eficiencia_final # perda total de eficiência

    print("\nResultados:")
    print(f"Eficiência inicial: {eficiencia_inicial:.2f}%")
    print(f"Eficiência final: {eficiencia_final:.2f}%")
    print(f"Perda total: {perda:.2f}%")

    gerar_grafico(lista_dias, eficiencias, "Perda de Eficiência por Poeira", "Dias sem Limpeza", "Eficiência (%)")

def recuperacao_limpeza(): # função onde calcula a recuperação de eficiência após a limpeza
    print("\n--- OPÇÃO 2: RECUPERAÇÃO DE EFICIÊNCIA APÓS LIMPEZA ---")

    try:
        poeira_nivel = float(input("Nível de poeira acumulada (0 a 100): ")) # quantidade de poeira atual
        recuperacao_maxima = float(input("Recuperação máxima possível após limpeza (%): ")) # quantidade de até quanto a limpeza consegue recuperar
        ponto_ideal = float(input("Nível de poeira em que a limpeza tem maior efeito (%): ")) # nivel onde a poeira alcança o maior impacto, ou seja, o topo da parabola
        
        if poeira_nivel < 0 or poeira_nivel > 100:
            print("O nível de poeira deve ser um valor entre 0 e 100.")
            return
        
        if recuperacao_maxima <= 0 or recuperacao_maxima > 100:
            print("A recuperação máxima deve ser um valor entre 0 e 100.")
            return
        
        if ponto_ideal < 0 or ponto_ideal > 100:
            print("O ponto ideal deve ser um valor entre 0 e 100.")
            return
        
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    abertura = 0.01  # abertura da parábola pode ser ajustada conforme necessário
    recuperacao = -abertura * (poeira_nivel - ponto_ideal) ** 2 + recuperacao_maxima # calcula a recuperação utilizando função quadrática

    if recuperacao < 0:
        recuperacao = 0 # se a recuperação for negativa, ela vira 0
    elif recuperacao > recuperacao_maxima:
        recuperacao = recuperacao_maxima # se a recuperação passar do valor permitido, ela vira o valor máximo

    print("\nResultados:")
    print(f"Nível de poeira: {poeira_nivel:.2f}%")
    print(f"Recuperação de eficiência após a limpeza: {recuperacao:.2f}%")

    poeiras = list(range(0, 101))
    recuperacoes = []

    for poeira in poeiras: # valor de cada poeira ( de 0 a 100 )
        r = -abertura * (poeira - ponto_ideal) ** 2 + recuperacao_maxima 

        if r < 0:
            r = 0
        elif r > recuperacao_maxima:
            r = recuperacao_maxima

        recuperacoes.append(r)

    gerar_grafico(poeiras, recuperacoes, "Recuperação de Eficiência por Nível de Poeira", "Nível de Poeira (%)", "Recuperação de Eficiência (%)")

def economia_limpezas():
    print("\n--- OPÇÃO 3: Limpezas economizadas pelo sistema ---")

    try:
        custo_limpeza = float(input("Custo de cada limpeza (R$): ")) # custo de cada limpeza
        limpezas = int(input("Número de limpezas realizadas por ano sem tecnologia: ")) # total de limpezas sem utilizar o sistema EDS

        if custo_limpeza < 0:
            print("O custo de limpeza deve ser um valor positivo.")
            return
        
        if limpezas <= 0:
            print("O número de limpezas deve ser maior que zero.")
            return
        
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    economia = custo_limpeza * math.log(limpezas + 1) # Calcula a economia usando função logaritmica
    print("\nResultados:")
    print(f"Quantidade de limpezas: {limpezas:.2f}")
    print(f"Economia estimada: R$ {economia:.2f}")

    lista_limpezas = list(range(1, limpezas + 1))
    economias = []

    for limpeza in lista_limpezas:
        funcao = custo_limpeza * math.log(limpeza + 1)
        economias.append(funcao)

    gerar_grafico(lista_limpezas, economias, "Economia Acumulada por Limpeza", "Número de Limpezas", "Economia (R$)")

def solicitar_periodo():
    quantidade = []
    semanas = int(input("Digite quantas semanas: ")) 
    dias = int(input("Digite quantos dias na semana: "))
    quantidade.append(semanas)
    quantidade.append(dias)
    return quantidade


def mapear_consumo(quantidade):
    consumo = []
    semanas = quantidade[0]
    dias = quantidade[1]
    for i in range(semanas):
        valores = []
        print(f"Semana {i+1}:")
        for a in range (dias):
            valor_consumo = float(input(f"Digite o consumo para o dia {a+1}: "))
            valores.append(valor_consumo)
        consumo.append(valores)
    return consumo


def max_min_consumo(consumo):
    print(f"Valor total {consumo}")
    semanas = len(consumo)
    valores_max = []
    valores_min = []
    for i in range(semanas):
        dias = []
        dias = consumo[i]
        valores_max.append(max(dias))
        valores_min.append(min(dias))
    max_min = (max(valores_max),min(valores_min))
    return max_min  


def consumo_medio(consumo):
    semanas = len(consumo)
    soma_total = 0
    qnt_itens = 0
    for i in range(semanas):
        dias = []
        dias = consumo [i]
        soma_total += sum(dias)
        qnt_itens += len(dias) 
    resultado = soma_total / qnt_itens
    media = round(resultado, 2)
    return media        


def valores_abaixo_media(consumo,media):
    valores_abaixo = []
    semanas = len(consumo)
    for i in range(semanas):
        dias = []
        dias = consumo[i]
        qnt_dias = len(dias)
        for a in range (qnt_dias):
            valor = dias[a]
            if (valor < media):
                valores_abaixo.append(valor)
    return valores_abaixo


def main():
    pass
    quantidade = solicitar_periodo()
    consumo = mapear_consumo(quantidade)
    max_min = max_min_consumo(consumo)
    print(f"\nValor Maximo: {max_min[0]} Litros")
    print(f"Valor Minimo: {max_min[1]} Litros")
    media = consumo_medio(consumo)
    print(f"\nMédia de consumo: {media} Litros")
    valores_abaixo = valores_abaixo_media(consumo,media)
    print(f"Valores abaixo da media: {valores_abaixo} Litros")
    

# Não apagar as linhas abaixo.
if __name__ == '__main__':
    main()
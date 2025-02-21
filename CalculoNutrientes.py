def calcular_calorias():
    print("Calculadora de Valor Energético (kcal) para Hipercalóricos")
    print("Insira os dados dos ingredientes. Digite 'fim' como nome do ingrediente para terminar.")

    total_calorias = 0
    total_proteinas = 0
    total_carboidratos = 0
    peso_total = 0
    ingredientes = []

    while True:
        nome = input("Nome do ingrediente: ")
        if nome.lower() == "fim":
            break

        try:
            quantidade = float(input(f"Quantidade de {nome} (em gramas ou ml): "))
            calorias_por_unidade = float(input(f"Calorias por unidade (kcal por grama/ml) de {nome}: "))
            proteinas_por_unidade = float(input(f"Proteínas por unidade (g por grama/ml) de {nome}: "))
            carboidratos_por_unidade = float(input(f"Carboidratos por unidade (g por grama/ml) de {nome}: "))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            continue

        calorias_ingrediente = quantidade * calorias_por_unidade
        proteinas_ingrediente = quantidade * proteinas_por_unidade
        carbo_ingrediente = quantidade * carboidratos_por_unidade

        total_calorias += calorias_ingrediente
        total_proteinas += proteinas_ingrediente
        total_carboidratos += carbo_ingrediente
        peso_total += quantidade

        ingredientes.append((nome, quantidade, calorias_por_unidade, calorias_ingrediente, proteinas_por_unidade, proteinas_ingrediente, carboidratos_por_unidade, carbo_ingrediente))
        print(f"{nome} adicionado: {calorias_ingrediente:.2f} kcal, {proteinas_ingrediente:.2f}g proteínas, {carbo_ingrediente:.2f}g carboidratos.\n")

    print("\nResumo da Mistura:")
    for ing in ingredientes:
        print(f"{ing[0]}: {ing[1]}g/ml x {ing[2]} kcal/g = {ing[3]:.2f} kcal, "
              f"{ing[4]}g proteínas/g = {ing[5]:.2f}g, {ing[6]}g carboidratos/g = {ing[7]:.2f}g")

    print(f"\nPeso total da mistura: {peso_total:.2f} g/ml")
    print(f"Valor energético total: {total_calorias:.2f} kcal")
    print(f"Proteínas totais: {total_proteinas:.2f} g")
    print(f"Carboidratos totais: {total_carboidratos:.2f} g")

    if peso_total > 0:
        calorias_por_grama = total_calorias / peso_total
        proteinas_por_grama = total_proteinas / peso_total
        carboidratos_por_grama = total_carboidratos / peso_total

        print(f"\nValores por grama da mistura:")
        print(f"Calorias: {calorias_por_grama:.2f} kcal/g")
        print(f"Proteínas: {proteinas_por_grama:.2f} g/g")
        print(f"Carboidratos: {carboidratos_por_grama:.2f} g/g")

        quantidade_desejada = float(input("\nDigite a quantidade desejada (em gramas/ml) para calcular os valores nutricionais: "))
        calorias_desejadas = quantidade_desejada * calorias_por_grama
        proteinas_desejadas = quantidade_desejada * proteinas_por_grama
        carboidratos_desejados = quantidade_desejada * carboidratos_por_grama

        print(f"\nPara {quantidade_desejada}g/ml da mistura:")
        print(f"Calorias: {calorias_desejadas:.2f} kcal")
        print(f"Proteínas: {proteinas_desejadas:.2f} g")
        print(f"Carboidratos: {carboidratos_desejados:.2f} g")
    else:
        print("Peso total da mistura é zero. Não é possível calcular valores por grama.")

    print("\nObrigado por usar a calculadora!")

# Chama a função principal
calcular_calorias()


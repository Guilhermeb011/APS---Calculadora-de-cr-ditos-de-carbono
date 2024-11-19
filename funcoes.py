import openpyxl

def registrar_consumo(atividadeID, opcao_atividade):
    """Registra o consumo de diferentes atividades e calcula as emissões de CO2e."""
    if atividadeID == 1:  # Eletricidade
        fator = 0.5  # kg CO2e por kWh
        if opcao_atividade == 1:
            entradaQntd = 1092  # kWh por ano
        elif opcao_atividade == 2:
            entradaQntd = 1644
        elif opcao_atividade == 3:
            entradaQntd = 600
        elif opcao_atividade == 4:
            entradaQntd = 912
        elif opcao_atividade == 5:
            entradaQntd = 2184
        elif opcao_atividade == 6:
            entradaQntd = 1260
        else:
            print("Opção de eletricidade inválida.")
            return 0
        emissao = entradaQntd * fator
        atividade = "Eletricidade"
        
    elif atividadeID == 2:  # Combustível
        fator = 2.31  # kg CO2e por litro
        if opcao_atividade == 1:
            entradaQntd = 9600
        elif opcao_atividade == 2:
            entradaQntd = 10800
        elif opcao_atividade == 3:
            entradaQntd = 12000
        elif opcao_atividade == 4:
            entradaQntd = 15000
        else:
            print("Opção de combustível inválida.")
            return 0
        emissao = entradaQntd * fator
        atividade = "Combustível"
        
    elif atividadeID == 3:  # Viagem aérea
        fator = 0.115  # kg CO2e por km
        distancia = float(input("Digite a distância percorrida pelo voo (em km): "))
        passageiros = int(input("Digite o número de passageiros: "))
        entradaQntd = distancia
        emissao = entradaQntd * fator * passageiros
        atividade = "Viagem aérea"
    else:
        print("Atividade inválida.")
        return 0

    print(f"Consumo registrado: {entradaQntd} unidades de {atividade}. Emissão: {emissao:.2f} kg de CO2e")
    return emissao


def calcular_creditos(emissaoTotal):
    """Calcula os créditos de carbono e o custo para compensação."""
    precoPorCredito = 50  # Preço de 1 crédito de carbono
    quantidadeCred = emissaoTotal / 100  # 1 crédito = 100 kg CO2
    custoTotal = quantidadeCred * precoPorCredito  # Cálculo do custo total
    return quantidadeCred, custoTotal


def gerar_relatorio(usuarioNOME, emissaoTotal):
    """Gera um relatório em formato Excel com as emissões e os créditos de carbono."""
    quantidadeCred, custoTotal = calcular_creditos(emissaoTotal)

    # Criação de um novo arquivo Excel
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Relatório de Emissões"

    # Cabeçalho
    sheet["A1"] = "Relatório de Emissões de CO2"
    sheet["A2"] = f"Usuário: {usuarioNOME}"
    sheet["A4"] = "Emissões Totais de CO2 (kg)"
    sheet["B4"] = emissaoTotal
    sheet["A5"] = "Créditos de Carbono Necessários"
    sheet["B5"] = quantidadeCred
    sheet["A6"] = "Custo Total para Compensação (R$)"
    sheet["B6"] = custoTotal

    # Salvando o relatório em um arquivo Excel
    nome_arquivo = f"relatorio_{usuarioNOME}.xlsx"
    wb.save(nome_arquivo)
    print(f"Relatório gerado com sucesso! O arquivo está salvo como {nome_arquivo}")

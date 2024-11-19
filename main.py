from funcoes import registrar_consumo, calcular_creditos, gerar_relatorio

def main():
    emissaoTotal = 0
    verdadeiro = 1
    usuarioNOME = input("Digite o nome de usuário: ")

    while verdadeiro == 1:
        print("\n======Calculadora de Créditos de Carbono======")
        print("1. Registrar consumo")
        print("2. Calcular emissões")
        print("3. Créditos de carbono")
        print("4. Gerar relatório")
        print("5. Sair")
        opcao = int(input())

        if opcao == 1:
            print("\nAtividades disponíveis:")
            print("1. Eletricidade (Fator de emissão: 0.5 kg CO2e/unidade)")
            print("2. Combustível (Fator de emissão: 2.31 kg CO2e/unidade)")
            print("3. Viagem aérea (Fator de emissão: 0.115 kg CO2e/unidade)")
            atividadeID = int(input("Digite o ID da atividade: "))

            # Exibindo as opções de consumo baseadas na atividade
            if atividadeID == 1:  # Eletricidade
                print("Escolha uma opção de consumo:")
                print("1. Aparelhos eletrônicos (4 horas por dia)")
                print("2. Eletrodomésticos (24 horas por dia)")
                print("3. Iluminação (6 lâmpadas LED, 16h por dia)")
                print("4. Lavanderia e limpeza (1 hora 4x por semana)")
                print("5. Climatização (ar-condicionado, ventilador)")
                print("6. Chuveiro elétrico (30 minutos por dia)")
                
            elif atividadeID == 2:  # Combustível
                print("Escolha uma opção de consumo:")
                print("1. Necessidades diárias (9.600 km por ano)")
                print("2. Passeios (10.800 km por ano)")
                print("3. Viagens para cidades próximas (12.000 km por ano)")
                print("4. Ida e volta do trabalho (15.000 km por ano)")
                
            elif atividadeID == 3:  # Viagem aérea
                pass  # Não precisa de opções para viagens aéreas, pois a distância será inserida manualmente

            else:
                print("Atividade inválida.")
                continue
            
            opcao_atividade = int(input("Escolha a opção de consumo: "))
            emissao = registrar_consumo(atividadeID, opcao_atividade)
            emissaoTotal += emissao

        elif opcao == 2:
            print(f"Emissão total de CO2e para {usuarioNOME}: {emissaoTotal:.2f} kg")

        elif opcao == 3:
            quantidadeCred, custoTotal = calcular_creditos(emissaoTotal)
            print(f"Créditos de carbono necessários: {quantidadeCred:.2f} créditos")
            print(f"Custo total para compensação: R$ {custoTotal:.2f}")

        elif opcao == 4:
            gerar_relatorio(usuarioNOME, emissaoTotal)

        elif opcao == 5:
            verdadeiro = 0

    print("Fim do programa")

# Executando o programa
if __name__ == "__main__":
    main()

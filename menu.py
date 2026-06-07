from calculo import perda_exponencial_poeira, recuperacao_limpeza, economia_limpezas

def menu():
    while True:
        print("\n" + "-" * 50)
        print(" ADS - Adaptive Electrodynamic Shield ")
        print("-" * 50)
        print("1. Calcular perda de eficiência por poeira")
        print("2. Recuperação após limpeza")
        print("3. Economia acumulada com limpezas")
        print("0. Sair")
        print("-" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            perda_exponencial_poeira()

        elif opcao == "2":
            recuperacao_limpeza()

        elif opcao == "3":
            economia_limpezas()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")


if __name__ == "__main__":
    menu()
from chempy import balance_stoichiometry

def balancear_equacao_quimica(equacao_quimica):
    # Divide a equação nos lados esquerdo e direito
    lado_esquerdo, lado_direito = equacao_quimica.split("=")

    # Remove espaços em branco
    lado_esquerdo = lado_esquerdo.strip()
    lado_direito = lado_direito.strip()

    # Realiza o balanceamento
    reagentes, produtos = balance_stoichiometry({lado_esquerdo}, {lado_direito})

    return reagentes, produtos

if __name__ == "__main__":
    print("Bem-vindo ao balanceador de equações químicas!")
    
    while True:
        equacao_quimica = input("Digite a equação química (ou 'q' para sair): ")

        if equacao_quimica.lower() == 'q':
            break

        # Realiza o balanceamento
        reagentes, produtos = balancear_equacao_quimica(equacao_quimica)

        print("Reagentes balanceados:")
        for elemento, coeficiente in reagentes.items():
            print(f"{elemento}: {coeficiente}")

        print("Produtos balanceados:")
        for elemento, coeficiente in produtos.items():
            print(f"{elemento}: {coeficiente}")
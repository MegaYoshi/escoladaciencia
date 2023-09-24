from sympy import symbols, Eq, solve

def balance_chemical_equation(reactants, products):
    # Obter os símbolos para as variáveis
    variables = symbols(' '.join(set(''.join(reactants + products))))

    # Inicializar os coeficientes com 1
    coefficients = {v: 1 for v in variables}

    # Criar as equações para o balanceamento
    equations = []
    for r in reactants:
        equation = sum(coefficients[s] for s in r)
        equations.append(Eq(equation, 0))

    for p in products:
        equation = sum(coefficients[s] for s in p)
        equations.append(Eq(equation, 0))

    # Resolver o sistema de equações
    solutions = solve(equations, dict=True)

    # Obter os coeficientes
    coefficients = {v: solutions[0][v] for v in variables}

    return coefficients

# Equação química: CH4 + O2 -> CO2 + H2O
reactants = ['CH4', 'O2']
products = ['CO2', 'H2O']

coefficients = balance_chemical_equation(reactants, products)

# Mostrar os coeficientes
print('Coeficientes balanceados:')
for symbol, coefficient in coefficients.items():
    print(f'{symbol}: {coefficient}')

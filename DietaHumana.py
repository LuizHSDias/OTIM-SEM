from pulp import *

# Criação do problema
prob = LpProblem("Problema_Dieta_Humana", LpMinimize)

x = []

for i in range(1, 22):
    if i == 18:  # x18 = mamão
        x.append(LpVariable(f"x{i}", lowBound=0.5, upBound=1))
    else:
        x.append(LpVariable(f"x{i}", lowBound=1, upBound=1))

# lowBound=0.5 porque o artigo menciona que cada alimento
# deve ter no mínimo meia porção.

# Função objetivo (custos)
custos = [
    0.13, 0.15, 0.05, 0.93, 2.00,
    0.20, 0.56, 0.02, 0.04, 0.15,
    0.18, 0.46, 0.20, 1.15, 1.20,
    0.08, 0.13, 1.99, 0.20, 0.51,
    0.52
]

#Custos atuais
# custos = [
#     0.53,  # Chá (1 sachê de caixa com 10)
#     1.19,  # Pão francês (1 unidade)
#     0.21,  # Margarina (10 g de pote 500 g)
#     0.54,  # Melão (115 g)
#     2.50,  # Pêra (1 unidade)
#     0.64,  # Arroz (124 g de pacote 5 kg)
#     3.50,  # Carne (65 g)
#     0.10,  # Cenoura (8 g)
#     0.06,  # Pimentão (12 g)
#     0.51,  # Brócolis (39,7 g)
#     0.40,  # Tomate (45 g)
#     2.12,  # Abacaxi (1 fatia)
#     0.60,  # Laranjada (100 ml)
#     4.23,  # Iogurte (150 ml de pote 170 g)
#     2.43,  # Barra de cereais (1 unidade)
#     0.70,  # Alface (22 g)
#     1.52,  # Espinafre (66 g)
#     1.87,  # Mamão (110 g)
#     0.87,  # Suco de uva (150 ml)
#     1.20,  # Maçã (120 g)
#     1.39   # Frango (75 g)
# ]

prob += lpSum(custos[i] * x[i] for i in range(21)), "Custo_Total"

# Coeficientes de carboidratos
carb = [
    4.7, 14.3, 0.01, 8.2, 11.9,
    31.6, 0.31, 0.8, 0.8, 2,
    2, 16.1, 8.4, 10.9, 17.8,
    0.8, 2.4, 9.1, 22.6, 18.4,
    0.2
]

# Coeficientes de proteínas
prot = [
    0.14, 2.3, 0.01, 0.7, 0.3,
    2.8, 16.9, 0.08, 0.1, 1.1,
    0.3, 0.5, 0.4, 6.4, 3.2,
    0.3, 1.9, 0.6, 0.4, 0.2,
    22.2
]

# Coeficientes de lipídios
lip = [
    0, 0.05, 8.2, 0.5, 0.3,
    1.5, 9.1, 0.01, 0.02, 0.1,
    0.1, 0.5, 0.1, 2.1, 1.2,
    0.06, 0.2, 0.1, 0, 0.4,
    4.7
]

# Restrições de carboidratos
prob += lpSum(carb[i] * x[i] for i in range(21)) >= 150
prob += lpSum(carb[i] * x[i] for i in range(21)) <= 190

# Restrições de proteínas
prob += lpSum(prot[i] * x[i] for i in range(21)) >= 50
prob += lpSum(prot[i] * x[i] for i in range(21)) <= 70

# Restrições de lipídios
prob += lpSum(lip[i] * x[i] for i in range(21)) >= 25
prob += lpSum(lip[i] * x[i] for i in range(21)) <= 30

# Resolver
prob.solve()

# Resultados
print("Status:", LpStatus[prob.status])
print("Custo mínimo = R$", round(value(prob.objective), 2))

for v in prob.variables():
    print(v.name, "=", round(v.varValue, 4))
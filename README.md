# Modelagem Matemática Aplicada a Dietas Alimentares

## Descrição

Este projeto apresenta uma implementação em Python do problema de otimização de dietas alimentares descrito no artigo:

**ARAÚJO, Viviane Mariteli Bertuola Marques; SOUZA, Luciane de Fátima Rodrigues.**
*Modelagem Matemática aplicada a dietas alimentares e estudo da obesidade*. Revista Eletrônica de Educação e Ciência (REEC), v. 2, n. 1, p. 30–43, 2012.

O objetivo é reproduzir o modelo de Programação Linear utilizado pelos autores para minimizar o custo de uma dieta alimentar, respeitando restrições nutricionais de carboidratos, proteínas e lipídios.

---

## Ferramentas Utilizadas

* Python 3
* PuLP 3.3.1
* Solver CBC (integrado ao PuLP)

Instalação da biblioteca:

```bash
pip install pulp
```

---

## Modelagem

### Função Objetivo

Minimizar o custo total da dieta:

Min Z = Σ(ci · xi)

onde:

* xi = quantidade de cada alimento;
* ci = custo associado ao alimento.

### Restrições

O modelo considera:

* Carboidratos: 150 g ≤ CH ≤ 190 g
* Proteínas: 50 g ≤ Prot ≤ 70 g
* Lipídios: 25 g ≤ Lip ≤ 30 g

Além disso, foi incorporada a restrição descrita pelos autores de que cada alimento deve possuir pelo menos meia porção, evitando soluções em que determinados alimentos sejam eliminados da dieta.

---

## Execução

Execute o arquivo:

```bash
python dieta.py
```

---

## Saída Esperada

O programa exibe:

* Status da solução;
* Valor mínimo da função objetivo;
* Quantidade ótima de cada alimento.

Exemplo:

```text
Status: Optimal
Custo mínimo = R$ 9.85

x1 = 1.0
x2 = 1.0
...
x18 = 0.5
...
```

---

## Objetivo Acadêmico

Este código foi desenvolvido para fins educacionais na disciplina de Pesquisa Operacional, com o objetivo de:

* Reproduzir o modelo apresentado no artigo;
* Validar os resultados publicados;
* Demonstrar a aplicação da Programação Linear em problemas reais;
* Comparar a implementação em Python com a solução originalmente desenvolvida no software LINDO.

---

## Autores

João Carlos Ferreira Martins

Luiz Henrique Santos Dias

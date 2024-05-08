# Compreensão de Lista em Python

A compreensão de lista é uma construção poderosa em Python que permite criar novas listas de maneira concisa e eficiente. Ela é especialmente útil quando você precisa aplicar uma operação a cada elemento de uma lista existente e criar uma nova lista com os resultados.

## Exemplo Básico

Suponha que tenhamos uma lista de números e que desejamos criar uma nova lista contendo o quadrado de cada número da lista original.

Sem usar compreensão de lista, faríamos algo assim:

```python
numeros = [1, 2, 3, 4, 5]
quadrados = []

for numero in numeros:
    quadrado = numero ** 2
    quadrados.append(quadrado)

print(quadrados)

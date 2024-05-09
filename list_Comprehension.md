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
```

isso imprimirá:
```
[1, 4, 9, 16, 25]
```

Agora, usando compreensão de lista, podemos fazer isso de forma mais concisa:

```python

numeros = [1, 2, 3, 4, 5]
quadrados = [numero ** 2 for numero in numeros]

print(quadrados)
```

Isso também imprimirá:

```
[1, 4, 9, 16, 25]
```

Na linha **[numero ** 2 for numero in numeros]**, estamos utilizando a compreensão de lista. Ela cria uma nova lista contendo o quadrado de cada número na lista original numeros. Cada elemento da nova lista é definido como numero ** 2, onde numero é o valor atual na iteração sobre a lista numeros.


Essa explicação inclui uma introdução à compreensão de lista, um exemplo básico e uma comparação entre o uso de compreensão de lista e um loop tradicional.

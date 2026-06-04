#Pergunta 1

Nosso inventário apresenta reagentes com nomes repitidos, o que faria um dicionário criado ter a chave com o nome do reagente, mas a cada vez que encontrasse aquele nome da chave o valor seria sobrescrito sobre o valor anterior, ou seja, informações seriam perdidas.

#Pergunta 2 

o zip não cria uma lista de tuplas, na verdade ele cria um iterador chamado de zip object, se utilizasse um print direto no zip apareceria algo do tipo: <zip object at 0x...>

#pergunta 3 

o list comprehensions faz com que cada iteração do for seja um valor para aquela lista, logo não é necessário criar uma lista vazia e adicionar valores, pois cada iteração já adiciona o valor que eu quero desde que cumpra as condições estabelecidas

#Funcionamento

O programa recebe três listas (reagentes, lotes, purezas) onde cada indice seria um frasco no laboratório e suas informações. Utiliza-se o set() para tirar repetições e o len() para contar quantos reagentes únicos existem. A função zip une as 3 listas e o retorno do zip é transformado em uma lista de tuplas onde cada tupla são as informações de um frasco e passa essas informações pro usuário. Por fim, o único list comprehension usado percorre a lista de tuplas para mostrar quais lotes tem pureza acima ou igual a 98.0.
#Simulador TCG de monstros

##Explicação do Funcionamento

Esse programa simula o duelo entre dois monstros personalizáveis pelo usuário em um jogo baseado em turnos e em status dos monstros. O duelo só termina quando um dos monstros atinge 0 de vida. Nesse ponto o mostro que não atingiu 0 de vida é o ganhador. 

##Instruções de como rodar o script

Execute o código do "simulador_tcg.py" e forneca os dados requisitados no terminal sobre os monstros. Aproveite o duelo!

##Respostas às perguntas teóricas

###1

Um laço for tem número pré-definido de iterações, enquanto o while tem um número condicional de iterações, nesse caso o while foi a decisão correta pois não há como saber quantos turnos o combate vai durar durante a escrita do código.

###2

O return é a forma de pegar o resultado de uma função e guardar o valor fora dela, uma função tem o valor do seu retorno, que pode ser salvo em uma variável. Caso seja pedido o valor de uma função sem return definido, o eu valor é vazio "none".

###3

Um loop infinito é um laço que roda pra sempre, nunca encontra um operador de fluxo que o interrompa. Ele pode ser evitado principalmente com variáveis de controle, como usado com a vida no código do simulador, ou a partir de um contador que devem seguir um limite.
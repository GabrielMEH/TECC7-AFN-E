# TECC7-AFN-E
 Resolução de exercício do trabalho final de TECC7

Autômato Finito Não-determinístico com 
movimentos vazios (AFN-ε εε ε) 
O problema consiste em implementar um Autômato Finito Não-determinístico com movimentos 
vazios (AFN-ε) conforme a entrada indicada a seguir. O AFN-ε deve ler cada uma das cadeias 
indicadas e imprimir “Aceita” ou “Rejeita”, se ele aceita ou rejeita cada uma delas, respectivamente. 
Entrada 
A entrada consiste de diversas linhas. Na primeira linha, são apresentados os símbolos do alfabeto, 
separados por um espaço, sendo 5 o número máximo de símbolos. Na segunda linha, são 
apresentados os estados do autômato, também separados por um espaço, sendo 10 o número 
máximo de estados. A terceira linha contém um número inteiro N que representa a quantidade de 
transições. Nas próximas N (1 ≤ N ≤ 100) linhas, são apresentadas as transições no formato EI S EJ, 
de modo que, estando no estado EI e lendo o símbolo S (Obs.: se S for a string vazio, então trata-se 
de um movimento vazio, e não um símbolo.), chega-se ao estado EJ. Na linha seguinte, é 
apresentado o estado inicial (existe apenas um estado inicial). Em outra linha, são apresentados 
todos os estados finais, separados por um espaço, sendo 10 o número máximo de estados. A 
próxima linha contém um número inteiro C (1 ≤ C ≤ 10) que representa a quantidade de cadeias a 
serem testadas. Nas próximas C linhas, são apresentadas as cadeias a serem testadas. 
Saída 
Apresente, para cada cadeia, “Aceita” (sem aspas) se o autômato aceita a cadeia; ou “Rejeita” (sem 
aspas) se o autômato rejeita a cadeia.

exemplo entrada:
a b 
q0 q1 
3 
q0 a q0 
q0 vazio q1 
q1 b q1 
q0 
q1 
6 
aa 
bb 
ab 
ba 
aaaabbbb 
aaabbba 

exemplo saida: 
Aceita 
Aceita 
Aceita 
Rejeita 
Aceita 
Rejeita 
"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] (i- inicio | f - fim | p - passo)
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
linha = '-' * 10
print(variavel[4:])
print(variavel[:3])
print(f'{linha}')
print(variavel[0:2])
print(variavel[0:3])
print(f'{linha}')
print(len(variavel))
print(len(variavel[:3]))
print(len(variavel[4:]))
print(len(variavel[0:3]))
print(f'{linha}')
print(variavel[0:len(variavel):])
print(variavel[0:len(variavel):1]) # pula de 1 em 1 (normal)
print(variavel[0:len(variavel):2]) # pula de 2 em 2
print(f'{linha}')
print(variavel[::-1])
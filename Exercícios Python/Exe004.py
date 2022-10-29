#informações a respeito dessa var
palavra = input('Informe alguma palavra: ')
print(f'O tipo primitivo dessa var e: {type(palavra)}')
print(f'So tem espacos? {palavra.isspace()}')
print(f'E um numero? {palavra.isnumeric()}')
print(f'E alfabetico? {palavra.isalpha()}')
print(f'E alfabnumerico? {palavra.isalnum()}')

#vou diversas funções que verificam a natureza dessa var!
a = ['a', 'b', 'c', 'd', 'e', 'f']

print( a[ -5:-3 ] ) # Saída: ['b', 'c']
# Isto ocorre porque vai do indíce -5 (isto é [1]) até o limite do outro índice (mas sem imprimí-lo)

a = [ '1', '2', '3', '4', '5' ]
a.pop() # Remove a último elemento da pilha.
print(a)

a = [ 'a', 'b', 'c', 'd', 'e', 'f' ]
a.pop( 0 ) #remove 'a' que é o que está no índice [0]
print(a)
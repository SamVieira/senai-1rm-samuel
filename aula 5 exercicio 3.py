listanum = []
mai = 0
men = 0
for c in range(0, 3):
    listanum.append(int(input(f'Digite um Algoritmo {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'O maior Algoritmo e: {mai}')
print(f'O menor Algoritmo e: {men}')
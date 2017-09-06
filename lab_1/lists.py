lista = ["hello", 3.1415, True, None, 42]

print(lista)

lista_1 = [["cat", "bat"], [10, 20, 30, 40, 50]]

print(lista_1[0])
print(lista_1[0][1])
print(lista_1[1][4])

spam = ["cat", "bat", "rat", "elephant"]
print(spam[-1])

print("Ex. 1:", spam[0:3])
print("Ex. 2:", spam[0:4])
print("Ex. 3:", spam[0:])
print("Ex. 4:", spam[:])
print("Ex. 5:", spam[0:-1])
print("Ex. 6:", spam[:-1])

del spam[2]
print(spam)

spam_1 = [1, 2, 3]
spam_1 = 2 * spam_1
print(spam_1)

spam_1 = 3 * spam_1
print(spam_1)

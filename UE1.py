import numpy as np

print("----==== Programm Start====----")

x = np.sqrt(27 * 3)
y = 20 * 7

print("x={}, y={}".format(x, y))

print("----==== Programm Ende====-----")

print(type(x))
print(type(y))
del x, y
print("pi=%7.5f" % np.pi)

# 2.3
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x)
print("|")
satz= '"Python" ist eine tolle Programmiersprache'
print(satz)

print(satz.replace('"Python"','"C++"'))

print(satz)  #warum wir hier Python ausgegeben ?

print(satz.insert(10,'auch'))
print(satz)



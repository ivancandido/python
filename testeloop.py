#teste loop

num = 1
while num <= 10:
    print(str(num))
    num = num + 1

print("###########")

tabuada = int(input("qual a tabuada?"))
for valor in range(1, 11, 1):
    print(str(tabuada), " x ", valor, " = ", tabuada * valor)
# Напишите программу которая принимает на вход число N и выдает набор произведений чисел от 1 до N
n = int(input())
fact = 1
some_list = []
for i in range(2, n + 1):
    some_list.append(fact)
    fact *= i
some_list.append(fact)    
print(some_list)  
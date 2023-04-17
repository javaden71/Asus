num = int(input())      # вывести сумму цифр и произведение с текстом
d3 = num % 10
d1 = num // 10//10
d2 = (num // 10) %10

print('Сумма цифр =', d1 + d2 + d3)
print("Произведение цифр =", (d1 * d2) * d3)
print("Hello World!")

print("Введіть площу планети")
s=int(input())
print("Введіть площу першого типу лабораторій")
s1=int(input())
print("Введіть площу другого типу лабораторій")
s2=int(input())
print("Введіть площу третього типу лабораторій")
s3=int(input())
num1 = s // s1
num2 = (s - num1 * s1) // s2
num3 = (s - num1 * s1 -num2 * s2) // s3
print("Кількість лаборатлрій першого типу %s" %num1 )
print("Кількість лаборатлрій другого типу %s" %num2 )
print("Кількість лаборатлрій Третього типу %s" %num3 )
wil = s - num1 * s1 -num2 * s2 - num3 * s3
print("Вільного місця залишилося %s" %wil )
kil = num1 + num2 + num3
print("Кількість лабораторій %s" %kil )
pol = num1 * s1
print("Площа лабораторій першого типу %s" %pol )
pol2 = num2 * s2
print("Площа лабораторій другого типу %s" %pol2 )
pol3 = num3 * s3
print("Площа лабораторій третього типу %s" %pol3 )
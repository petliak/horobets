import random
print("Гра складаєтяся з 5 раундів")
print("в кожному раунді я загадую випадкове число від 1 до 5. Твоя задача його вгадати. Якщо ти вгадуєш число то отримуєш 2 бали, Якщо твоє число відрізняється від мого то ти отримуєш 1 бал")
chuslo = 0
for x in range(1,6):
    print("round %s" %x)
    n = int(input())
    r = random.randint(1, 5)
    print("загадане число %s" %r)
    if n == r:
        chuslo += 2
    elif n - r  == -1:
        chuslo += 1
    elif n - r == 1:
        chuslo += 1

    print("Твій рахунок %s" %chuslo)


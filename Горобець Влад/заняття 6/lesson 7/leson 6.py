import random
answer = ('ТАК','Ні','МОЖЛИВО','я скажу коли',)
data = {'log':'1','log1':'11','log2':'111','log3':'1111'}
while True:
    print("що потрібно зробити?")
    print("1-грати 2-додати акаунт 3-видалити акаунт")
    a = input()
    if a == "1":
        print("Введіть логін")
        login = input()
        print("Введіть parol")
        parrol = input()
        if data[login]==parrol:
            count = 0
            print("Ти хочеш зіграти?")
            choi = input()
            while choi == "da":
                print(answer[random.randint(0,3)])
                count = count + 1
                print("hochesh gratu she raz?")
                a = input()
                if a != "da" :
                    break
                if count == 2:
                    print("Кількість спрoб вичерпана")
                    break

    elif a == "2" :
        print("Введіть новий логін")
        now_log=input()
        print("Введіть новий пароль")
        now_znach = input()
        data[now_log]=now_znach
        print("Введіть логін")
        login = input()
        print("Введіть parol")
        parrol = input()
        if data[login] == parrol:
            count = 0
            print("Ти хочеш зіграти?")
            choi = input()
            while choi == "da":
                print(answer[random.randint(0, 3)])
                count = count + 1
                print("hochesh gratu she raz?")
                a = input()
                if a != "da":
                    d = False
                if count == 2:
                    print("Кількість спрoб вичерпана")
    elif a == "3":
        print("Введіть логін який хочеш видалити")
        star_log = input()
        del data[star_log]

    else:
        print("Введіть вірну інформацію")
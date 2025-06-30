print("Привіт, Скільки тобі років")
vik=int(input())
if (vik >=5) and (vik <= 52):
    print("Хочеш я вгадаю коли в тебе день народження?")
    a=input()

    if a == "Так" :
        print("Помнож на 2 число дня твого дня народження")
        print("Додай 5 до результату")
        print("Тепер помнож на 50")
        print("І додай номер місяця свого народження")
        print("яке число вийшло")
        s=int(input(""))
        s -= 250
        dete = s // 100
        mis = s - 100 * dete
        if  mis == 1:
            mis = "Січня"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 2:
            mis = "Лютого"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 3:
            mis = "Березня"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 4:
            mis = "Квітня"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 5:
            mis = "Травня"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 6:
            mis = "Червня"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 7:
            mis = "Липня"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 8:
            mis = "Серпня"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 9:
            mis = "Вересня"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 10:
            mis = "Жовтня"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 11:
            mis = "Листопада"
            print("Твій день нарадження %s %s" %(dete, mis))
        elif mis == 12:
            mis = "Грудня"
            print("Твій день нарадження %s %s" %(dete, mis))
        else:
            print("лох %s %s" %(dete, mis))

    else:
        print("добре, бувай")
else:
    print("гуляй лісом")



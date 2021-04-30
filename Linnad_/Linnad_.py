
def linnad(c):
    cs=[]
    civ=[]
    for i in range(c):
        cs.append(str(input("Название города: ")))
        civ.append(int(input("Кол-жителей: ")))
    q = cs.copy()
    q.sort()
    b = []
    for j in range(c):
        b.append(civ[cs.index(q[j])])
    
    while True:
        print("1 - Сколько жителей в городе")
        print("2 - Отсортировать")
        print("3 - Самый густонаселенный город")
        print("4 - Город, в котором жителей меньше чем n")
        print("5 - Среднее кол-во жителей")
        print("Чтобы выйти, вставьте что угодно")
        
        w = str(input("Ввод: "))
        if w == "1":
            Q(civ, cs)
            
        elif w == "2":
            W(c, cs, civ, b)
            
        elif w == "3":
            E(cs, civ)
            
        elif w == "4":
            R(c, cs, civ)
            
        elif w == "5":
            T(civ, cs)
            
        else:
            print("Выход")
            break
        

def Q(civ, cs):
    k = input("Навание города: ")
    print(k, ": ", civ[cs.index(k)])
    print()

def W(c, cs, civ, b):
    for f in range(c):
        print(cs[f], ": ", b[f])
    print()

def E(cs, civ):
    print(cs[civ.index(max(civ))])
    print()

def R(c, cs, civ):
    n = int(input("n = "))
    for i in range(c):
        if civ[i] <= n:
            print(cs[i])
    print()

def T(civ, cs):
    s=0
    for o in range(len(civ)):
        s += civ[o]
    print(round(s/len(civ), 2))
    print()
                
linnad(int(input("Кол-во городов: ")))
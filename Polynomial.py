from cmath import polar, rect
from math import pi,sin,cos,sqrt, trunc

def sign(x): 
    return -1 if x<0 else 1 if x else 0
def round(x,dp=5):
    ''' dp - кол-во десятичных знаков после запятой'''
    return trunc(0.5*sign(x)+x*10**dp)/10**dp
def nth_root(n,z):
    #  переход от декартова z в полярные координаты, ф. polar(z) возвращает 
    #  пару, которая записывается в r,phi соотвественно
    r, phi = polar(z)
    return [rect(r**(1/n), (phi+2*pi*k)/n) for k in range(n)]
def cube_root(z):
    '''возвращаем список из трех кубических корней'''
    return nth_root(3,z) 
def complex_trunc(z,dp=5):
    # 0.5 прибавляем для округления
    return round(z.real,dp) + 1j*round(z.imag,dp)
def square_root(z):
    return nth_root(2,z)
def complex_filter(z):
    return z.real if z.imag==0 else z  
    
print("Здравствуйте! Создаем новый полином. Введите коэффициенты для полинома:")
print("C₄x⁴+C₃x³+C₂x²+C₁x¹+C₀x⁰")
#C[x⁰,x¹x²x³,x⁴] 
# C=[0, 0, 0, 1, 1]
while True:
    try:
        C = list(map (int, input().split()))
        #*map разворачивает mapping-объект в его содержимое. 
        break
    except ValueError:
        print("Некорректный ввод.")
while C and C[-1] ==0:
    C.pop()
superscript="⁰¹²³⁴⁵⁶⁷⁸⁹"
def term(c,i): #представление одночлена со степенью i и коэф. с
    if i==0:
        return '%d' % c
    if i==1:
        if c!=1:
            return '%dx' % c
        return 'x'
    if c!=1: 
        return '%dx%s' % (c,superscript[i])
    return 'x%s' % superscript[i]
print("+".join([term(c,i) for i,c in reversed(list(enumerate(C))) if c]).replace("+-","-"))
# Выбор метода решения:
n=-1 #Степень тождественного нуля доопределяется значением -∞. Мы взяли -1 вместо -∞.
for index, value in enumerate(C): # i= индекс, c= значение
             if value!=0: n=index  # если находим ненулевой элемент, то присв-ем n индекс ненулевого элемента
if n==-1: #C=[0,0,0,0, 0]
    print("Любое вещественное число является корнем полинома.")
elif n==0: #(Константа) C=[1,0,0,0, 0] 
    # C=[3,0,0,0, 0]
    print("Полином не имеет корней.")
elif n==1: #(Линейный) C=[-4,2,0,0, 0] Корень полинома: 2.0
    # C=[9, 3,0,0,0] Корень полинома: -3.0
    print("Корень полинома:",-C[0]/C[1])
elif n==2: #(Квадратный)
         print("Находим корни по общей формуле: ")
         c, b, a = C[0], C[1], C[2]
         D = b**2 - 4*a*c
         if D < 0: print("Нет вещественных корней. (D<0)") #C=[6,2,3,0, 0] 
                                                        # C=[4, 5,3,0,0]
         elif D == 0: #C=[64,-16,1,0, 0] Корень двойной кратности 8.0
            #  C=[49, -14,1,0,0] Корень двойной кратности(D==0) 7.0
             x = -b / (2*a) 
             print("Корень двойной кратности. (D==0)", x)
         else:# C=[4,-6,2,0, 0] Первый корень равен: 2.0 Второй корень равен: 1.0
            #  C=[-54, -3,1,0,0] Первый корень равен: 9.0 Второй корень равен: -6.0
            x1 = (-b + sqrt((b**2) - 4*a*c)) / (2*a)
            x2 = (-b -sqrt((b**2) - 4*a*c)) / (2*a)
            print("Первый корень равен:",x1)
            print("Второй корень равен:",x2)   
elif n==3: #(Кубический)
    d,c,b,a=C[0],C[1],C[2],C[3]
    p=(3*a*c-b**2)/(3*a**2)
    q=(2*b**3-9*a*b*c+27*a**2*d)/(27*a**3)
    H= 108 * 27 * a**6
    Q=4*(3*a*c-b**2)**3+(2*b**3-9*a*b*c+27*a**2*d)**2
    Q=Q/H
    print("Q=",Q)
    if Q<0: #C=[-6, 11,-6,1,0] Корень 3.0 Корень 1.0 Корень 2.0
        # C=[-54, -57,-2,1,0] Корень 9.0 Корень -6.0 Корень -1.0
        #Для Q<0 sqrt(Q) заменяем на sqrt(-1(-Q))=i*sqrt(-Q)
        print("Q<0")
        alpha=cube_root(-q/2+1j*sqrt(-Q))
        beta=[-p/3/a for a in alpha]
        for A, B in zip(alpha,beta):#!!!!Отметка (1)
            print("Корень", complex_filter(complex_trunc(A+B-b/3/a)))   #A+B=y, x=y-b/3/a
    elif Q==0: 
        #  C=[49, 35,-13,1,0]Корень 7.0 Корень -1.0 Корень 7.0
        #C=[-4, 8,-5,1,0] Корень 2.0 Корень 1.0 Корень 2.0 
        print("Q==0")
        alpha=cube_root(-q/2)
        beta=[-p/3/a for a in alpha]
        for A, B in zip(alpha,beta):
            print("Корень", complex_filter(complex_trunc(A+B-b/3/a)))
    else: #Q>0 
        # C=[-4, 2,1,1,0] Корень 1.0 Корень (-1+1.73205j) Корень (-1-1.73205j)
        # C=[13, 7,-5,1,0] Корень (3-2j) Корень -1.0 Корень (3+2j)
        print("Q>0")
        alpha=cube_root(-q/2+sqrt(Q))
        beta=[-p/3/a for a in alpha]
        for A, B in zip(alpha,beta): 
            print("Корень", complex_filter(complex_trunc(A+B-b/3/a)))

elif n==4: #(Полином 4-ой степени)
    E,D,C,B,A=C[0],C[1],C[2],C[3],C[4]
    alpha=-3*B**2/(8*A**2)+C/A
    beta=B**3/(8*A**3)-B*C/(2*A**2)+D/A
    gamma=-3*B**4/(256*A**4)+B**2*C/(16*A**3)-B*D/(4*A**2)+E/A
    if beta==0:# C=[24, -50,35,-10,1] Корень 4.0 Корень 1.0 Корень 3.0 Корень 2.0
        # C=[1, 0, 2, 0, 1] Корень 1j Корень -1j Корень 1j Корень -1j
        print("beta==0",beta)
        x_roots=[-B/4*A+root1
            for root2 in square_root(alpha**2-4*gamma)
            for root1 in square_root((-alpha+root2)/2)]
        for x in x_roots:
            print("Корень", complex_filter(complex_trunc(x)))
    else: 
        P=-alpha**2/12-gamma
        Q=-alpha**3/108+alpha*gamma/3-beta**2/8
        R=-Q/2-square_root(Q**2/4+P**3/27)[0]
        U=cube_root(R)[0]
        if U==0: 
            # C= [0, 1, 0, 0, 1] Корень 1: (0.5-0.86603j) Корень 2: 0.0 Корень 3: (0.5+0.86603j) Корень 4: -1.0
            #  C=[0, 0, 0, 1, 1]
             print("U==0",U)
             y=-5*alpha/6+U-cube_root(Q)[0]
        else: #C=[-50, 25, 7, -7, 1] Корень 1: (2-1j)Корень 2: (2+1j) Корень 3: 5.0 Корень 4: -2.0
            #C=[-39, -14, 18, -6, 1] Корень 1: (2-3j) Корень 2: (2+3j) Корень 3: 3.0 Корень 4: -1.0
             print("U!=0")
             print("U==",U)
             y=-5*alpha/6+U-P/3/U
        x_roots=[-B/4/A+(root1+root2)/2
            for root1 in square_root(alpha+2*y)
            for root2 in square_root(-(3*alpha+2*y+2*beta/root1))]
        for index, x in enumerate(x_roots):
            print("Корень ",index+1,": ", complex_filter(complex_trunc(x)),sep="")

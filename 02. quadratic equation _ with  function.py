"""
Программа вычисления корней квадратных уравнений, построенная на максимальном использовании функций
"""
def hello_():
    print()
    print("Данная программа находит корни квадратного уравнения вида:")
    print("a∙x² + b∙x + c = 0")
    print("-" * 18)
    r = int(input("Округлить решение до знака после точки (от 1 до 10): "))
    return r

def koefficient():
    while True:
        a = float(input("Введите первый коэффициент а: "))
        if a == 0:
            print("Первый коэффициент не должен быть равен нулю!")
            continue
        else:
            break
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    ron_1 = ' + ' if b >= 0 else ' - '
    ron_2 = ' + ' if c >= 0 else ' - '
    print("Вид уравнения, для которого будут найдены корни:")
    print(f"{a}∙x²" + f"{ron_1}" + f"{abs(b)}∙x" + f"{ron_2}" + f"{abs(c)}" + " = 0")
    return (a, b, c)

def diskriminant(a, b, c):                         # Нахождение дискриминанта по коэффициентам
    dis_ = b ** 2 - 4 * a * c
    print("Дискриминант равен ", dis_)
    return dis_

def root_equation(d, a, b, c, r):
    if d == 0:
        x = -b / (2 * a) if b != 0 else abs(-b / (2 * a))       # Чтобы не получать значение "-0.0 ", т.е. ноль с минусом
        print("У данного уравнения один корень:")
        print("\tx = ", round(x, r))

    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print("У данного уравнения два вещественных корня:")
        print("\tx1 = ", round(x1, r))
        print("\tx2 = ", round(x2, r))
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print("У данного уравнения два комплексных корня:")
        print("\tx1 = ", round(x1.real, r) + round(x1.imag, r) * 1j)
        print("\tx2 = ", round(x2.real, r) + round(x2.imag, r) * 1j)

def start():
    round_ = hello_()
    print()
    k = koefficient()
    print()
    d = diskriminant(k[0], k[1], k[2])
    print()
    root_equation(d, k[0], k[1], k[2], round_)

start()
while True:
    print()
    print("Данная программа находит корни квадратного уравнения вида:")
    print("a∙x² + b∙x + c = 0")
    print("-" * 18)

    while True:
        try:
            round_ = int(input("Округлить решение до знака после точки (от 1 до 10): "))
            if 1 <= round_ <= 10:
                break
            else:
                print("Диапазон округления должен быть от 1 до 10 знаков после точки.")
                continue
        except:
            print("Вы ввели не число")
            continue
        else:
            break

    print("-" * 18)

    while True:
        try:
            a = float(input("Введите каэффициент a: "))
        except:
            print("Вы ввели не число")
        else:
            if a == 0:
                print("Первый коэффициент не может быть равен нулю!")
                continue
            break

    while True:
        try:
            b = float(input("Введите каэффициент b: "))
        except:
            print("Вы ввели не число")
        else:
            break
    while True:
        try:
            c = float(input("Введите каэффициент c: "))
        except:
            print("Вы ввели не число")
        else:
            break
    print("-" * 25)

    ron_1 = ' + ' if b >= 0 else ' - '
    ron_2 = ' + ' if c >= 0 else ' - '

    print("Вид уравнения, для которого будут найдены корни")
    print(f"{a}∙x²"+f"{ron_1}"+f"{abs(b)}∙x"+f"{ron_2}"+f"{abs(c)}"+" = 0")
    print("-" * 25)

    diskriminant = b ** 2 - 4 * a * c

    if diskriminant > 0:
        print(f"Дискриминант больше нуля и равен {round(diskriminant, round_)}")
        x1 = (-b + diskriminant ** 0.5) / (2 * a)
        x2 = (-b - diskriminant ** 0.5) / (2 * a)
        print("У данного уравнения два корня:")
        print("\tx1 = ", round(x1, round_))
        print("\tx2 = ", round(x2, round_))

    elif diskriminant == 0:
        print("Дискриминант равен нулю")
        x = -b / (2 * a) if b != 0 else abs(-b / (2 * a))        # Чтобы не получать значение "-0.0 ", т.е. ноль с минусом
        print("У данного уравнения один корень:")
        print("\tx = ", round(x, round_))
    else:
        print(f"Дискриминант меньше нуля и равен {diskriminant}")
        print("Уравнение имеет решение в комплексных числах.")
        x1 = (-b + diskriminant ** 0.5) / (2 * a)
        x2 = (-b - diskriminant ** 0.5) / (2 * a)
        print("У данного уравнения два комплексных корня:")
        print("\tx1 = ", round(x1.real, round_) + round(x1.imag, round_) * 1j)
        print("\tx2 = ", round(x2.real, round_) + round(x2.imag, round_) * 1j)
    print("-" * 25)

    while True:
        reload_ = str(input("Вычислить корни для другого уравнения - y/n: "))
        try:
            if reload_ == 'y' or reload_ == 'n':
                break
            else:
                raise Exception
        except:
            print('Введите "y" или "n"')
        continue
    if reload_ == 'n':
        break
    else:
        continue

print("Конец программы.")















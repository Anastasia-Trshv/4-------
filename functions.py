'''Функции из пунктов 1-8'''
def devide (a, b):
    '''Пункт 1. Делит два числа'''
    if b==0:
        raise ZeroDivisionError("Аргумент b не должен быть равен 0")
    else:
        return a/b

def multiply (a, b):
    '''Пункт 1. Умножает два числа'''
    if (type(a)==str or type(b)==str):
        raise TypeError
    else:
        return a*b


def calculate_area(length, width):
    '''Пункт 2. Возвращает площадь прямоугольника, если это возможно'''
    try:
        if length < 0 or width < 0:
            raise Exception("Длина и ширина прямоугольника должны быть положительными.")
        else:
            return length*width
    except Exception:
        print("Значения должны быть положительными")


def calculate_perimeter(length, width):
    '''Пункт 3. Возвращает перимтер прямоугольника, если это возможно'''
    try:
        if length < 0 or width < 0:
            raise Exception("Длина и ширина прямоугольника должны быть положительными.")
        else:
            return (length+width)*2
    except Exception:
        print("Значения должны быть положительными")
    finally:
        print("Функция завершила работу")

def return_symbol_by_number(string, number):
    '''Пункт 4. Возвращает символ строки по порядковому номеру '''
    try:
        if type(number)!=int:
            raise TypeError
        if len(string)<number:
            raise IndexError
        if number<=0:
            raise ValueError

        return string[number]
    except TypeError:
        print("Второй аргумен должен быть числом")
    except IndexError:
        print("Максимальный порядковый номер символа строки меньше искомого")
    except ValueError:
        print("Целевой индекс должен быть больше нуля")

def trapezoid_area(a, b, h):
    '''Пункт 4. Возвращает площадь трапеции '''
    try:
        if type(a)!=int or type(a)!=float:
            raise TypeError
        if (a, b, h)<=0:
            raise ValueError
        if a==b:
            raise Exception

        return 0,5*h*(a+b)
    except TypeError:
        print("Аргументы должны быть числом")
    except ValueError:
        print("Значения должны быть больше нуля")
    except Exception:
        print("Оба основания не могут быть равны.")

def triangle_permeter(a, b, c):
    '''Пункт 4 и 5. Возвращает периметр круга '''
    try:
        if type(a)!=int or type(a)!=float:
            raise TypeError
        if (a, b, c)<=0:
            raise ValueError
        if a> b+c or b>c+a or c> a+b:
            raise Exception

        return a+b+c
    except TypeError:
        print("Аргументы должны быть числом")
    except ValueError:
        print("Значения должны быть больше нуля")
    except Exception:
        print("Треугольник не существует")

class RetirementageException(Exception):
    '''Пункт 6. '''
    print("Человек не достиг пенсионного возраста (66 лет)")

class InvalidTriangleSidesException(Exception):
    '''Пункт 6.'''
    def __init__(self, sides):
        super().__init__(f"Стороны {sides} не могут составить треугольник, так как не соответствуют правилу существования треугольника.")


class TooShortPasswordException(Exception):
    '''Пункт 6.'''
    print("Пароль должен составлять не менее 10 символов")

def validate_password(password):
    '''Пункт 7. Функция проверяющая длину пароля '''
    try:
        if len(password)<= 10:
            raise TooShortPasswordException
        else:
            print("Пароль подходит")
    except TooShortPasswordException:
        print("Пароль должен составлять не менее 10 символов")

def retire_person(age, name):
    "Пункт 8. Оформление выхода сотрудника на пенсию"
    try:
        if age<66:
            raise RetirementageException
        else:
            print(f"{name} на пенсии")
    except RetirementageException:
        print("Человек не достиг пенсионного возраста")

def create_triangle(a, b, c):
    "Пункт 8. Симуляция создания треугольника"
    try:
        if a> b+c or b>c+a or c> a+b:
            raise InvalidTriangleSidesException((a,b,c))
        else:
            print("Треугольник создан")
    except InvalidTriangleSidesException:
        print(f"Стороны {a, b, c} не могут составлять треугольник")

def greeting(string):
    "Пункт 8. Печатает приветствие"
    try:
        if string !="Привет":
            raise ValueError
        else:
            print("И Вам здравствуйте!")
    except ValueError:
        print(f"Ожидалось приветствие")
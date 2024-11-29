if  __name__ == "__main__":
    import functions

    print("______________________________________________")
    try:
        print(functions.devide(4, 0))
    except ZeroDivisionError:
        print("Делитель не должен быть равен нулю")

    print("______________________________________________")
    try:
        print(functions.multiply(4, "h"))
    except TypeError:
        print("Ожидались числа")

    print("______________________________________________")
    print(functions.calculate_area(7, -8))
    print("______________________________________________")
    print(functions.calculate_perimeter(7, -7))
    print("______________________________________________")
    print(functions.return_symbol_by_number("солнце", 10))
    print("______________________________________________")
    print(functions.trapezoid_area(7,-8,4))
    print("______________________________________________")
    print(functions.triangle_permeter(3,4,9))
    print("______________________________________________")
    functions.validate_password("hjk")
    print("______________________________________________")
    functions.retire_person(7,"Igor" )
    print("______________________________________________")
    functions.create_triangle(10,7,1)
    print("______________________________________________")
    functions.greeting("Пока")
    print("______________________________________________")

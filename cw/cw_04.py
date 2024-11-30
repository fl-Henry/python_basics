def func():
    try:
        x = int(input("Введите число: "))
        result = 10 / x
    except ZeroDivisionError as e:
        print("Ошибка: деление на ноль!")
        raise
    except ValueError as e:
        print("Ошибка: введено не число!")
        raise

try:
    func()
except Exception as e:
    print(f"Ошибка была повторно выброшена: {e}")
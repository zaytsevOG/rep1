def main(input: str) -> str:
    try:
        parts = input.split()

        if len(parts) != 3:
            raise ValueError("Неверный формат ввода. Используйте формат: 'число операция число'")

        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])

        if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль")
            result = num1 // num2
        else:
            raise ValueError("Недопустимый оператор. Используйте +, -, * или /")

        return str(result)

    except ValueError as ve:
        raise ValueError(f"Ошибка ввода: {ve}")
    except ZeroDivisionError as zde:
        raise ZeroDivisionError(f"Ошибка деления: {zde}")
    except Exception as e:
        raise Exception(f"Неизвестная ошибка: {str(e)}")


if __name__ == "__main__":
    try:
        user_input = input("Введите выражение (формат: 'число операция число'): ")
        result = main(user_input)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Программа завершена с ошибкой: {str(e)}")

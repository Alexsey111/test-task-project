# Задача 1:
# Необходимо реализовать декоратор @strict
# Декоратор проверяет соответствие типов переданных в вызов функции аргументов типам аргументов, объявленным в прототипе функции.
# (подсказка: аннотации типов аргументов можно получить из атрибута объекта функции func.__annotations__ или с помощью модуля inspect)
# При несоответствии типов бросать исключение TypeError
# Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str
# Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию
#
# def strict(func):
#     ...
#
#
# @strict
# def sum_two(a: int, b: int) -> int:
#     return a + b
#
#
# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError


import inspect

def strict(func):
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            expected_type = sig.parameters[name].annotation
            if expected_type is not inspect.Parameter.empty and not isinstance(value, expected_type):
                raise TypeError(
                    f"Argument '{name}' must be of type {expected_type.__name__}, got {type(value).__name__} instead."
                )

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # ✅ 3

try:
    print(sum_two(1, 2.4))  # TypeError
except TypeError as e:
    print(f"Caught an error: {e}")

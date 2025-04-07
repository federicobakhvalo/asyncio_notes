import asyncio


async def my_coroutine() -> None:
    print('Hello world!')


async def test_() -> int:
    return 1


async def coroutine_add_one(number: int) -> int:
    print('Выполняю асинхронную функцию')
    return number + 1


def add_one(number: int) -> int:
    return number + 1


function_result = add_one(1)
coroutine_result = coroutine_add_one(1)
print(f'Результат функции равен {function_result}, а его тип равен {type(function_result)}')

print(f"Результат сопрограммы равен {coroutine_result}, а его тип равен {type(coroutine_result)}")

asyncio.run(coroutine_result)
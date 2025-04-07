import asyncio
from asyncio import Future


#"2.14"
my_future = Future()
print(f'my_future готов? {my_future.done()}')
my_future.set_result(42)
print(f'my_future готов? {my_future.done()}')
print(f'Какой результат хранится в my_future? {my_future.result()}')


#2.15

def make_req()->Future:
    future=Future()
    asyncio.create_task(set_future_value(future))
    return future




async def set_future_value(future : Future)->None:
    await asyncio.sleep(1)
    future.set_result(42)


async def main():
    future = make_req()
    print(f'Будущий объект готов? {future.done()}')
    value = await future
    print(f'Будущий объект готов? {future.done()}')
    print(value)

asyncio.run(main())
import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return 'Hello World!'


async def delay(delay_seconds:int)-> int :
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'Сон в течение {delay_seconds} с окончен ')
    return delay_seconds


async def main() -> None:
    message = await hello_world_message()
    print(message)


asyncio.run(main())

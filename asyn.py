import asyncio
from time import time

from classes import Fisher, result1


async def main():
    q = asyncio.Queue()
    t = time()
    # await asyncio.gather(Fisher('Иван').run(q), Fisher('Василий').run(q))
    await  asyncio.gather(*[Fisher(f'Рыбак {i}').run(q) for i in range(10)])
    a = await result1(q)
    print('\nВсего поймано рыб:')
    for key, value in a.items():
        print(f'{key:<12} - ', value)
    print(f"Время выполнения: {time() - t:.3f} сек.")


asyncio.run(main())
# result1(q)

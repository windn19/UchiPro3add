import asyncio
from random import randint, choice
from time import sleep
from queue import Queue


class Fisher:
    FISHES = ['подлещик', "окунь", "лещ", "сом", "верхоплавка", "карась", None]

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.cage = {}

    async def run(self, q: Queue):
        n = randint(1, 20)
        print(f'Рыбак {self.name} накопал {n} червей')
        for _ in range(n):
            print(f'Рыбак {self.name} закинул удочку')
            # sleep(0.5)
            await asyncio.sleep(0.5)
            fish = choice(self.FISHES)
            if fish:
                self.count += 1
                self.cage[fish] = self.cage.get(fish, 0) + 1
            else:
                print("Сорвалась!!!")
        print(f'Рыбак {self.name} пошел домой. Поймал {self.count} рыб')
        for key, value in self.cage.items():
            print(f'{key:<12} - ', value )
        # q.put(self.cage)
        await q.put(self.cage)


def result(q: Queue):
    res = {}
    # print(q.qsize())
    for _ in range(q.qsize()):
        for key, val in q.get().items():
            res[key] = res.get(key, 0) + val
    return res


async def result1(q: asyncio.Queue):
    res = {}
    # print(q.qsize())
    for _ in range(q.qsize()):
        # print(q._queue.pop())
        for key, val in q._queue.pop().items():
            res[key] = res.get(key, 0) + val
    return res


if __name__ == '__main__':
    f1 = Fisher('Иван')
    f1.run()

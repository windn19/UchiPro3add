import asyncio


async def ivan():
    print(" (1)  // Иван идет по дороге и тут светофор! надо подождать...")
    await asyncio.sleep(2)
    print(" (2) // Загорается зеленый свет для пешеходов и мы идем дальше")


async def car():
    print(" (3) // Машина начинает ехать")
    await asyncio.sleep(2)
    print(" (4) // Загорается красный для пешеходов и снова начинают ехать машины")


if __name__ == "__main__":
    event_l = asyncio.get_event_loop()
    tasks = [event_l.create_task(ivan()), event_l.create_task(car())]
    wait_tasks = asyncio.wait(tasks)
    event_l.run_until_complete(wait_tasks)
    event_l.close()

from time import time
from threading import Thread
from queue import Queue

from classes import Fisher, result


t = time()
q1 = Queue()
# thr1 = Thread(target=Fisher('Иван').run, args=(q1,))
# thr2 = Thread(target=Fisher('Василий').run, args=(q1,))
# thr1.start()
# thr2.start()
# thr1.join()
# thr2.join()
ths = [Thread(target=Fisher(f'Рыбак {i}').run, args=(q1,)) for i in range(10)]
for th in ths:
    th.start()
for th in ths:
    th.join()

print('Всего поймано рыб:')
for key, value in result(q1).items():
    print(f'{key:<12} - ', value)
print(f"Время выполнения: {time() - t:.3f} сек.")
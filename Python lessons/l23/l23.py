# import threading
# import time

# def task(name):
#     print(f"Старт{name}")
#     time.sleep(2)
#     print(f"Конец {name}")
#
# t1 = threading.Thread(target=task, args=("A",))
# t2 = threading.Thread(target=task, args=("B",))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

# def task_1(name,delay):
#     print(name)
#     time.sleep(delay)
#
# threads = []
# for i in range(10):
#     t = threading.Thread(target=task_1, args=(f"Поток {i + 1} ", 2))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()

# import asyncio

# async def task_2(name):
#     print(f"Старт {name}")
#     await asyncio.sleep(2)
#     print(f"Конец {name}")
#
# async def main():
#     await asyncio.gather(
#         task_2("A"),
#         task_2("B"),
#     )
#
# asyncio.run(main())

# async def task_3(name, delay):
#     print(f"Task {name} started.")
#     await asyncio.sleep(delay)
#
# async def main():
#     await asyncio.gather(
#         task_3(name="Task 1", delay=1),
#         task_3(name="Task 2", delay=7),
#         task_3(name="Task 3", delay=2),
#     )
#
# asyncio.run(main())

# def download_image():
#     time.sleep(1)
#
# threads = []
# start = time.time()
#
# for i in range(10):
#     t = threading.Thread(target=download_image)
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print("Время:", time.time() - start)

# import time
# from multiprocessing import Process
#
# def download_movie():
#     time.sleep(1)
#
# if __name__ == '__main__':
#     processes = []
#     start = time.time()
#
#     for _ in range(10):
#         p = Process(target=download_movie)
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     print("Время:", time.time() - start)

# import asyncio
#
# async def download_text():
#     await asyncio.sleep(1)
#
# async def main():
#     tasks = [download_text() for _ in range(10)]
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())
# print("Готово")
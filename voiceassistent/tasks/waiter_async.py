import asyncio 
import time

#Створеня асинхроної функції
async def cook_steak(table_number):
    print(f"Кухар отримав замовлення для столика{table_number}")
    #розумне очікування виконнаня задачі 
    await asyncio.sleep(3)
    print(f"Стейк для стола {table_number} готовий")
    #поверненя результату асихроної функції
    return f"Стейк для столика {table_number} готов"

async def serve_table(table_number):
    print(f"Офіціант підходить до стола {table_number}")
    print(f"Офіціант приймає замовлення {table_number}")
    print(f"Офіціант передає замовлення ")
    #створення задачи для нашого кухаря
    steak_task = asyncio.create_task(cook_steak(table_number))
    #очікування результату кухаря без зупиненя программи
    steak = await steak_task
    print(f"Офіціант отримав стейк {steak} і подає його столику {table_number}")
    print("-" * 30)

async def main():
    start_time = time.time()
    #створення списку задач для офіціанта
    tasks_list = [
        asyncio.create_task(serve_table(3)),
        asyncio.create_task(serve_table(2)),
        asyncio.create_task(serve_table(1))
    ]
    #збір всіх задач в одну 
    # * подрібно щоб роспакувати список задач 
    await asyncio.gather(*tasks_list)
    end_time = time.time()
    print(f"Загальний час: {end_time - start_time:.2f} секунд")

#запуск основної асинхроної функції
asyncio.run(main())
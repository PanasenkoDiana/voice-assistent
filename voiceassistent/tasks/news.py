import asyncio

async def news(name = str, time = int):
    print(f'Починаю завантаження з {name}.')
    await asyncio.sleep(time)
    print(f'Завантажено {name} за {time} секунд')
    return(f'Дані з {name}')


async def main():
    task_list = [
        asyncio.create_task(news('Гугл', 4)),
        asyncio.create_task(news('Гіт хаб', 3)),
    ]
    
    result = await asyncio.gather(*task_list)
    print('Отримані дані:', result)

asyncio.run(main())
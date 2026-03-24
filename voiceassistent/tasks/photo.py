import asyncio

async def resize_image(image_id):
    print(f"Зменшуємо фото {image_id}")
    await asyncio.sleep(1)
    return f"small {image_id}"

async def apply_filter(image_name):
    print(f"Накладаємо фільтр на {image_name}")
    await asyncio.sleep(1)
    return f"filtered {image_name}"

async def cloud_download(image_name):
    print(f"Завантажуємо {image_name} на сервер")
    await asyncio.sleep(1)
    print(f"Фото {image_name} доступно за посиланням")
    
async def process_user_upload(image_id):
    image_small = await resize_image(image_id)
    image_filtered = await apply_filter(image_small)
    await cloud_download(image_filtered)

async def main():
    print("Початок обробки фото")
    await asyncio.gather(
        process_user_upload("user1_photo.jpg"), 
        process_user_upload("user2_photo.jpg")
    )
    
asyncio.run(main())
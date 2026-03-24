import time

def serve_table(table_number):
    print(f"Офіціант підійшов до столу {table_number}")
    print(f"Офіціант приймає замовлення від столу {table_number}")
    print(f"ОФіціант йде на кухню готовати замовлення {table_number}")
    time.sleep(3)
    print(f"Стейк для столу {table_number} готовий")
    print(f"Офіціант подає стейк до столу {table_number}")
    print("-" * 30)

start_time = time.time()
serve_table(3)
serve_table(2)
serve_table(1)

end_time = time.time()
print(f"Загальний час: {end_time - start_time:.2f} секунд")

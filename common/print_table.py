# Функция для вывода таблицы в консоль
def print_table(records, table):
    if not records:
        print("Нет записей для отображения.")
        return

    # Получаем имена столбцов
    columns = table.columns.keys()
    # Печатаем имена столбцов
    print(" | ".join(columns))
    print("-" * (len(columns) * 12))

    # Печатаем строки таблицы
    for record in records:
        print(" | ".join(str(getattr(record, column)) for column in columns))
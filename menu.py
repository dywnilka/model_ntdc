import os
from datetime import datetime

from sqlalchemy import insert, func

from common.print_table import print_table
from init import SessionLocal, parts, devices, journal, part_type, operation, user, status, location


# Функция для очистки экрана
def clear_screen():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для MacOS и Linux
    else:
        os.system('clear')

# Основное меню
def main_menu():
    while True:
        clear_screen()
        print("Главное меню:")
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("0. Выход")
        choice = input("Выберите пункт: ")

        if choice == '1':
            clear_screen()
            records_menu()
        elif choice == '2':
            clear_screen()
            add_record_menu()
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

# Меню для работы с записями
def records_menu():
    while True:
        clear_screen()
        print("Меню записей:")
        print("1. Показать все записи")
        print("2. Найти запись")
        print("3. Вернуться в главное меню")
        choice = input("Выберите пункт: ")

        if choice == '1':
            clear_screen()
            show_all_records_menu()
        elif choice == '2':
            clear_screen()
            print("Найти запись")
            find_records_menu()
            input("Нажмите Enter для возврата...")
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

# Меню для добавления записи
def add_record_menu():
    while True:
        clear_screen()
        print("Меню добавления записи:")
        print("1. Добавить новую запись")
        print("2. Редактировать запись")
        print("3. Вернуться в главное меню")
        choice = input("Выберите пункт: ")

        if choice == '1':
            clear_screen()
            add_records_menu()
        elif choice == '2':
            clear_screen()
            update_records_menu()
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

def show_all_records_menu():
    while True:
        clear_screen()
        print("Выберите таблицу для показа всех записей:")
        print("1. Детали")
        print("2. Устройства")
        print("3. Журнал")
        print("4. Вернуться назад")
        choice = input("Выберите пункт: ")

        if choice == '1':
            clear_screen()
            with SessionLocal() as sess:
                 records = sess.query(parts).all()
            print_table(records, parts)

            input("\nНажмите Enter для возврата...")

        elif choice == '2':
            clear_screen()
            with SessionLocal() as sess:
                records = sess.query(devices).all()
            print_table(records, devices)
            input("\nНажмите Enter для возврата...")

        elif choice == '3':
            clear_screen()
            with SessionLocal() as sess:
                records = sess.query(journal).all()
            print_table(records, journal)
            input("\nНажмите Enter для возврата...")

        elif choice == '4':
            clear_screen()
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

def add_records_menu():
    while True:
        clear_screen()
        print("Выберите таблицу для добавления записи:")
        print("1. Детали")
        print("2. Устройства")
        print("3. Журнал")
        print("4. Вернуться назад")
        choice = input("Выберите пункт: ")

        if choice == '1':
            clear_screen()
            name = input("Введите имя: ")
            decimal_num = input("Введите десятичное число: ")
            desc = input("Введите описание: ")
            parent_id = int(input("Введите ID родителя: "))

            with SessionLocal() as sess:
                 records = sess.query(part_type).order_by(part_type.c.id).all()
            print_table(records, part_type)
            type_id = int(input("Введите ID типа: "))

            stmt = insert(parts).values(name=name, decimal_num=decimal_num, desc=desc, parent_id=parent_id, type_id=type_id)
            with SessionLocal() as sess:
                sess.execute(stmt)
                sess.commit()
            print("Запись добавлена")
            input("\nНажмите Enter для продолжения...")

        elif choice == '2':
            clear_screen()
            serial = input("Серийный номер: ")
            desc = input("Введите описание: ")
            part_id = int(input("Введите ID детали: "))

            stmt = insert(devices).values(serial=serial, desc=desc, part_id=part_id)
            with SessionLocal() as sess:
                sess.execute(stmt)
                sess.commit()
            print("Запись добавлена")
            input("\nНажмите Enter для продолжения...")

        elif choice == '3':
            clear_screen()

            with SessionLocal() as sess:
                records = sess.query(devices).order_by(devices.c.id).all()
            print_table(records, devices)
            device_id = int(input("Введите ID устройства: "))
            with SessionLocal() as sess:
                records = sess.query(operation).order_by(operation.c.id).all()
            print_table(records, operation)
            operation_id = int(input("Введите ID операции: "))
            desc = input("Введите описание: ")
            result = input("Введите результат: ")
            with SessionLocal() as sess:
                records = sess.query(user).order_by(user.c.id).all()
            print_table(records, user)
            user_id = int(input("Введите ID пользователя: "))
            with SessionLocal() as sess:
                records = sess.query(status).order_by(status.c.id).all()
            print_table(records, status)
            status_id = int(input("Введите ID статуса: "))
            dttm = func.now()
            with SessionLocal() as sess:
                records = sess.query(location).order_by(location.c.id).all()
            print_table(records, location)
            location_id = int(input("Введите ID локации: "))

            stmt = insert(journal).values(device_id=device_id, operation_id=operation_id, description=desc, result=result,
                                          user_id=user_id, status_id=status_id, dttm=dttm, location_id=location_id)
            with SessionLocal() as sess:
                sess.execute(stmt)
                sess.commit()
            print("Запись добавлена")
            input("\nНажмите Enter для продолжения...")

        elif choice == '4':
            clear_screen()
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

def find_records_menu():
    while True:
        clear_screen()
        print("Выберите таблицу для поиска записи:")
        print("1. Детали")
        print("2. Устройства")
        print("3. Журнал")
        print("4. Вернуться назад")
        choice = input("Выберите пункт: ")

        if choice == '1':
            clear_screen()
            print("Выберите поле для поиска записи:")
            print("1. ID")
            print("2. Серийный номер")
            choice = input("Выберите пункт: ")

            if choice == '1':
                record_id = int(input("Введите ID записи: "))
                with SessionLocal() as sess:
                     records = sess.query(parts).filter(parts.c.id==record_id).all()
                print_table(records, parts)

                input("\nНажмите Enter для возврата...")

            elif choice == '2':
                record_decimal_num = input("Введите Десятичное число: ")
                with SessionLocal() as sess:
                    records = sess.query(parts).filter(parts.c.decimal_num == record_decimal_num).all()
                print_table(records, parts)

                input("\nНажмите Enter для возврата...")

        elif choice == '2':
            clear_screen()
            print("Выберите поле для поиска записи:")
            print("1. ID")
            print("2. Серийный номер")
            choice = input("Выберите пункт: ")

            if choice == '1':
                record_id = int(input("Введите ID записи: "))
                with SessionLocal() as sess:
                    records = sess.query(devices).filter(devices.c.id == record_id).all()
                print_table(records, devices)

                input("\nНажмите Enter для возврата...")

            elif choice == '2':
                record_serial = input("Введите Серийный номер: ")
                with SessionLocal() as sess:
                    records = sess.query(devices).filter(devices.c.serial == record_serial).all()
                print_table(records, devices)

                input("\nНажмите Enter для возврата...")

        elif choice == '3':
            clear_screen()

            record_id = int(input("Введите ID записи: "))
            with SessionLocal() as sess:
                records = sess.query(devices).filter(devices.c.id == record_id).all
            print_table(records, devices)

            input("\nНажмите Enter для возврата...")

        elif choice == '4':
            clear_screen()
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

def update_records_menu():
    while True:
        clear_screen()
        print("Выберите таблицу для добавления записи:")
        print("1. Детали")
        print("2. Устройства")
        print("3. Журнал")
        print("4. Вернуться назад")
        choice = input("Выберите пункт: ")

        if choice == '1':
            clear_screen()
            record_id = int(input("Введите ID записи: "))

            try:
                # Открываем сессию и находим запись по ID
                with SessionLocal() as sess:
                    record = sess.query(parts).filter(parts.c.id == record_id).first()
                    if not record:
                        print(f"Запись с ID={record_id} не найдена.")
                        return False

                    new_name = input("Введите имя: ")
                    new_decimal_num = input("Введите десятичное число: ")
                    new_desc = input("Введите описание: ")
                    new_parent_id = int(input("Введите ID родителя: "))

                    records = sess.query(part_type).all()
                    print_table(records, part_type)
                    new_type_id = int(input("Введите ID типа: "))

                    update_stmt = (
                        parts.update()
                        .where(parts.c.id == record_id)
                        .values(name=new_name, decimal_num=new_decimal_num, desc=new_desc, parent_id=new_parent_id,
                                type_id=new_type_id)
                    )

                    # Сохраняем изменения
                    sess.execute(update_stmt)
                    sess.commit()
                    print("Запись обновлена")


            except Exception as e:
                print(f"An error occurred: {e}")
                return False

            input("\nНажмите Enter для продолжения...")

        elif choice == '2':
            clear_screen()
            serial = input("Серийный номер: ")
            desc = input("Введите описание: ")
            part_id = int(input("Введите ID детали: "))

            stmt = insert(devices).values(serial=serial, desc=desc, part_id=part_id)
            with SessionLocal() as sess:
                sess.execute(stmt)
                sess.commit()
            print("Запись добавлена")
            input("\nНажмите Enter для продолжения...")

        elif choice == '3':
            clear_screen()

            with SessionLocal() as sess:
                records = sess.query(devices).all()
            print_table(records, devices)
            device_id = int(input("Введите ID устройства: "))
            with SessionLocal() as sess:
                records = sess.query(operation).all()
            print_table(records, operation)
            operation_id = int(input("Введите ID операции: "))
            desc = input("Введите описание: ")
            result = input("Введите результат: ")
            with SessionLocal() as sess:
                records = sess.query(user).all()
            print_table(records, user)
            user_id = int(input("Введите ID пользователя: "))
            with SessionLocal() as sess:
                records = sess.query(status).all()
            print_table(records, status)
            status_id = int(input("Введите ID статуса: "))
            dttm = func.now()
            with SessionLocal() as sess:
                records = sess.query(location).all()
            print_table(records, location)
            location_id = int(input("Введите ID локации: "))

            stmt = insert(journal).values(device_id=device_id, operation_id=operation_id, description=desc,
                                          result=result,
                                          user_id=user_id, status_id=status_id, dttm=dttm, location_id=location_id)
            with SessionLocal() as sess:
                sess.execute(stmt)
                sess.commit()
            print("Запись добавлена")
            input("\nНажмите Enter для продолжения...")

        elif choice == '4':
            clear_screen()
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main_menu()

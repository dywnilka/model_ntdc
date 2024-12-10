# Функция для получения записей из таблицы
def get_records(session, table):
    return session.query(table).all()
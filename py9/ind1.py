#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


if __name__ == '__main__':
    # Список работников.
    workers = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            name = input("Фамилия и имя: ")
            tel = input("Номер телефона: ")
            dateString = input("День рождения: ")
            # Создать словарь.
            worker = {
                'name': name,
                'tel': tel,
                'date': datetime.strptime(dateString, "%Y-%m-%d")
            }
            # Добавить словарь в список.
            workers.append(worker)
            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 16
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^16} |'.format(
                    "No",
                    "Ф.И.",
                    "Телефон",
                    "Дата рождения"
                )
            )
            print(line)
            # Вывести данные о всех сотрудниках.
            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>16} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('tel', ''),
                        worker.get('date', 0)
                    )
                )
            print(line)

        elif command.startswith('select '):
            # Разбить команду на части для выделения номера года.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый стаж.
            period = int(parts[1])
            # Инициализировать счетчик.
            count = 0
            # Проверить сведения работников из списка.
            for worker in workers:
                if worker['date'].month == period:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, worker.get('name', ''))
                    )
            # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("В этом месяце ни у одного из работников нет дня рождения.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <месяц> - месяц рождения работника;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

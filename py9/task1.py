#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    school = {
        "1А": 30,
        "1Б": 26,
        "2А": 21,
        "2Б": 32,
        "3А": 28,
        "3Б": 19,
    }

    for key, value in school.items():
        print(f" В {key} классе количество детей = {value}.")

    # Часть а)
    print("\nВ одном из классов поменялось количество детей, теперь:\n")
    school['2Б'] = 16
    for key, value in school.items():
        print(f" В {key} классе количество детей = {value}.")

    # Часть б)
    print("\nПоявился новый класс, теперь:\n")
    school.setdefault("3В", 31)
    for key, value in school.items():
        print(f" В {key} классе количество детей = {value}.")

    # Часть с)
    print("\nРасформировали один класс, теперь:\n")
    school.pop("1А")
    for key, value in school.items():
        print(f" В {key} классе количество детей = {value}.")

    count = 0
    for value in school.values():
        count += value
    print(f"\nВсего учеников в школе - {count}")

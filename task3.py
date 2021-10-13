# variant 25

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    word = input("Введите слово из 12 символов: ")
    if len(word) != 12:
        print(
            "Длина слова должна быть равна 12",
            file=sys.stderr
        )
        exit(1)
    n = len(word)
    word = word[n // 2: n][::-1] + word[0: n // 2][::-1]
    print(f"Слово после изменений: {word}")

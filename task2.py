# variant 25

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    word = input("Введите слово четной длины: ")
    if len(word) % 2 != 0:
        print(
            "Слово должно быть четной длины",
            file=sys.stderr
        )
        exit(1)
    n = len(word)
    word = word[n // 2: n][::-1] + word[0: n // 2][::-1]
    print(f"Слово после изменений: {word}")

# variant 25

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input("Введите предложение: ")
    sentence = sentence.replace(',', '')
    sentence = sentence.replace('.', '')
    sentence = sentence.replace('!', '')
    sentence = sentence.replace('?', '')
    words = sentence.lower().split(' ')
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                print(f"Одинаковые слова: {words[i]}")
                exit(1)
    print("Нет одинаковых слов")

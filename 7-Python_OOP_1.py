#!/usr/bin/env python3

wordlist = ['hello', 'world', 'python', 'is', 'awesome', '123']

# طباعة جميع الكلمات
for word in wordlist:
    print(word)

# البحث عن العنصر '123'
for word in wordlist:
    if word == '123':  # استخدم المطابقة المباشرة بدلاً من "in"
        print('123')

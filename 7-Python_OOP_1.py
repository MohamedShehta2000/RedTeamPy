#!/usr/bin/env python3
# الدالة الأولى تأخذ قيمتين ثابتتين وتعيد مجموعهما
wordlist = ['hello', 'world', 'python', 'is', 'awesome', '123']

# طباعة جميع الكلمات
for word in wordlist:
    print(word)

# البحث عن العنصر '123'
for word in wordlist:
    if word == '123':  # استخدم المطابقة المباشرة بدلاً من "in"
        print('123')


def sum():
    x = 3
    y = 4
    return x + y
new = sum()
print(new)

# الدالة الثانية تأخذ قيمة واحدة وتعيد مجموعها مع قيمة ثابتة
def sum(x):
    y = 4
    return x + y
new = sum(100)
print(new)

# الدالة الثالثة تأخذ قيمتين وتعيد جملة تحتوي على القيمتين ومجموعهما
def sum(x, y):
    word = f"the sum of {x} and {y} is {x + y}"
    return word
new = sum(100, 200)
print(new)

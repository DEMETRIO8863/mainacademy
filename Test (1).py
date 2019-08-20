#!/usr/bin/env python
# coding: utf-8

# # Практичні завдання

# ## Завдання 1
# 
# Створити список з 10 елементів типу `int` від 1 до 10.
# 
# Знайти:
# - суму всіх чисел
# - добуток всіх чисел
# - добуток тільки парних чисел
# - сформувати новий список, кожний елемент якого це квадрат числа кожного елементу з вихідного списку
# 
# Результати роботи записувати в змінну `result` типу `dict`, де ключ - це номер завдання, а значення - результат

# In[68]:


# task 1
new_dict = {}
numList = int()
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,2,3,4,5,6,7,8,9,10]))
new_dict['task1'] = listsum([1,2,3,4,5,6,7,8,9,10])
print(new_dict)


# In[69]:


# task 2

lst = [1,2,3,4,5,6,7,8,9,10]
def dobutok(lst):
    theDob = 1
    for i in lst:
        theDob = theDob * i
    return theDob
print(dobutok(lst))
new_dict['task2'] = (dobutok(lst))
print(new_dict)


# In[72]:


# task 3
from functools import reduce
 
lst = [1,2,3,4,5,6,7,8,9,10]
nimb = (reduce(lambda x, y: x * y, lst[::2]))
 
print(nimb)

new_dict['task3'] = (reduce(lambda x, y: x * y, lst[::2]))
print(new_dict)


# In[73]:


# task 4
new_list = [1,2,3,4,5,6,7,8,9,10]
a = (list(map(lambda x: x**2, new_list)))
print(a)
new_dict['task4'] = a
print(new_dict)


# ## Завдання 2
# Створити список з 20 елементів типу `int` від 1 до 20.
# 
# Знайти:
# - розбити список на два списки: парні та непарні числа; результата записати до словника з двома ключами під парні і непарні числа;
# - кожне парне число піднести до степені, де степінь - це кожне непарне число; результат записати до словника, де ключ це рядок "a ** b", а значення - це результат піднесення до степені;
# - розділити список на два, однакових за довжиною; по кожному списку створити новий, в якому всі двозначні числа розділені на цифри, наприклад, 13 - це 1 і 3;
# - на основі отриманих списків з попереднього кроку, створити два set, над якими провести операції union, intersection, difference, symmetric_difference, а результати записати до словника, де ключ - це тип операції, а значення - отриманий результат.

# In[48]:


# task 1
n_dict = {}
N_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list1 = [N_list[::2]]
list2 = [N_list[1::2]]
print(list1, list2)
n_dict['neparni'] = list1
n_dict['parni'] = list2
print(n_dict)


# In[ ]:





# In[91]:


# task 2
lst = []
for i in range(1,21):
    if i % 2 == 0:
        for j in range(1,21):
            if j % 2 != 0:
                sp = i**j
                lst.append(sp)

print(lst)
my_dict = {} 
for i in range(0, len(lst),1):
    my_dict['a**b'] = lst[i]  
    print(my_dict)


# In[78]:


# task 3
N_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lst1 = N_list[:len(N_list)//2]
lst2 = N_list[len(N_list)//2:]
print(lst1, lst2)
bad = []
def rozriz(listsort):
    laset = []
    for a in listsort:
        laset.extend(list(str(a)))
    return laset
new_lst1 = rozriz(lst1)
new_lst2 = rozriz(lst2)
print(new_lst1)
print(new_lst2)
    


# In[81]:


# task 4
set1 = set(new_lst1)
set2 = set(new_lst2)

print(set1, set2)

task4rezult = {
    'union': set1.union(set2),
    'intersection': set1.intersection(set2),
    'difference': set1.difference(set2),
    'symetric_difference':set1.symmetric_difference(set2)
}
print(task4rezult)


# ## Завдання 3

# **1. Напишіть програму, яка буде визначати, чи є номер телефону "крутим".**
# 
# "Крутий" номер - це випадки, коли:
#     
# - у номері підряд йдуть 4 і більше однакових цифри;
# - у номері підряд йдуть 4 і більше цифри у порядку спадання чи зростання;
# - сума перших 5 цифр номеру дорівнює сумі 5 останніх.
# 
# Приклади "крутих" номерів:
# 
# 1. 0981177770 (випадок 1)
# 2. 0951234567 (випадок 2)
# 3. 0670171123 (випадок 3)
# 
# Програма бере на вхід строку з номером із 10 знаків. На вихід друкує або "Крутий", або "Звичайний"

# In[80]:


a = 981177770
x = [int(i) for i in str(a)]
print(x)
for j in range(len(x)-3):
    if len(set(x[j:j+4])) == 1:
        print('Ok')
        break
for j in range(len(x)-3):
    if (x[j:j+4] == sorted(x[j:j+4]) or x[j:j+4] == sorted(x[j:j+4], reverse = True)) and len(set(x[j:j+4])):
        print((x[j:j+4]),sorted(x[j:j+4]))
        break
if sum(x[:len(x)//2]) == sum(x[int(len(x)//2):]):
    print('okok')


# ## Завдання 4

# **2. Напишіть програму, яка буде видавати з масиву локацій координати найближчої точки до центру.**
# 
# Перший ввід - координати широт.
# Другий ввід - координати довгот.
# 
# Кожне нове значення розділяйте пробілом.
# 
# Вивід - tuple з координатами довготи і широти, які найближчі до центру локацій.
# 
# Центр локацій - це середнє арифметичне введених координат довгот і широт.
# 
# Для простоти відстань міряємо в евклідовій метриці.
# 
# Всі розрахунки потрібно зробити без підключення додаткових модулів.
# 
# Приклад
# 
# Вхід:
# 
# 23 34 45
# 
# 88 99 77
# 
# Вивід:
# 
# (23, 88)

# In[85]:


from math import sqrt
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
distance = (sqrt((x1+x2)**2 + (y1+y2)**2))
print(distance)


# ## Завдання 5

# - знайти кількість букв в тексті в розрізі: всього, верхній регістр, нижній регістр; результат записати до dict з ключами total, upper, lower.
# - знайти кількість по кожній букві в тексті; результат записати в list, де кожний елемент - це tuple(letter, count);
# - сформувати list на основі list з п.2, в якому елементи відсортовані по кількості букв (від найменшої до найбільшої кількості);
# - знайти загальну кількість слів в тексті, результат записати як int;
# - знайти кількість чисел в тексті, результат записати як int;
# - створити dict, де ключ - це довжина слова, а значення - це кількість слів з такою довжиною;
# - знайти відсоток речень, в яких зустрічається слово Python; результат записати як float (на 100 не множимо).
# - знайти кількість спеціальних символів в тексті; результат записати до dict, де ключ - це спеціальний символ, а значення - кількість;
# - створити list, в якому речення відсортовані по кількості букв в верхньому регістрі;
# - знайти букву, яка зустрічається найчастіше і найрідше; результат записати як tuple(max, min);
# - знайти всі числа та записати їх до list, відсортувавши від найбільного до найменшого;
# - знайти мінімальне і максимальне число; результат записати як tuple(min, max);
# - знайти абзац, в якому Python зустрічається найчастіше; результат записати як str.
# - створити dict, де ключ - це слово, а значення - кількість разів, з якою слово зустрічається в тексті;
# - знайти слово, яке зустрічається найчастіше і найрідше; результат записати як tuple(tuple(word, count), tuple(word, count)).

# Для кожного пункту постановки реалізувати окрему функцію з наступною сигнатурою:
# 
#     def task_N(text, result):
#         # body
#         return local_result
# де, text - це вхідний текст, а result - це результат з попередніх завдань.
# 
# Дозволяється використовувати результати попередніх функції, але не змінювати значення result).
# 
# Створити dict, де ключ - це номер завдання типу int, а значення - це функція.
# 
#     handlers = {
#         N: task_N
#     }
# Створити функцію def analyze_text(text), яка:
# 
# - на вхід приймає text - вихідний текст;
# - містить в собі змінну result типу dict, де:
# - ключ - це номер завдання типу int;
# - значення - це результат завдання.
# - проходиться по handlers, викликає потрібну функцію, і записує результат до result;
# - в кінці повертає змінну result.
# 
# Для даного завдання погоджуємо, що:
# 
# - буква - букви латинці, без цифр, яка представлена одним символом;
# - цифра - це цифра, яка представлена одним символом;
# - число - це набір цифр, які йдуть разом;
# - спеціальний символ - це все те, що не буква, і не цифра, наприклад, крапка, кома, лапки, дужки і т.д.;
# - слово - від 1 до N символів (букви, цифри), які йдуть разом (спеціальні символи не вважаються словами);
# - речення - все, що до крапки.

# In[93]:


initial_text = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27] In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.[28][29]

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[30]

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[31] and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation.

Python was conceived in the late 1980s[32] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL)[33], capable of exception handling and interfacing with the Amoeba operating system.[7] Its implementation began in December 1989.[34] Van Rossum's long influence on Python is reflected in the title given to him by the Python community: Benevolent Dictator For Life (BDFL) – a post from which he gave himself permanent vacation on July 12, 2018.[35]"""


# In[101]:





# In[ ]:





# ## Завдання 6

# Это простое упражнение на использование функции как аргумента.
# 
# Если вы не использовали раньше сортировку по заданному ключу при помощи встроенной функции sorted, рекомендую прочитать вот этот python-howto (упражнение про это, да и вообще возможность чрезвычайно полезная).
# 
# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не больше 19).
# 
# Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке.
# 
# Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в словаре встречается позже слова three, а слово three -- позже слова one (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)
# 
# Наприклад
# 
# Вхід: 0 1 1 2 3 5 8 13
# 
# Вихід: 8 5 1 1 13 3 2 0

# In[2]:


number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}


# ## Завдання 7

# Это упражнение на написание декоратора.
# 
# Напишите декоратор flip, который делает так, что задекорированная функция принимает все свои неименованные аргументы в порядке, обратном тому, в котором их передали (для аргументов с именем не вполне правильно учитывать порядок, в котором они были переданы)

# In[1]:


#@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

    
#div(2, 4, show=True) #return 2


# In[ ]:





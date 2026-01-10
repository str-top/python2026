Вопросы с выбором варианта: 15/39%  
#  Вопрос 1. Замыкания (closures)
  
Проанализируйте временную и пространственную сложность замыканий. Объясните, когда они могут потреблять много памяти и почему.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multipliers = [make_multiplier(i) for i in range(1000000)]
```
  
### Ответ
asdfad  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 2. Аргументы функции
  
Проанализируйте следующую функцию с различными типами аргументов:

```python
def create_user(name, age=18, *, active=True, **kwargs):
    user = {'name': name, 'age': age, 'active': active}
    user.update(kwargs)
    return user
```

Объясните, какие типы аргументов используются и как их правильно передавать при вызове.
  
### Ответ
asdf  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Рекурсивные функции
  
Какова сложность поиска, вставки и удаления в **сбалансированном двоичном дереве поиска** (например, AVL или Red-Black tree)?
  
Варианты ответов:
1) O(log n) для поиска, O(n) для вставки/удаления
2) O(n) для всех операций
3) O(log n) для всех операций
4) ❌ O(1) для поиска, O(log n) для вставки/удаления
5) O(n²) для всех операций
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Lambda-функции
  
Какова временная сложность вычисления n-го числа Фибоначчи с использованием lambda и reduce?

```python
from functools import reduce

fibonacci = lambda n: reduce(lambda acc, _: (acc[1], acc[0] + acc[1]), range(n-1), (0, 1))[0]
```
  
Варианты ответов:
1) O(2^n) - экспоненциальная из-за рекурсии
2) ✅ O(n) - линейная сложность, итеративное вычисление
3) O(1) - константная, только арифметика
4) O(n log n) - из-за reduce
5) O(n²) - квадратичная
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Определение и вызов функции
  
Какой из следующих вариантов **правильно** определяет и вызывает функцию в Python?

```python
# 1. Определение функции
def greet(name):
    return f"Hello, {name}!"

# 2. Вызов функции
message = greet("Alice")
```
  
Варианты ответов:
1) def greet(name): print(f'Hello, {name}!') - ничего не возвращает
2) ❌ greet = lambda name: f'Hello, {name}!'; message = greet['Alice'] - ошибка, функция вызывается круглыми скобками
3) function greet(name): return f'Hello, {name}!' - неверный синтаксис
4) def greet = (name): return f'Hello, {name}!' - неверный синтаксис
5) def greet(name): return f'Hello, {name}!' - правильное определение и вызов
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 6. Возвращаемые значения
  
Что возвращает следующая функция и почему?

```python
def process_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n * 2)
    # Нет явного return
```
  
Варианты ответов:
1) None - функция без явного return возвращает None
2) Произойдет ошибка - отсутствует return
3) 0 - значение по умолчанию
4) ❌ [] - пустой список, так как result не изменяется
5) Последний элемент result
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 7. Комплексная задача
  
Проанализируйте следующую функцию высшего порядка:

```python
def compose(*functions):
    def composed(x):
        for func in reversed(functions):
            x = func(x)
        return x
    return composed

# Использование
add_one = lambda x: x + 1
multiply_two = lambda x: x * 2
square = lambda x: x ** 2

pipeline = compose(add_one, multiply_two, square)
result = pipeline(3)
```

Определите:
1. Что делает функция compose
2. Какой результат будет в pipeline(3)
3. Временную сложность composed
4. Можно ли оптимизировать по памяти?
5. Предложите альтернативный вариант
  
### Ответ
фыва  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 8. Область видимости (scope)
  
Проанализируйте код и объясните, какие значения будут выведены и почему:

```python
x = 10

def outer():
    x = 20
    
    def inner():
        nonlocal x
        x = 30
        print(f'inner: {x}')
    
    inner()
    print(f'outer: {x}')

outer()
print(f'global: {x}')
```
  
### Ответ
цуке  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 9. Декораторы
  
Объясните концепцию декораторов на примере таймера:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Время выполнения: {time.time() - start}')
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return 'Done'
```
  
### Ответ
фывафыв  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 10. Генераторы и yield
  
Какова временная сложность алгоритма генератора, который фильтрует и преобразует данные?

```python
def process_data(data):
    for item in data:
        if item % 2 == 0:
            yield item * 2
```
  
Варианты ответов:
1) O(log n) - логарифмическая
2) O(n!) - факториальная
3) O(1) - константная для каждого элемента
4) ✅ O(n) - линейная относительно размера входных данных
5) O(n²) - квадратичная из-за фильтрации
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">

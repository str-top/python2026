Вопросы с выбором варианта: 33/39%  
# Вопрос 1. Рекурсивные функции
  
Какова сложность поиска, вставки и удаления в **сбалансированном двоичном дереве поиска** (например, AVL или Red-Black tree)?
  
Варианты ответов:
- [ ] Option 1: O(1) для поиска, O(log n) для вставки/удаления
- [ ] Option 2: O(n) для всех операций
- [X] ✅ Option 3: O(log n) для всех операций
- [ ] Option 4: O(n²) для всех операций
- [ ] Option 5: O(log n) для поиска, O(n) для вставки/удаления
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 2. Lambda-функции
  
Какова временная сложность вычисления n-го числа Фибоначчи с использованием lambda и reduce?

```python
from functools import reduce

fibonacci = lambda n: reduce(lambda acc, _: (acc[1], acc[0] + acc[1]), range(n-1), (0, 1))[0]
```
  
Варианты ответов:
- [ ] Option 1: O(2^n) - экспоненциальная из-за рекурсии
- [X] ✅ Option 2: O(n) - линейная сложность, итеративное вычисление
- [ ] Option 3: O(n²) - квадратичная
- [ ] Option 4: O(1) - константная, только арифметика
- [ ] Option 5: O(n log n) - из-за reduce
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Определение и вызов функции
  
Какой из следующих вариантов **правильно** определяет и вызывает функцию в Python?

```python
# 1. Определение функции
def greet(name):
    return f"Hello, {name}!"

# 2. Вызов функции
message = greet("Alice")
```
  
Варианты ответов:
- [ ] Option 1: def greet = (name): return f'Hello, {name}!' - неверный синтаксис
- [ ] Option 2: def greet(name): print(f'Hello, {name}!') - ничего не возвращает
- [X] ❌ Option 3: greet = lambda name: f'Hello, {name}!'; message = greet['Alice'] - ошибка, функция вызывается круглыми скобками
- [ ] Option 4: def greet(name): return f'Hello, {name}!' - правильное определение и вызов
- [ ] Option 5: function greet(name): return f'Hello, {name}!' - неверный синтаксис
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 4. Комплексная задача
  
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
Функция compose(*functions) создаёт композицию функций, применяя их справа налево.
Например, pipeline = compose(add_one, multiply_two, square); pipeline(3) вернёт 19.
Временная сложность O(n), память минимальна.
Альтернатива: с functools.reduce:
from functools import reduce
compose = lambda *f: lambda x: reduce(lambda v, func: func(v), reversed(f), x)
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 5. Декораторы
  
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
фыва
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 6. Аргументы функции
  
Проанализируйте следующую функцию с различными типами аргументов:

```python
def create_user(name, age=18, *, active=True, **kwargs):
    user = {'name': name, 'age': age, 'active': active}
    user.update(kwargs)
    return user
```

Объясните, какие типы аргументов используются и как их правильно передавать при вызове.
  
### Ответ
фывафы
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 7. Генераторы и yield
  
Какова временная сложность алгоритма генератора, который фильтрует и преобразует данные?

```python
def process_data(data):
    for item in data:
        if item % 2 == 0:
            yield item * 2
```
  
Варианты ответов:
- [ ] Option 1: O(1) - константная для каждого элемента
- [ ] Option 2: O(log n) - логарифмическая
- [ ] Option 3: O(n!) - факториальная
- [ ] Option 4: O(n²) - квадратичная из-за фильтрации
- [X] ✅ Option 5: O(n) - линейная относительно размера входных данных
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 8. Замыкания (closures)
  
Проанализируйте временную и пространственную сложность замыканий. Объясните, когда они могут потреблять много памяти и почему.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multipliers = [make_multiplier(i) for i in range(1000000)]
```
  
### Ответ
йцук
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 9. Область видимости (scope)
  
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
йцукйываы
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 10. Возвращаемые значения
  
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
- [ ] Option 1: Произойдет ошибка - отсутствует return
- [X] ✅ Option 2: None - функция без явного return возвращает None
- [ ] Option 3: [] - пустой список, так как result не изменяется
- [ ] Option 4: Последний элемент result
- [ ] Option 5: 0 - значение по умолчанию
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">

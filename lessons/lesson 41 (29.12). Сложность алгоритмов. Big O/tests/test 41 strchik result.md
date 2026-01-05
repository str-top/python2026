Вопросы с выбором варианта: 12/39%  
#  Вопрос 1. Хеш-таблицы
  
## Хеш-таблицы

Проанализируйте временную и пространственную сложность хеш-таблиц. Объясните, в каких случаях сложность деградирует до O(n) и почему.
  
Answer:
asdfzzxczvfasd
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
  
#  Вопрос 2. Амортизированный анализ
  
## Амортизированный анализ

Объясните концепцию амортизированного анализа на примере динамического массива (list в Python), когда он увеличивает свой размер.
  
Answer:
asdfzzxczvfasd
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
  
#  Вопрос 3. Пространственная сложность
  
## Пространственная сложность

Проанализируйте пространственную сложность следующего рекурсивного алгоритма вычисления факториала:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

Объясните, сколько памяти используется в стеке вызовов и как это зависит от n.
  
Answer:
asdfzzxczvfasd
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
  
# ❌ Вопрос 4. Сортировки
  
## Сортировки

Какова **асимптотически наилучшая возможная сложность в худшем случае** для алгоритмов сортировки, которые **сравнивают элементы** (comparison-based)?

```python
# Пример comparison-based сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
  
Варианты ответов:
- [ ] Option 1: O(n) - линейная сложность
- [ ] Option 2: O(n log n) - линейно-логарифмическая сложность
- [ ] Option 3: O(n²) - квадратичная сложность
- [X] **Option 4: O(log n) - логарифмическая сложность**
- [ ] Option 5: O(1) - константная сложность
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
  
# ❌ Вопрос 5. Графы
  
## Графы

Какова временная сложность алгоритма поиска в глубину (DFS) в графе с V вершинами и E рёбрами?

```python
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
```
  
Варианты ответов:
- [ ] Option 1: O(V + E) - линейная относительно числа вершин и рёбер
- [ ] Option 2: O(V²) - квадратичная относительно числа вершин
- [X] **Option 3: O(V log V) - зависит от числа вершин**
- [ ] Option 4: O(E log V) - зависит от рёбер и вершин
- [ ] Option 5: O(V * E) - произведение вершин и рёбер
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
  
# ❌ Вопрос 6. Временная сложность операций
  
## Временная сложность операций

Какова **средняя (амортизированная) временная сложность** поиска элемента в следующих структурах данных (в Python)?

```python
# 1. Проверка наличия в списке (list)
my_list = [1, 2, 3, 4, 5]
x = 3 in my_list

# 2. Проверка наличия в множестве (set)
my_set = {1, 2, 3, 4, 5}
x = 3 in my_set

# 3. Доступ по ключу в словаре (dict)
my_dict = {'a': 1, 'b': 2, 'c': 3}
x = my_dict['b']
```

Примечание: в `set` и `dict` **в худшем случае** может быть `O(n)`, но здесь спрашивается средняя.
  
Варианты ответов:
- [ ] Option 1: O(n), O(1), O(1) - линейный для списка, константный для set и dict
- [ ] Option 2: O(1), O(1), O(1) - все операции константные
- [X] **Option 3: O(n), O(n), O(n) - все операции линейные**
- [ ] Option 4: O(log n), O(log n), O(log n) - все логарифмические
- [ ] Option 5: O(n), O(log n), O(1) - линейный, логарифмический, константный
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
  
# ✅ Вопрос 7. Динамическое программирование
  
## Динамическое программирование

Какова временная сложность вычисления n-го числа Фибоначчи с использованием динамического программирования?

```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
```
  
Варианты ответов:
- [ ] Option 1: O(2^n) - экспоненциальная сложность
- [ ] Option 2: O(n) - линейная сложность
- [X] **Option 3: O(n log n) - линейно-логарифмическая**
- [ ] Option 4: O(log n) - логарифмическая сложность
- [ ] Option 5: O(n²) - квадратичная сложность
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
  
# ✅ Вопрос 8. Деревья поиска
  
## Деревья поиска

Какова сложность поиска, вставки и удаления в сбалансированном двоичном дереве поиска (например, AVL или Red-Black tree)?
  
Варианты ответов:
- [ ] Option 1: O(log n) для всех операций
- [ ] Option 2: O(n) для всех операций
- [ ] Option 3: O(1) для поиска, O(log n) для вставки/удаления
- [ ] Option 4: O(log n) для поиска, O(n) для вставки/удаления
- [X] **Option 5: O(n²) для всех операций**
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
  
#  Вопрос 9. Комплексная задача
  
## Комплексная задача

Проанализируйте следующий алгоритм:

```python
def find_pairs(arr, target):
    result = []
    seen = {}
    for num in arr:
        complement = target - num
        if complement in seen:
            result.append((complement, num))
        seen[num] = True
    return result
```

Определите:
1. Временную сложность
2. Пространственную сложность
3. Можно ли улучшить по памяти?
4. Предложите альтернативный вариант
  
Answer:
asefz
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
  
#  Вопрос 10. Оптимизация кода
  
## Оптимизация кода

Дан код для поиска уникальных элементов:

```python
def find_unique(arr):
    unique = []
    for item in arr:
        if item not in unique:
            unique.append(item)
    return unique
```

Проанализируйте сложность и предложите оптимизированную версию с объяснением.
  
Answer:
asefz
  
## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)

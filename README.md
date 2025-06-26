📊 CSV Processor

**CSV Processor** — это консольная утилита для фильтрации и агрегации данных из CSV-файлов. Написана на чистом Python, без сторонних библиотек, кроме `tabulate` и `pytest` (для красивого вывода и тестов).

---

## 🚀 Возможности

* 📁 Чтение CSV-файла с любыми колонками
* 🔍 Фильтрация по одному условию (`==`, `>`, `<`, `=` как синоним `==`)
* 📈 Агрегация (`avg`, `min`, `max`) по числовым колонкам
* 🧩 Комбинированное использование фильтрации и агрегации
* ✅ Удобный CLI-интерфейс через `argparse`
* 🧪 Покрытие тестами с помощью `pytest`

---

## 🧾 Пример CSV-файла

```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4
```

---

## ⚙️ Установка

Убедитесь, что у вас установлен Python 3.7+.

Установите зависимости:

```bash
pip install -r requirements.txt
```

Содержимое `requirements.txt`:

```text
tabulate
pytest
```

---

## 🧑‍💻 Использование

```bash
python main.py --file <путь_к_csv> [--where <условие>] [--aggregate <агрегация>]
```

### 📌 Аргументы

| Аргумент | Обязательный | Описание                                                   |
| ---------------- | ------------------------ | ------------------------------------------------------------------ |
| `--file`       | ✅                       | Путь к CSV-файлу                                         |
| `--where`      | ❌                       | Фильтрация:`column==value`,`column>value`, и т.п. |
| `--aggregate`  | ❌                       | Агрегация: `column=avg                                    |

---

### 🔍 Примеры запуска

#### ✅ Вывести все строки

```bash
python3 main.py --file products.csv

| name             | brand   |   price |   rating |
|------------------|---------|---------|----------|
| iphone 15 pro    | apple   |     999 |      4.9 |
| galaxy s23 ultra | samsung |    1199 |      4.8 |
| redmi note 12    | xiaomi  |     199 |      4.6 |
| iphone 14        | apple   |     799 |      4.7 |
| galaxy a54       | samsung |     349 |      4.2 |
| poco x5 pro      | xiaomi  |     299 |      4.4 |
| iphone se        | apple   |     429 |      4.1 |
| galaxy z flip 5  | samsung |     999 |      4.6 |
| redmi 10c        | xiaomi  |     149 |      4.1 |
| iphone 13 mini   | apple   |     599 |      4.5 |
```

#### 🔍 Отфильтровать по бренду

```bash
python3 main.py --file products.csv --where "brand==xiaomi"

| name          | brand   |   price |   rating |
|---------------|---------|---------|----------|
| redmi note 12 | xiaomi  |     199 |      4.6 |
| poco x5 pro   | xiaomi  |     299 |      4.4 |
| redmi 10c     | xiaomi  |     149 |      4.1 |
```

#### 📈 Посчитать максимум по цене

```bash
python3 main.py --file products.csv --aggregate "price=max"

|   max(price) |
|--------------|
|         1199 |
```

#### 🔗 Комбинировать фильтр и агрегацию

```bash
python3 main.py --file products.csv --where "brand==xiaomi" --aggregate "rating=min"

|   min(rating) |
|---------------|
|           4.1 |
```

---

## 🧪 Тесты

Тесты находятся в папке `tests/` и покрывают:

* фильтрацию (все типы условий)
* агрегации (все операции)
* ошибки при неверном вводе
* интерфейс запуска скрипта через CLI

### ▶ Запуск всех тестов

```bash
pytest
```

### 📊 Покрытие кода

Установите `pytest-cov`, если хотите посмотреть покрытие:

```bash
pip install pytest-cov
pytest --cov=.
```

---

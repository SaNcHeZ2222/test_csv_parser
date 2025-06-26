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
python main.py --file example.csv
```

#### 🔍 Отфильтровать по бренду

```bash
python main.py --file example.csv --where "brand=xiaomi"
```

#### 📈 Посчитать максимум по цене

```bash
python main.py --file example.csv --aggregate "price=max"
```

#### 🔗 Комбинировать фильтр и агрегацию

```bash
python main.py --file example.csv --where "brand=xiaomi" --aggregate "rating=min"
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

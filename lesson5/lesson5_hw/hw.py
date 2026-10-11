'''
⁠1.1 save_test_ids(test_ids) — принимает список ID тестов и сохраняет их в tests.txt. Каждый ID должен находиться на отдельной строке.
1.2⁠  ⁠add_test_id(test_id) — добавляет один новый ID в конец существующего файла, не удаляя предыдущие записи.
1.3  ⁠load_test_ids(filename) — читает файл и возвращает список ID. Пустые строки нужно пропускать, пробелы по краям удалять.
Пример исходного списка->["QA-1001", "QA-1002", "QA-1003"]
После вызова add_test_id("QA-1004") функция load_test_ids("tests.txt") должна вернуть:
["QA-1001", "QA-1002", "QA-1003", "QA-1004"]
Используйте: def, return, for, list, append(), with open(), режимы w, a, r, strip().
Проверьте пустой список, повторное добавление записи и чтение файла с пустыми строками.
'''
from tkinter.constants import BROWSE

# def save_test_id(test_ids):
#     if type(test_ids) != list or not test_ids:
#         print('wrong format')
#         return
#     with open('tests.txt','w',encoding='utf-8') as file:
#         for test in test_ids:
#             file.write(test.strip()+'\n')
#
# save_test_id(['qa-001','  qa-002', 'qa-003  '])
# save_test_id([])
# save_test_id('test-001')
#
# def add_test_id(test_id):
#     with open('tests.txt', 'a', encoding='utf-8') as file:
#         if not test_id:
#             print('empty id')
#             return
#         file.write(test_id.strip()+'\n')
#
# add_test_id('qa-004 ')
# add_test_id('')
#
# def load_test_id(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         return file.read().splitlines()
#
# print(load_test_id('tests.txt'))

'''
2.Создайте файл results.csv test_id,status,duration_ms
QA-1001,PASSED,120
QA-1002,FAILED,230
QA-1003,PASSED,150
Напишите функцию get_test_statistics(filename)

Функция должна:
1.⁠ ⁠Прочитать данные из CSV.
2.⁠ ⁠Посчитать общее количество тестов.
3.⁠ ⁠Посчитать количество PASSED и FAILED.
4.⁠ ⁠Найти суммарное время выполнения тестов в миллисекундах.
5.⁠ ⁠Собрать в список ID всех проваленных тестов.
6.Вернуть словарь с результатом
Ожидаемый резальт->
{
    "total": 3,
    "passed": 2,
    "failed": 1,
    "total_duration_ms": 500,
    "failed_ids": ["QA-1002"]
}
Используйте: csv.DictReader(), for, if, dict, list, int(), append(), return.
Считайте, что в корректном входном файле статусы могут быть только PASSED и FAILED, а время — целое неотрицательное число.
Дополнительно проверьте файл, содержащий только заголовки. Все счётчики должны быть равны нулю, список ошибок — пустой.

'''
import csv

def get_test_statistics(filename):
    stats = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "sum_duration_ms": 0,
        "failed_ids": []
    }
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        for row in csv.DictReader(file):
            stats["total"] += 1
            stats["sum_duration_ms"] += int(row["duration_ms"])
            if row["status"] == "PASSED":
                stats["passed"] += 1
            else:
                stats["failed"] += 1
                stats["failed_ids"].append(row["test_id"])
    return stats

print(get_test_statistics('results.csv'))

'''
Напишите две функции:
•⁠  ⁠save_test_config(environment, base_url, timeout) — создаёт config.json и сохраняет параметры тестового окружения.
•⁠  ⁠load_test_config(filename) — читает JSON и возвращает словарь с настройками.
Пример вызова
save_test_config(
    "staging",
    "https://example.com",
    30
)
Ожидаемый JSON {
    "environment": "staging",
    "base_url": "https://example.com",
    "timeout": 30
}
—-----------
1.⁠ ⁠Для сохранения используйте json.dump().
2.⁠ ⁠Для чтения используйте json.load().
3.⁠ ⁠Сохраняйте данные с отступами для удобного чтения.
4.⁠ ⁠Проверьте, что после загрузки тип timeout остаётся int.
5.⁠ ⁠Проверьте, что повторное сохранение заменяет старую конфигурацию.

Используйте: dict, json.dump(), json.load(), with open(), type(), assert.
'''

import json

def save_test_config(environment, base_url, timeout):
    config = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout
    }
    with open('config.json', 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=2)

def load_test_config(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

save_test_config("staging", "https://example.com", 30)
config = load_test_config("config.json")

# данные совпадают с ожидаемыми
assert config == {
    "environment": "staging",
    "base_url": "https://example.com",
    "timeout": 30
}, f"Unexpected config: {config}"

# 4. timeout после загрузки остался int
assert type(config["timeout"]) is int, f"timeout is {type(config['timeout'])}"

# повторное сохранение заменяет старую конфигурацию
save_test_config("prod", "https://prod.example.com", 60)
config = load_test_config("config.json")

assert config["environment"] == "prod"
assert config["base_url"] == "https://prod.example.com"
assert config["timeout"] == 60
assert len(config) == 3, "Old data was not replaced"

print("All checks passed")
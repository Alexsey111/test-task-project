# Задача 2
#
# Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных
# (https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv
# количество животных на каждую букву алфавита. Содержимое результирующего файла:
#
# А,642
# Б,412
# В,....
#
# Примечание:
# анализ текста производить не нужно, считается любая запись из категории
# (в ней может быть не только название, но и, например, род)

import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict
import time
import os

BASE_URL = "https://ru.wikipedia.org"
START_URL = "/wiki/Категория:Животные_по_алфавиту"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_animals_count_by_letter():
    url = BASE_URL + START_URL
    counts = defaultdict(int)

    while url:
        print(f"Обработка: {url}")
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            for li in soup.select('.mw-category-group ul li'):
                text = li.text.strip()
                if text:
                    first_letter = text[0].upper()
                    counts[first_letter] += 1

            next_link = soup.find('a', string='Следующая страница')
            if next_link:
                url = BASE_URL + next_link['href']
                time.sleep(0.5)
            else:
                url = None

        except requests.RequestException as e:
            print(f"Ошибка при загрузке {url}: {e}")
            url = None

    return counts

def save_to_csv(counts, filename=None):
    if filename is None:
        # Сохраняем в папку с задачей
        dir_path = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(dir_path, 'beasts.csv')

    with open(filename, mode='w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])

if __name__ == "__main__":
    counts = get_animals_count_by_letter()
    save_to_csv(counts)
    print("Готово! Результат сохранён в beasts.csv")

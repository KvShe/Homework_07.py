import csv
import database
import qui


def import_data():
    try:
        with open(qui.file_name() + '.csv', newline='') as f:
            reader = list(csv.reader(f, delimiter=';'))
        [database.add_contact(item) for item in reader]
    except FileNotFoundError:
        print('Файл не найден')


def write_to_file(lst):
    with open(qui.file_name() + '.txt', 'w') as f:
        for item in lst:
            f.write(', '.join(item) + '\n')

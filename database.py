import psycopg2
from config import host, user, password, db_name


def contact_list():
    with connection.cursor() as cursor:
        cursor.execute('select * from contacts;')
        return cursor.fetchall()


def add_contact(lst):
    with connection.cursor() as cursor:
        cursor.execute(
            "insert into contacts (last_name, first_name, phone) values ('{}', '{}', '{}');".format(lst[0],
                                                                                                    lst[1], lst[2]))


def deletion_contact(string):
    with connection.cursor() as cursor:
        cursor.execute("delete from contacts where last_name='{}';".format(string))


def contact_finder(string):
    with connection.cursor() as cursor:
        cursor.execute("select last_name, first_name from contacts where last_name = '{}'".format(string))
        print(*cursor.fetchone())


def change(last_name, phone):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE contacts SET phone = '{}' WHERE last_name = '{}';".format(phone, last_name))


connection = psycopg2.connect(host=host,
                              user=user,
                              password=password,
                              database=db_name)

connection.autocommit = True  # авто-коммит - без него не будет обновляться database

change('Шафигуллин', '48165464684')

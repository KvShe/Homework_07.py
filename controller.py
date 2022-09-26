from database import contact_list, add_contact, deletion_contact, contact_finder, change
import qui
from file_management import import_data, write_to_file

match qui.user_choice():
    case '1':
        [print(*item) for item in contact_list()]
        # Переделал в комперхейшен из-за того, что contact_list перестал выводить print
    case '2':
        add_contact(qui.enter_data())
    case '3':
        deletion_contact(qui.del_contact())
    case '4':
        contact_finder(qui.del_contact())
    case '5':
        last_name, phone = qui.change_phone()
        change(last_name, phone)
    case '6':
        import_data()
    case '7':
        write_to_file(contact_list())
    case _:
        print('Введена недопустимая операция')

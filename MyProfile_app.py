# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
user_name = ''
user_age = 0
telephone_number = ''
Email_address = ''
postcode = ''
mail_address = ''
additional_information = ''

# information about the entrepreneur
state_regist_num_IE = 0
tax_identification_num = 0
payment_account = 0
bank_name = ''
bank_id_cod = 0
correspondent_account = 0


def personal_info_user(name, age, telephone, email, index, mail, add_info):
    print(SEPARATOR)
    print(f'Имя:   \t{name}')
    print(f'Возраст: {age} ', end='')
    if (age % 10 == 1) and (age != 11) and (age % 100 != 11):
        print('год')
    elif (1 < age % 10 <= 4) and (age != 12) and (age != 13) and (age != 14):
        print('года')
    else:
        print('лет')
    print(f'Телефон: {telephone}')
    print(f'E-mail:  {email}')
    print(f'Индекс:  {index}')
    print(f'Почтовый адрес: {mail}')
    print(f'Дополнительная информация: {add_info}')


def general_info_user(srni, tin, pay_ac, bank, bank_id, cor_ac):
    personal_info_user(user_name, user_age, telephone_number, Email_address,
                       postcode, mail_address, additional_information)
    print()
    print('Информация о предпринимателе')
    print(f'ОГРНИП: {srni}')
    print(f'ИНН: {tin}')
    print('Банковские реквизиты')
    print(f'Р/С: {pay_ac}')
    print(f'Банк: {bank}')
    print(f'БИК: {bank_id}')
    print(f'К/С: {cor_ac}')


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    main_menu = int(input('Введите номер пункта меню: '))

    if main_menu == 0:
        break

    elif main_menu == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            editing_option = int(input('Введите номер пункта меню: '))

            if editing_option == 0:
                break
            elif editing_option == 1:
                # input personall info
                user_name = input('Введите имя: ')
                while True:
                    # validate user age
                    user_age = int(input('Введите возраст: '))
                    if user_age < 0:
                        print('Некорректный ввод! Возраст должен быть положительным')
                    else:
                        break

                telephone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')

                Email_address = input('Введите адрес электронной почты: ')
                # validate postcode
                postcode = input('Введите индекс: ')
                count_num = ''
                for symbol in postcode:
                    if '0' <= symbol <= '9':
                        count_num += symbol
                postcode = int(count_num)

                mail_address = input('Введите почтовый адрес: ')

                additional_information = input('Введите дополнительную информацию: ')

            elif editing_option == 2:
                # input information about the entrepreneur
                while True:
                    # validate character count
                    state_regist_num_IE = int(input('Введите ОГРНИП: '))
                    if len(str(state_regist_num_IE)) == 15:
                        break
                    else:
                        print('Некорректный ввод! Пожалуйста введите заново')

                tax_identification_num = int(input('Введите ИНН: '))

                while True:
                    # validate character count
                    payment_account = int(input('Введите расчётный счёт: '))
                    if len(str(payment_account)) == 20:
                        break
                    else:
                        print('Некорректный ввод! Пожалуйста введите заново')

                bank_name = input('Введите название банка: ')

                bank_id_cod = int(input('Введите БИК: '))

                correspondent_account = int(input('Введите корреспондентский счёт: '))

            else:
                print('Введите корректный пункт меню')

    elif main_menu == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            print_info = int(input('Введите номер пункта меню: '))
            if print_info == 0:
                break
            elif print_info == 1:
                personal_info_user(user_name, user_age, telephone_number, Email_address,
                                   postcode, mail_address, additional_information)
            elif print_info == 2:
                general_info_user(state_regist_num_IE, tax_identification_num, payment_account,
                                  bank_name, bank_id_cod, correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')

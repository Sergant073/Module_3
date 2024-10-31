def send_email(message, recipient, *, sender="university.help@gmail.com"):


    def is_valid_email(email):
        return (isinstance(email, str)
                and "@" in email
                and (email.endswith('.com')
                     or email.endswith('.ru')
                     or email.endswith('.net')))

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



mail = str(input('Введите ваш email:  '))

send_email('Проверка', mail)

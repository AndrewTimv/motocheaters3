"""
Answer phrases
"""

# Главное меню  ---------------------------------------------------
hello = 'Привет, {}! Хочешь узнать, кто кидала? Напиши номер телефона, банковской карты или адрес страницы.'

tell_about_cheater = 'Расскажи свою историю. \n Если передумал - нажми на кнопку'

help_us = 'Для помощи можешь перевести денежку сам знаешь куда.'

samples = 'Например: \n' \
          'Страницы: \n' \
          'vk.com/id987654321 \n' \
          'vk.com/durov \n' \
          'а еще лучше - скопируйте адрес из браузера;\n' \
          'Телефоны: \n' \
          '+700012365487 \n' \
          '89991112233 \n' \
          'Карты: \n' \
          '1234 5678 9123 4567 8901 \n' \
          '1234567890123456'

how_check = 'Чтобы проверить человека, напиши адрес его страницы, номер телефона или номер банковской карты. \n' \
            + samples

change_mind = 'Если захочешь рассказать - ждем!'

thanks = 'Спасибо!'

# Ответы на запросы кидал ----------------------------------------------------------------------------------------------
is_cheater = 'Это кидала! Не доверяй ему.'

is_fifty = 'Иногда кидает. А иногда нет. Будь осторожен.'

not_cheater = 'В наших базах ничего не найдено. Но всегда будь начеку.'

dont_understand = 'Извини, я тебя не понял. Напиши адрес страницы, телефон или номер банковской карты. \n'

# Сообщения админам. ---------------------------------------------------------------------------------------------------
dont_understand_to_admin = 'Пользователь vk.com/{} написал что-то непонятное:\n'
cheater_story_to_admin = 'Пользователь vk.com/{} хочет поделиться кидалой:\n'
admin_menu = 'Ты в админском меню.'
return_to_main = 'Ты на главной.'
spam_header = 'Напиши текст, который ты хочешь разослать всем членам группы.'
spam_send = 'Сейчас отправляю(нет) всем текст:\n'

add_cheater_id = 'Введи адрес страницы, телефон или номер карты. Если хочешь добавить полтиника - введи 50.' \
                 'Как только все введешь - нажми "Добавить"'
add_cheater_tel = 'Введи телефоны (каждый с новой строчки)'
add_cheater_card = 'Введи номера карт (каждую с новой строчки)'
add_cheater_proof = 'Введи ссылку на страницу'
# TODO Указать на id пользователя/группы.
add_cheater_id_delete = 'Этот пользователь(сообщество) @{} пока под баном.'
add_cheater_no_id = 'Такого id Вконтакте нет. Лучше возьми другой.'
add_cheater_exist = 'Уже есть чел с параметрами:\n id: {vk_id}, screen_name: {screen_name} '
add_cheater_new_screen_name = 'Кидала старый - имя новое. Вот известный чел: \n id: {vk_id}, screen_name: {screen_name}'
add_cheater_error_value = 'Не распознал, введи еще раз.'
add_cheater_ok = 'Кидала добавлен.'

del_cheater_start = '''Введи ID, Screen_name, телефон, карту или пруфлинк.
                       ID, Screen_name - удаляет все связанное с кидалой.
                       Телефон, карта, пруфлинк - удалит все записи о соответствующей категории. 
                    '''
del_cheater_error_value = 'Не распознал, введи еще раз.'
del_success = 'Удалили(нет)'

admin_common = 'Нажми на одну из кнопок.'

# Заготовки для развернутых ответов. -----------------------------------------------------------------------------------
cheaters_card = """
                Карта {card} принадлежит пользователю {vk_id} {firstname} {lastname}.
                Он есть в наших базах. Не доверяй ему.
                """

cheaters_telephone = """
                Телефон {tel} принадлежит пользователю {vk_id} {firstname} {lastname}.
                Он есть в наших базах. Не доверяй ему.
                """

cheaters_user = """
                Пользователь vk.vom/{vk_id} {firstname} {lastname}\
                 есть в наших базах.
                Не доверяй ему.
                """

cheaters_group = 'Группа vk.com/{group} есть в наших базах. Не доверяй ей!'

# Тексты для апдейта БД. -----------------------------------------------------------------------------------------------
update_db_from_file = 'Ты решил обновить БД через файл. Жди, пожалуйста.'
no_data_in_file = 'В файле нет нужных данных.'

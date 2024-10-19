import pandas as pd
from Tools.demo.spreadsheet import ljust

pd.options.display.expand_frame_repr = False
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
person = pd.DataFrame([[0, 'Анна Петровна Смирнова', 47, 'женский', 0, 20], [1, 'Иван Сергеевич Петров', 26, 'мужской', 3, 16], [2, 'Мария Ивановна Сидорова', 38, 'женский', 9, 23], [3, 'Сергей Михайлович Иванов', 33, 'мужской', 3, 9], [4, 'Ольга Дмитриевна Васильева', 29, 'женский', 7, 5], [5, 'Дмитрий Викторович Соколов', 44, 'мужской', 5, 27], [6, 'Елена Николаевна Петрова', 32, 'женский', 6, 8], [7, 'Андрей Константинович Васильев', 50, 'мужской', 7, 24], [8, 'Татьяна Михайловна Соколова', 23, 'женский', 8, 2], [9, 'Алексей Викторович Смирнов', 36, 'мужской', 9, 12], [10, 'Екатерина Сергеевна Иванова', 25, 'женский', 10, 0], [11, 'Виктор Дмитриевич Петров', 49, 'мужской', 9, 3], [12, 'Юлия Константиновна Сидорова', 42, 'женский', 0, 19], [13, 'Михаил Сергеевич Васильев', 28, 'мужской', 1, 22], [14, 'Ирина Николаевна Соколова', 39, 'женский', 2, 26], [15, 'Николай Викторович Петров', 35, 'мужской', 3, 17], [16, 'Светлана Михайловна Сидорова', 22, 'женский', 4, 4], [17, 'Константин Дмитриевич Иванов', 46, 'мужской', 5, 14], [18, 'Галина Николаевна Васильева', 41, 'женский', 6, 6], [19, 'Павел Викторович Смирнов', 24, 'мужской', 7, 28], [20, 'Роман Сергеевич Иванов', 34, 'женский', 8, 13], [21, 'Виктория Михайловна Сидорова', 59, 'мужской', 9, 21], [22, 'Александр Дмитриевич Васильев', 27, 'женский', 10, 18], [23, 'Дарья Николаевна Соколова', 43, 'мужской', 11, 7], [24, 'Григорий Викторович Петров', 48, 'женский', 0, 25], [25, 'Виталий Сергеевич Сидоров', 31, 'мужской', 1, 10], [26, 'Ксения Михайловна Иванова', 45, 'женский', 2, 29], [27, 'Максим Викторович Васильев', 20, 'мужской', 3, 1], [28, 'Валерия Николаевна Соколова', 37, 'женский', 4, 15], [29, 'Артём Сергеевич Петров', 40, 'мужской', 5, 11]], columns=['id', 'ФИО', 'Возраст', 'Пол', 'ID_Фирмы', 'ID_Должности'])
position = pd.DataFrame([[0, 'Системный администратор'], [1, 'Веб-разработчик'], [2, 'Инженер по тестированию'], [3, 'Специалист по информационной безопасности'], [4, 'Администратор баз данных'], [5, 'UX/UI-дизайнер'], [6, 'Разработчик мобильных приложений'], [7, 'Аналитик данных'], [8, 'DevOps-инженер'], [9, 'Архитектор решений'], [10, 'Технический писатель'], [11, 'Менеджер проектов'], [12, 'Бизнес-аналитик'], [13, 'Сетевой инженер'], [14, 'Специалист технической поддержки'], [15, 'Data Scientist'], [16, 'Специалист по машинному обучению'], [17, 'Администратор серверов'], [18, 'Программист'], [19, 'Инженер облачных технологий'], [20, 'Инженер-исследователь'], [21, 'Специалист по кибербезопасности'], [22, 'Специалист по работе с большими данными'], [23, 'Инженер по автоматизации процессов'], [24, 'Инженер машинного обучения'], [25, 'Инженер искусственного интеллекта'], [26, 'Инженер по разработке алгоритмов'], [27, 'Инженер по оптимизации производительности'], [28, 'Инженер по внедрению новых технологий'], [29, 'Инженер по анализу и обработке данных']], columns=['id', 'Название_Должности'])
firm = pd.DataFrame([[0, 'Цифровые технологии'], [1, 'IT-решения'], [2, 'ИнфоТех'], [3, 'Информационные системы'], [4, 'Техноком'], [5, 'Интеллект-системы'], [6, 'Интеллектуальные технологии'], [7, 'Кибернетика'], [8, 'Сети и системы'], [9, 'Технологии будущего'], [10, 'ИТ-эксперт'], [11, 'Инновационные технологии']], columns=['id', 'Название_Фирмы'])

union = person.merge(position, left_on="ID_Должности", right_on="id").merge(firm, left_on="ID_Фирмы", right_on="id")
# print(person.merge(position, left_on="ID_Должности", right_on="id").merge(firm, left_on="ID_Фирмы", right_on="id"))

list_of_position = dict()
for i in union['Название_Фирмы']:
    list_of_position[i] = []
    for j in union['Возраст']:
        for k in union.values:
            if (i in k and j in k) and (20 <= j <= 30):
                list_of_position[i].append(j)

max_len = 0
name_firm_with_max_person = ''
for i in list_of_position:
    if len(list_of_position[i]) > max_len:
        max_len = len(list_of_position[i])
        name_firm_with_max_person = i
print(name_firm_with_max_person)
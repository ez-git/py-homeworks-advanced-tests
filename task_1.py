
def russian_visits(geo_logs):

    geo_logs_2 = []
    for geo_log in geo_logs:
        for key, value in geo_log.items():
            if value[1] == 'Россия':
                geo_logs_2.append(geo_log)

    return geo_logs_2


def unique_ids(ids):

    values_list = []
    for value in ids.values():
        values_list = values_list + value

    return list(set(values_list))


def words_distribution(queries):

    results = {}
    result = ''

    for words in queries:
        words_list = words.split(' ')
        words_count = len(words_list)
        if results.get(words_count) is None:
            results.setdefault(words_count, 1)
        else:
            results[words_count] = results[words_count] + 1

    results = dict(sorted(results.items()))
    total = len(queries)
    for key, value in results.items():
        result = result + f'Количество запросов из {key} слов(а) -' \
                          f' {round(value / total * 100, 2)} %\n'

    return result


if __name__ == '__main__':

    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    russian_visits(geo_logs)

    ids = {
        'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]
    }
    unique_ids(ids)

    queries = [
        'смотреть сериалы онлайн', 'новости спорта', 'афиша кино',
        'курс доллара',
        'сериалы этим летом', 'курс по питону', 'сериалы про спорт'
    ]
    words_distribution(queries)

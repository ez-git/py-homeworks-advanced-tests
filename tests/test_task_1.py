from unittest import TestCase
from task_1 import russian_visits, unique_ids, words_distribution


class TestRussianVisits(TestCase):

    def test_russian_visits(self):
        test_data = [
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
        ]
        result = russian_visits(test_data)
        expected = [
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
        ]
        self.assertListEqual(result, expected)


class TestUniqueIDs(TestCase):

    def test_unique_ids(self):
        test_data = {
            'user1': [213, 213, 213, 15, 213],
            'user2': [54, 54, 119, 119, 119],
            'user3': [213]
        }
        result = unique_ids(test_data)
        expected = [15, 213, 54, 119]
        self.assertListEqual(sorted(result), sorted(expected))


class TestWordsDistribution(TestCase):

    def test_words_distribution(self):
        test_data = [
            'сериалы этим летом', 'курс по питону', 'сериалы про спорт'
        ]
        result = words_distribution(test_data)
        expected = 'Количество запросов из 3 слов(а) - 100.0 %\n'
        self.assertEqual(result, expected)

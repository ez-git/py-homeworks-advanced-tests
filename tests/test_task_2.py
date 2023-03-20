from unittest import TestCase
from task_2 import YaDisk, YA_TOKEN


class TestYaDisk(TestCase):

    def setUp(self) -> None:
        self.folder_path = 'my_new_folder'

    def test_folder_is_exist(self):

        result = YaDisk(YA_TOKEN).get_metainfo(self.folder_path)
        expected = 200
        self.assertEqual(result, expected)

    def test_folder_is_not_exist(self):

        result = YaDisk(YA_TOKEN).get_metainfo('test_name')
        expected = 404
        self.assertEqual(result, expected)

    def test_folder_created(self):
        result = YaDisk(YA_TOKEN).create_folder(self.folder_path)
        expected = [201, 409]
        self.assertIn(result, expected)

import unittest
from sort_script import SortScript, ResultType, SearchResult, SearchType


class SortScriptTest(unittest.TestCase):

    def setUp(self):
        self.sort_script = SortScript()

    def test_test(self):

        int_array = [0, 2, 4, 6, 8]
        return_data = self.sort_script.find_number(-1, int_array, 4, True, SearchType.GREATER_THAN)
        self.assertEquals(return_data.search_result, SearchResult.FOUND_GREATER)

    def test_test2(self):

        int_array = [0, 2, 4, 6, 8]
        return_data = self.sort_script.find_number(-1, int_array, 4, True, SearchType.GREATER_THAN)
        self.assertNotEquals(return_data.search_result, SearchResult.FOUND_GREATER)


if __name__ == '__main__':
    unittest.main()

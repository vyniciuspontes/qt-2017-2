from enum import Enum

class SearchResult(Enum):
    NOT_FOUND = 1
    FOUND_EXACT = 2
    FOUND_GREATER = 3
    FOUND_LESS = 4


class SearchType(Enum):
    LESS_THAN = 1
    LESS_THAN_EQUALS = 2
    EQUALS = 3
    GREATER_THAN_EQUALS = 4
    GREATER_THAN = 5


class ResultType(object):

    def __init__(self, search_result: None, result_index: None, result_value: None):
        self.search_result = search_result
        self.result_index = result_index
        self.result_value = result_value

    def __str__(self):
        return "{0} - Index: {1} - Value: {2}".format(self.search_result, self.result_index, self.result_value)


class SortScript:

    def find_number(self, key, int_array, array_size, ascending, search_type):

        if any(v is None for v in [key, int_array, array_size, ascending, search_type]):
            raise TypeError('Null arguments are not allowed')

        if len(int_array) <= 0:
            raise TypeError('int_array must have at least one element')

        if array_size != len(int_array):
            raise TypeError("array_size argument value is different from the int_array size")

        if int_array != sorted(int_array, reverse=not ascending):
            raise TypeError("int_array is not sorted correctly")

        current_result_type = ResultType(SearchResult.NOT_FOUND, None, None)

        for element in range(0, array_size):

            element_value = int_array[element]

            if search_type in (
                SearchType.EQUALS, SearchType.GREATER_THAN_EQUALS, SearchType.LESS_THAN_EQUALS) and element_value == key:

                current_result_type.result_index = element
                current_result_type.result_value = element_value
                current_result_type.search_result = SearchResult.FOUND_EXACT
                break

            elif search_type in (SearchType.LESS_THAN, SearchType.LESS_THAN_EQUALS):
                if element_value > key:
                    return current_result_type

                if element_value < key:
                    current_result_type.result_index = element
                    current_result_type.result_value = element_value
                    current_result_type.search_result = SearchResult.FOUND_LESS

            elif search_type in (SearchType.GREATER_THAN, SearchType.GREATER_THAN_EQUALS):

                if element_value > key:
                    current_result_type.result_index = element
                    current_result_type.result_value = element_value
                    current_result_type.search_result = SearchResult.FOUND_GREATER
                    return current_result_type

        return current_result_type

    def run(self):
        int_array = [1, 2, 6, 7]
        print(self.find_number(-1, int_array, 4, True, SearchType.GREATER_THAN))


if __name__ == '__main__':
    SortScript().run()

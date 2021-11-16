#!/usr/bin/env python3
""" Module for 1-simple_pagination """
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get_page - returns data for page/page-size """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page >= 1
        assert page_size >= 1
        ixrange = index_range(page, page_size)
        if not self.dataset() or ixrange[1] > len(self.__dataset):
            return []
        return self.dataset()[ixrange[0]:ixrange[1]]

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
        if ixrange[0] >= ixrange[1]:
            return []
        if not self.dataset() or ixrange[1] > len(self.__dataset):
            return []
        return self.dataset()[ixrange[0]:ixrange[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        get_hyper - returns a dict with keys:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.floor(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": None if total_pages == page else page + 1,
            "prev_page": None if page == 1 else page - 1,
            "total_pages": total_pages
        }

""" Module for 0-simple_helper_function """


def index_range(page, page_size):
    """ index_range - helper fn to return indexes for page/size """
    return (page_size * (page - 1), page_size * page)

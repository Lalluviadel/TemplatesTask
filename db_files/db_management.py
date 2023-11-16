"""Contains a class for managing the TinyDB database."""
from db_files.db_raw_data import db_raw_data

from tinydb import Query, TinyDB


class TinyDbManager:
    """Class for managing the TinyDB database."""

    def __init__(self, file_path):
        """
        Initialize DB manager.

        Args:
            file_path (str): path to json db file.
        """
        self.db = TinyDB(file_path)

    def filter_by_dict(self, search_dict):
        """
        Database search using a dictionary (keys are field names).

        Args:
            search_dict (dict): dictionary for finding field matches.

        Returns:
            list: db search result.
        """
        return self.db.search(Query().fragment(search_dict))

    def fill_db(self, list_dicts):
        """
        Fill the database with data.

        Args:
            list_dicts (list[dict]): data to fill the db.

        Returns:
            None:
        """
        self.db.insert_multiple(list_dicts)


if __name__ == '__main__':
    test_db = TinyDbManager('db.json')
    test_db.fill_db(db_raw_data)

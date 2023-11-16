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

    def create_table(self, table_name):
        """
        Create a new db table.

        Args:
            table_name (str): name of the new table.

        Returns:
            tinydb.database.Table: new table object.
        """
        return self.db.table(table_name)

    def fill_db(self, table_name, list_dicts):
        """
        Fill the database with data.

        Args:
            table_name (str): name of the new table.
            list_dicts (list[dict]): data to fill the db.

        Returns:
            None:
        """
        table = self.create_table(table_name)
        table.insert_multiple(list_dicts)


if __name__ == '__main__':
    test_db = TinyDbManager('db.json')
    test_db.fill_db('form_templates', db_raw_data)

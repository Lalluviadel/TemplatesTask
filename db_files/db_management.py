from tinydb import TinyDB, Query

from db_files.db_raw_data import db_raw_data


class TinyDbManager:


    def __init__(self, address):
        self.db = TinyDB(address)

    def filter_by_dict(self, search_dict):
        return self.db.search(Query().fragment(search_dict))

    def create_table(self, table_name):
        return self.db.table(table_name)

    def fill_db(self, table_name, list_dicts):
        table = self.create_table(table_name)
        table.insert_multiple(list_dicts)


if __name__ == '__main__':
    test_db = TinyDbManager('db.json')
    test_db.fill_db('form_templates', db_raw_data)


class DatabaseController(object):

    def __init__(self, database_login):
        self.connection = self.connect(database_login)

    def connect(self, database_login):
        return None

    def list_all_tables(self):
        return None

    def list_all_remnant(self):
        return None

    def get_all_abilities_of_remnant(self, remnant_name):
        return None

    def get_remnant_definition_by_name(self, remnant_name):
        return None

    def get_remnant_abilities(self, remnant_id):
        return None

    def get_remnant_definitions_by_type(self, remnant_types, rarity):
        return None

    def get_remnant_types(self, remnant_id):
        return None


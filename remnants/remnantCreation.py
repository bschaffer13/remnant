from database.databaseController import DatabaseController


def generate_random_remnant(level, types, rarity, database: DatabaseController, location=None):

    database.get_remnant_definitions_by_type(types, rarity)


from database.databaseController import DatabaseController
import sqlite3
from database.databaseLoginInfo import DatabaseLoginInfo


class SqliteController(DatabaseController):

    def __init__(self, database_login):
        super().__init__(database_login)
        self.cursor = self.connection.cursor()

    def connect(self, database_login: DatabaseLoginInfo):
        return sqlite3.connect(database_login.database_name)

    def list_all_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self.cursor.fetchall()

    def list_all_columns(self, table):
        self.cursor.execute("PRAGMA table_info(%s)" % table)
        return list(map(lambda x: x[1], self.cursor.fetchall()))

    def list_all_remnant(self):
        self.cursor.execute("select * from remnant_definitions")
        return self.cursor.fetchall()

    def get_all_abilities_of_remnant(self, remnant_name):
        self.cursor.execute(""" select abilities.name, abilities.description, abilities.power,
                                abilities.class_name, abilities.speed, abilities.special_modifier,
                                remnant_abilities.level
                                from abilities
                                inner join remnant_abilities
                                on remnant_abilities.ability_id = abilities.ability_id
                                inner join remnant_definitions
                                on remnant_abilities.remnant_id = remnant_definitions.remnant_id
                                where remnant_definitions.name = "%s"
                                order by remnant_abilities.level""" % remnant_name)
        return self.cursor.fetchall()

    def get_remnant_definition_by_name(self, remnant_name):
        self.cursor.execute(""" select name, class_name, min_level, hp_base, speed_base,
                                power_base, evasion_base, spirit_base, crit_mult_min, crit_mult_max,
                                crit_chance, species, description
                                from remnant_definitions
                                where name = "%s"
                                """ % remnant_name)
        return self.cursor.fetchall()

    def get_remnant_definitions_by_type(self, remnant_types, rarity):
        query = """ select name, class_name, min_level, hp_base, speed_base,
                                power_base, evasion_base, spirit_base, crit_mult_min, crit_mult_max,
                                crit_chance, species, description
                                from remnant_definitions
                                inner JOIN remnant_types
                                on remnant_definitions.remnant_id = remnant_types.remnant_id
                                INNER JOIN remnant_rarity
                                on remnant_definitions.remnant_id = remnant_rarity.remnant_id
                                where remnant_rarity.rarity = %d
                                """ % rarity
        type_query = []
        if type(remnant_types) is list:
            for rtype in remnant_types:
                type_query .append("remnant_type = %d" % rtype)
        else:
            type_query.append("remnant_type = %d" % remnant_types)

        query += 'and (%s)' % ' or '.join(type_query)

        self.cursor.execute(query)

        return self.cursor.fetchall()

    def get_remnant_types(self, remnant_id):
        self.cursor.execute(""" select remnant_type from remnant_types
                                where remnant_id = %d
                            """ % remnant_id)
        return self.cursor.fetchall()

    def get_remnant_abilities(self, remnant_id):
        self.cursor.execute(""" select abilities.name, abilities.description, abilities.power, abilities.class_name,
                                abilities.speed, abilities.special_modifier, remnant_abilities.level
                                from remnant_abilities
                                inner join abilities
                                on abilities.ability_id = remnant_abilities.ability_id
                                where remnant_abilities.remnant_id = %d
                                order by remnant_abilities.level
                            """ % remnant_id)
        return self.cursor.fetchall()

if __name__ == '__main__':
    d = DatabaseLoginInfo('../remnant.db')

    sql = SqliteController(d)
    print(sql.list_all_tables())
    print(sql.list_all_columns("remnant_rarity"))
    print(sql.list_all_remnant())
    print()
    for ability in sql.get_all_abilities_of_remnant('Fire Dragon'):
        print(ability)
    print()
    print(sql.get_remnant_definition_by_name('Fire Dragon'))
    print()
    for i in sql.get_remnant_abilities(1):
        print(i)

    print('definitions')
    print(sql.get_remnant_definitions_by_type([1, 2], 1))
    print(sql.get_remnant_types(1))

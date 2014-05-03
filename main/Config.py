__author__ = 'kosttek'


class Config():

    username = None
    password = None
    databasename = None
    tables = None
    # state_values = None
    # point_values = None

    @staticmethod
    def load_config(configclass):
        Config.username = configclass.username
        Config.password = configclass.password
        Config.databasename = configclass.databasename
        Config.tables = configclass.tables
        # Config.state_values = configclass.state_values
        # Config.point_values = configclass.point_values
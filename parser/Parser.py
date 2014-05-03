__author__ = 'kosttek'
from parser_classes import *


class Parser():
    parsers_implementations = [
        ApplicationHistoryParser,
        NetworkParser,
        NetworkTrafficParser,
        ScreenParser,
        WeatherParser
    ]

    def __init__(self):
        self.table_parser_dict = self._create_table_parser_dict()

    def parse_event(self, event):
        tablename = event['table'].name
        parser = self.table_parser_dict.get(tablename, None)
        if parser is None:
            return dict()     # empty dict
        result = parser().parse(event['values'])
        return result

    def _create_table_parser_dict(self):
        result = dict()
        for parser in self.parsers_implementations:
            result[parser.table] = parser
        return result
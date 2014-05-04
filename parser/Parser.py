__author__ = 'kosttek'

from datamodel.learinigsetelement import LearningSetElement

class Parser():
    #todo
    # parsers_implementations = [
    #     ApplicationHistoryParser,
    #     NetworkParser,
    #     NetworkTrafficParser,
    #     ScreenParser,
    #     WeatherParser
    # ]

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
        parser_set = set()
        for type in LearningSetElement.attributes:
            if type.parser is not None:
                parser_set.add(type.parser)

        for parser in parser_set:
            result[parser.table] = parser
        return result
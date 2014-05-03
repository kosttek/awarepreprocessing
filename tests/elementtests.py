__author__ = 'kosttek'

from copy import deepcopy
import unittest
from datamodel import LearningSetElement, UpdateElement, ParserDict, Network


class TestTypes(unittest.TestCase):
    def setUp(self):
        pass

    def test_copy_element(self):
        le1 = LearningSetElement()
        le1.get_screen().set_value(1)
        le2 = deepcopy(le1)
        le2.get_screen().set_value(2)

        self.assertEqual(le1.get_screen().get_value(),1)
        self.assertEqual(le2.get_screen().get_value(),2)

    def test_update_element(self):
        le1 = LearningSetElement()
        parsed_event = dict()
        parsed_event[ParserDict.network]="WIFI"
        UpdateElement.update(le1, parsed_event)
        self.assertEqual("WIFI" in Network.values_set, True)



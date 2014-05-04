__author__ = 'kosttek'
import unittest
from datamodel.types import Time, Screen

class TestTypes(unittest.TestCase):
    def setUp(self):
        pass

    def test_types(self):
        time = Time()
        t_v = "time_val"
        time.add_to_value_set(t_v)


        screen = Screen()
        sc_v = "screen_value"
        screen.add_to_value_set(sc_v)

        screen2 = Screen()
        sc_v2 = "screen_value2"
        screen2.add_to_value_set(sc_v2)


        self.assertEqual(len(time.values_set),1)
        self.assertEqual(len(Screen.values_set),2)

        self.assertEqual(t_v in time.values_set,True)
        self.assertEqual(sc_v in screen.values_set,True)
        self.assertEqual(sc_v2 in screen.values_set,True)

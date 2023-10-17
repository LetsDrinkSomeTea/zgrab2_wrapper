import unittest
from modules.zgrab2 import Zgrab2, Zgrab2Config


class MyTestCase(unittest.TestCase):
    def all_moduls_loaded(self):
        Zgrab2Config.path = r'./zgrab2/zgrab2'
        Zgrab2Config.verbose = True

        zgrab2 = Zgrab2('google.com')

        zgrab2.start_scan()
        self.assertEqual(zgrab2.get_count_running()[1], len(zgrab2.modules))
        while zgrab2.is_running():
            pass
        self.assertEqual(zgrab2.get_count_running()[1], 0)
        self.assertEqual(len(zgrab2.get_results()), len(zgrab2.modules))


if __name__ == '__main__':
    unittest.main()

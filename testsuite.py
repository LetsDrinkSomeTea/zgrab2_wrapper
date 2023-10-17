import unittest
from modules.zgrab2 import Zgrab2, Zgrab2Config


class TestZgrab2Wrapper(unittest.TestCase):
    def test_all_modules_loaded(self):
        Zgrab2Config.path = r'./zgrab2/zgrab2'
        Zgrab2Config.verbose = True

        zgrab2 = Zgrab2('google.com')

        zgrab2.start_scan()
        # Alle Module wurden gestartet
        self.assertEqual(zgrab2.get_count_running()[1], len(zgrab2.modules))
        while zgrab2.is_running():
            self.assertNotEqual(zgrab2.get_count_running()[0], 0)
            pass
        # Alle Module wurden beendet
        self.assertEqual(zgrab2.get_count_running()[0], 0)
        # Alle Module haben Ergebnisse
        self.assertEqual(len(zgrab2.get_results()), len(zgrab2.modules))


if __name__ == '__main__':
    unittest.main()

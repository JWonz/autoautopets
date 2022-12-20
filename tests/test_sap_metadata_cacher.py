import unittest
from sap_metadata_cacher import read_most_recent_json


class TestReadMostRecentJson(unittest.TestCase):
    def test_empty_directory(self):
        # Test reading from an empty directory
        result = read_most_recent_json('./test_data/empty/')
        self.assertIsNone(result)

    def test_single_file(self):
        # Test reading from a directory with a single file
        result = read_most_recent_json('./test_data/single_file/')
        self.assertEqual(result, 'This is the only file')

    def test_multiple_files(self):
        # Test reading from a directory with multiple files
        result = read_most_recent_json('./test_data/multiple_files/')
        self.assertEqual(result, 'This is the most recent file')


if __name__ == '__main__':
    unittest.main()

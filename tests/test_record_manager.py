"""
CST8002 - Programming Language Research Project
Practical Project Part 2 - Project Review I
Professor: Stanley Pieda
Due Date: February 22, 2026
Student: Rakiba Chowdhury
Section: 020

This module contains a unit test for the RecordManager class.
It tests that adding a new record to the in-memory data structure
works correctly using Python's built-in unittest framework.

References:
[1] Python Software Foundation, "unittest - Unit testing framework,"
    Python 3.12 Documentation. [Online]. Available:
    https://docs.python.org/3/library/unittest.html
    [Accessed Feb. 15, 2026]
"""

import unittest
import sys
import os

# Add parent directory to path so we can import project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from business.record_manager import RecordManager

STUDENT_NAME = "Rakiba Chowdhury"

class TestRecordManagerCreate(unittest.TestCase):
    """
    Unit test class for testing the create_record method of the RecordManager 
    class.
    """

    def setUp(self):
        """
        Set up a fresh recordManager instance before each test.
        """
        self.manager = RecordManager()

    def test_create_record_adds_to_list(self):
        """
        Test that creating a new record adds it to the in-memory list.

        Verifies that:
        - The record count increases by 1 after creating a record.
        - The new record's fields match the values passed in.
        """
        # Arrange: check list starts empty
        initial_count = self.manager.get_record_count()

        # Act: create a new record
        new_record = self.manager.create_record(
            visit_date="15/02/2026",
            site_identification=99,
            species="Haematopus bachmani",
            total_black_oystercatcher_adults=5
        )

        # Assert: list has one more record
        self.assertEqual(
            self.manager.get_record_count(),
            initial_count + 1,
            "Record count should increase by 1 after creating a record"
        )

        # Assert: the new record has the correct values
        self.assertEqual(new_record.visit_date, "15/02/2026")
        self.assertEqual(new_record.site_identification, 99)
        self.assertEqual(new_record.species, "Haematopus bachmani")
        self.assertEqual(new_record.total_black_oystercatcher_adults, 5)

        print(f"\n  Test passed!  (Program by {STUDENT_NAME})")

if __name__ == "__main__":
    print(f"Running unit tests - Program by {STUDENT_NAME}")
    print("=" * 60)
    unittest.main(verbosity=2)
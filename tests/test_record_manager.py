"""
CST8002 - Programming Language Research Project
Practical Project Part 2 - Project Review I
Professor: Stanley Pieda
Due Date: February 22, 2026
Student: Rakiba Chowdhury
Section: 020

This module contains a unit test for the RecordManager class.
It tests that adding a new record to the in-memory data structure
works correctly using the pytest framework.

References:
[1] pytest development team, "pytest: helps you write better programs,"
    pytest.org. [Online]. Available: https://docs.pytest.org/en/stable/
    [Accessed Feb. 15, 2026]
"""

import sys
import os

# Add parent directory to path so we can import project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from business.record_manager import RecordManager

STUDENT_NAME = "Rakiba Chowdhury"


def test_create_record_adds_to_list():
    """
    Test that creating a new record adds it to the in-memory list.

    Verifies that:
    - The record count increases by 1 after creating a record.
    - The new record's fields match the values passed in.
    """
    # Arrange
    manager = RecordManager()
    initial_count = manager.get_record_count()

    # Act
    new_record = manager.create_record(
        visit_date="15/02/2026",
        site_identification=99,
        species="Haematopus bachmani",
        total_black_oystercatcher_adults=5
    )

    # Assert
    assert manager.get_record_count() == initial_count + 1
    assert new_record.visit_date == "15/02/2026"
    assert new_record.site_identification == 99
    assert new_record.species == "Haematopus bachmani"
    assert new_record.total_black_oystercatcher_adults == 5

    print(f"\n  Test passed! (Program by {STUDENT_NAME})")


if __name__ == "__main__":
    import pytest

    print(f"Running unit tests - Program by {STUDENT_NAME}")
    print("=" * 60)
    pytest.main([__file__, "-v"])
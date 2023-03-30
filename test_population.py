import pytest
from main import get_population_changes


@pytest.fixture
def population_data():
    return "population_test.txt"


def test_get_population_changes(population_data):
    expected_results = [
        ("Ukraine", 2020, 2021, -100000),
        ("USA", 2020, 2021, 4000000)
    ]
    assert get_population_changes(population_data) == expected_results


pytest.main(["-v", "--html=report.html"])

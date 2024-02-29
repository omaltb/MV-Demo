import pytest
from helpers import read_csv

def test_read_csv():
    #Arrange #Act #Assert
    filename = 'stock_data.csv'
    expected_type = list #pd.DataFrame

    data = read_csv(filename)
    actual_type = type(data)

    assert actual_type == expected_type 
import pytest
from revisit_testing import get_driver_information




def test_get_driver_information():
    assert get_driver_information(300,12,3.12) == 'The total cost of your trip is €78.00'
    
    with pytest.raises(ZeroDivisionError):
        1/0


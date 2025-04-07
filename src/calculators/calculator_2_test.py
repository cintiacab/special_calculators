from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)
    print()
    print(response)

    assert isinstance(response, dict) 
    assert response == {'data': {'Calculator': 2, 'result': (0.33)}}   

# Integration between NumpyHandler and Calculator2 (not a single test)
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)
    print()
    print(response)

    assert isinstance(response, dict) 
    assert response == {'data': {'Calculator': 2, 'result': (0.08)}}
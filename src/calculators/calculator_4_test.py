from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4 # type: ignore

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def average(self, numbers: List[float]) -> float:
        return 3.8956742        

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_4 = Calculator4(MockDriverHandler())
    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'result': 3.896}}

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"anything": [1, 2, 3, 4, 5]})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as exinfo:
        calculator_4.calculate(mock_request)
    assert str(exinfo.value) == "Body mal formatado"



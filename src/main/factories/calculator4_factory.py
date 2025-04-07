from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_4 import Calculator4 # type: ignore

def calculator4_factory():
    driver = NumpyHandler()
    calc = Calculator4(driver)
    return calc
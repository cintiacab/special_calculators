from typing import Dict, List
from flask import request as FlaskResquest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError # type: ignore

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskResquest) -> Dict: # type: ignore
            body = request.json
            input_data = self.__validate_body(body)
            average = self.__calculate_average(input_data)
            formated_response = self.__format_response(average)
            return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_average(self, numbers: List[float]) -> List[float]:
        average = self.__driver_handler.average(numbers)
        return average

    def __format_response(self, average: float) -> float:
       return {
                "data" : {
                    "Calculator": 4,
                    "result" : round (average, 3)
                }
            }
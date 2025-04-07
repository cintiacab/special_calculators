from typing import Dict
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process = self.__first_process(splited_number)
        second_process = self.__second_process(splited_number)
        third_process: float = splited_number

        calc_1 = first_process + second_process + third_process
        result = self.__format_response(calc_1)
        return result

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado")
        
        input_data = body["number"]
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.275
        return second_part
    
    def __second_process(self, second_number: float) -> float:
        first_part = (second_number ** 2.121) / 5
        second_part = first_part + 1
        return second_part
    
    def __format_response(self, calc_1: float) -> Dict:
        return{
              "data" : {
                  "Calculator" : 1,
                  "result" : round (calc_1, 2)
              }
        }


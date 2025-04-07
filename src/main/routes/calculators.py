from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1
from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = Calculator1()
    result = calc.calculate(request)
    return jsonify(result)

@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_2():
    driver = NumpyHandler()
    calc = Calculator2(driver)
    result = calc.calculate(request)
    return jsonify(result)
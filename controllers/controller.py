from flask import render_template
from app import app
from modules.calculator import Calculator

calculator = Calculator()

@app.route("/add/<num1>/<num2>")
def add_result(num1, num2):
    result = calculator.add(num1, num2)
    return render_template("calculator_result.html", title="Addition result", answer=result)

@app.route("/subtract/<num1>/<num2>")
def subtract_result(num1, num2):
    result = calculator.subtract(num1, num2)
    return render_template("calculator_result.html", title="Subtraction result", answer=calculator.subtract(num1, num2))

@app.route("/multiply/<num1>/<num2>")
def multiply_result(num1, num2):
    result = calculator.multiply(num1, num2)
    return render_template("calculator_result.html", title="Multiplication result", answer=calculator.multiply(num1, num2))

@app.route("/divide/<num1>/<num2>")
def divide_result(num1, num2):
    result = calculator.divide(num1, num2)
    return render_template("calculator_result.html", title="Division result", answer=calculator.divide(num1, num2))

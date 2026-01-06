from flask import Blueprint, request, jsonify, abort
import math
from . import errors as err
bp = Blueprint("maths", __name__)

def is_prime(n): 
    if n <= 1: # https://www.geeksforgeeks.org/python/python-program-to-check-whether-a-number-is-prime-or-not/
        return False
    else:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
        return prime
    
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
@bp.route("/math/factorial", methods=["GET"])
def factorial():
    num = request.args.get("number", "")
    if not num:
        return err.missingArgs("number")
    elif not num.isdigit():
        return err.invalidArg("number", "positive integer")
    num = int(num)
    return jsonify({
        "original": num,
        "factorial": math.factorial(num)
    })
    
@bp.route("/math/is_prime", methods=["GET"])
def isprime():
    num = request.args.get("number", "")
    if not num:
        return err.missingArgs("number")
    elif not is_int(number):
        return err.invalidArg("number", "integer")
    return jsonify({
        "original": num,
        "prime": is_prime(num)
    })
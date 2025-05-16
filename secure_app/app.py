from flask import Flask, request, jsonify
import os
import ast
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY", "default_secret")

def is_valid_ip(ip):
    return re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ip) is not None

@app.route("/")
def index():
    return "Secure Microservice Application"

@app.route("/ping")
def ping():
    ip = request.args.get("ip", "")
    if not is_valid_ip(ip):
        return jsonify({"error": "Invalid IP"}), 400
    response = os.popen(f"ping -c 1 {ip}").read()
    return jsonify({"response": response})

@app.route("/calculate")
def calculate():
    expr = request.args.get("expr", "")
    try:
        result = ast.literal_eval(expr)
        return jsonify({"result": result})
    except Exception:
        return jsonify({"error": "Invalid expression"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

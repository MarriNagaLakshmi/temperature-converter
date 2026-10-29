from flask import Flask, request, jsonify

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route('/convert/c-to-f', methods=['GET'])
def convert_c_to_f():
    try:
        c = float(request.args.get('celsius', 0))
        return jsonify({"celsius": c, "fahrenheit": celsius_to_fahrenheit(c)})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

@app.route('/convert/f-to-c', methods=['GET'])
def convert_f_to_c():
    try:
        f = float(request.args.get('fahrenheit', 0))
        return jsonify({"fahrenheit": f, "celsius": fahrenheit_to_celsius(f)})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

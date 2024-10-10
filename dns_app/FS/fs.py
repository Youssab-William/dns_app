from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    data = request.json
    hostname = data['hostname']
    ip = data['ip']
    as_ip = data['as_ip']
    as_port = int(data['as_port'])

    # Register with AS
    dns_register = f"TYPE=A\nNAME={hostname}\nVALUE={ip}\nTTL=10\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(dns_register.encode(), (as_ip, as_port))

    return "Registered successfully", 201

@app.route('/fibonacci')
def fibonacci():
    number = request.args.get('number')
    try:
        n = int(number)
        result = calculate_fibonacci(n)
        return str(result), 200
    except ValueError:
        return "Bad Request", 400

def calculate_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
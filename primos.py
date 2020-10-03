import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():
    final = 100
    p = 1
    numero = 3
    primos = "2,"

    while p < final:
        primo_sim = 1
        for i in range(2, numero):
            if numero % i ==0:
                primo_sim = 0
                break
        if (primo_sim):
            primos = primos + str(numero) + ","
            p += 1
            if p % 10 == 0:
                primos = primos + "<br>"
        numero+=1
    return primos
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
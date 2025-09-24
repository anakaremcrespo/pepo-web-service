import os
from flask import Flask, jsonify

app = Flask(__name__)

# Ruta principal: HTML bonito
@app.route("/")
def hola_html():
    return """
    <html>
        <head>
            <title>Pepo Web Service</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    text-align: center;
                }
                h1 {
                    color: #2e8b57;
                    font-size: 36px;
                    margin: 0;
                }
                p {
                    color: #333;
                    font-size: 24px;
                    margin: 10px 0 0 0;
                }
                a {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #2e8b57;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-size: 18px;
                }
                a:hover {
                    background-color: #246b45;
                }
            </style>
        </head>
        <body>
            <div>
                <h1>Hola Mundo, bienvenido a Pepo Web Service</h1>
                <p>Ana Karem Crespo López</p>
                <a href="/json">Ver JSON</a>
            </div>
        </body>
    </html>
    """

# Ruta JSON
@app.route("/json")
def hola_json():
    return jsonify({
        "mensaje": "Hola Mundo, bienvenido a Pepo Web Service",
        "nombre": "Ana Karem Crespo López"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
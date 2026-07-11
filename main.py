from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return (f"CoffeeBlanket is alive ☕")

@app.route("/about")
def about():
    return (f"This is About page")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
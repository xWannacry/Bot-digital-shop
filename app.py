from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def Home():
  return render_template("index.html")


@app.route('/login')
def login():
  return render_template("login.html")


@app.route('/signup')
def signup():
  return render_template("signup.html")


@app.route('/pricing')
def pricing():
  return render_template("pricing.html")


@app.route('/services')
def services():
  return render_template("services.html")


@app.route('/shopping-cart')
def shopping_cart():
  return render_template("shopping-cart.html")


@app.route('/products')
def products():
  return render_template("products.html")


@app.route('/product')
def product():
  return render_template("product.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

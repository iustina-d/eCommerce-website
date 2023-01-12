from flask import Flask,render_template, request, session, redirect, url_for
import os
import data_manager

app = Flask(__name__)
app.secret_key = "aegsrg-wr+a7 na7"

UPLOAD_FOLDER = (
  os.getenv("UPLOAD_FOLDER") if "UPLOAD_FOLDER" in os.environ else "images"
)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def main():
  first_6_books = data_manager.get_first_6_books()
  return render_template("home.html",books=first_6_books,page=1)

@app.route("/<int:page>")
def display_books(page):
  page = (page -1) *6
  get_books = data_manager.get_books_on_page(page)
  return render_template("home.html",books=get_books,page=page)


@app.route("/search_bar",methods=["POST"])
def display_search_bar_result():
  text = request.form.get("myInput")
  get_books = data_manager.get_books_using_search_box(text)
  return render_template("seach_bar_result.html",books=get_books)

@app.route("/sign-up")
def registrate():
  return render_template("sign_up.html")

@app.route("/login",methods=["GET","POST"])
def log_in():
  return render_template("log_in.html")

@app.route("/user_page",methods=["POST"])
def user_page():
  return render_template("user_page.html")

@app.route("/cart")
def display_cart_content():
  return render_template("cart.html")

@app.route("/card")
def card():
  return render_template("card.html")

@app.route("/search_gen",methods=["POST"])
def display_search_gen():
  return render_template("user_page.html")


@app.route("/product",methods=["POST"])
def display_product():
  return render_template("user_page.html")









if __name__ == "__main__":
    app.run(debug=True)
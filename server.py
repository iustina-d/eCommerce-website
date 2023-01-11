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
  get_books = data_manager.get_books()
  return render_template("home.html",books=get_books)

@app.route("/<page>")
def get_books_using_page_number(page):
  page = int(page)
  get_books = data_manager.get_books_on_page(page)
  return render_template("home.html",books=get_books,page=page)

@app.route("/search-bar" ,methods=["POST"])
def get_books_sing_search_bar():
  text = request.form.get("myInput")
  # text = input.capitalize()
  # text = str(text)
  get_books = data_manager.get_books_using_search_box(text)
  return render_template("home.html",books=get_books)

if __name__ == "__main__":
    app.run(debug=True)
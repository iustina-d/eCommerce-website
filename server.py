from flask import Flask,render_template,session
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



if __name__ == "__main__":
    app.run(debug=True)
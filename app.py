from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return render_template("index.html")

@app.route("/cv-olustur")
def cv_olustur():
    return render_template("cv-olustur.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
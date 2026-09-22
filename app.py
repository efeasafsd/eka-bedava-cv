from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return render_template("index.html")

@app.route("/cv-olustur")
def cv_olustur():
    return render_template("cv-olustur.html")

@app.route("/google790c84f256f4f866.html")
def google_verification():
    return Response(
        "google-site-verification: google790c84f256f4f866.html",
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

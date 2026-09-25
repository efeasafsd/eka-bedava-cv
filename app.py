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

@app.route("/robots.txt")
def robots():
    return Response(
        """User-agent: Google-InspectionTool
Allow: /

User-agent: *
Allow: /

Sitemap: https://eka-bedava-cv.onrender.com/sitemap.xml
""",
        mimetype="text/plain"
    )

@app.route("/sitemap.xml")
def sitemap():
    return Response(
        """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://eka-bedava-cv.onrender.com/</loc>
  </url>
  <url>
    <loc>https://eka-bedava-cv.onrender.com/cv-olustur</loc>
  </url>
</urlset>""",
        mimetype="application/xml"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

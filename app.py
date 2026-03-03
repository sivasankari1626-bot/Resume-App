from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/choose", methods=["POST"])
def choose():
    data = request.form.to_dict()

    photo = request.files.get("photo")
    if photo and photo.filename != "":
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
        photo.save(photo_path)
        data["photo"] = photo.filename
    else:
        data["photo"] = ""

    return render_template("choose_template.html", data=data)

@app.route("/generate")
def generate():

    theme_colors = {
        "emerald": ("#2ecc71", "#a9dfbf"),
        "pastel": ("#d7bde2", "#d5d8dc"),
        "ocean": ("#1f618d", "#76d7ea"),
        "midnight": ("#1b2631", "#bdc3c7"),
        "mustard": ("#c49a00", "#f8f1e7"),
        "teal": ("#16a085", "#7fdbff"),
        "olive": ("#556b2f", "#ffffff"),
        "navy": ("#1e3a8a", "#87ceeb"),
        "coffee": ("#6f4e37", "#fffdd0"),
        "royal": ("#6a0dad", "#e6e6fa"),
        "rose": ("#ff66b2", "#fff0f5"),
        "forest": ("#228b22", "#98ff98"),
        "sunset": ("#ff8c00", "#ffd1a9")
    }

    data = request.args.to_dict()
    theme = data.get("theme", "emerald")

    primary, secondary = theme_colors.get(theme, theme_colors["emerald"])

    return render_template("resume.html",
                           data=data,
                           primary=primary,
                           secondary=secondary)

if __name__ == "__main__":
    app.run(debug=True)
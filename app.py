from flask import Flask, render_template, request
#here the modules are being imported
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home(): #the function home for the prediction logic
    prediction = ""

    if request.method == "POST":
        cases = int(request.form["cases"])
        prediction = int(cases * 1.2)  # simple prediction logic

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

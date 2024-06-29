from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def calc():
    if request.method == "POST":
        first  = int(request.form["first"])
        second = int(request.form["second"])
        result = first + second 
    else:
        first, second, result  = 0, 0, 0
    return render_template(
            'calc.html', first = first,
            second = second,
            result = result)
    
app.run(debug=True)
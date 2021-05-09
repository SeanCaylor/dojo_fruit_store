from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    fname = request.form['first_name']
    lname = request.form['last_name']
    student_id = request.form['student_id']
    count = int(strawberry) + int(raspberry) + int(apple)
    print(f"Charging {fname} {lname} for {count} fruits")

    return render_template("checkout.html", strawberry = strawberry, raspberry = raspberry, apple = apple, fname = fname, lname = lname, student_id = student_id, count = count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
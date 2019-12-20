from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    scritta="Ciao mondo!"
    return render_template("base.html", testo =scritta)

@app.route('/info')
def info():
    scritta="Informazioni"
    return render_template("base.html", testo=scritta)

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    titolo="Pagina Iniziale"
    testo="Benvenuto sul sito di Vexteer"
    bottone="Più info"
    return render_template("base.html", 
            titolo=titolo,
            testo=testo,
            bottone=bottone)

@app.route('/info')
def info():
    titolo="Pagina Info"
    testo="Informazioni"
    bottone="Homepage"
    return render_template("base.html", 
            titolo=titolo,
            testo=testo,
            bottone=bottone)


if __name__ == '__main__':
    app.run()

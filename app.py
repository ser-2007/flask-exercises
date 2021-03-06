from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def aws():
    return '<h1>Clarusway AWS</>'

@app.route('/index')
def index():
    site = "Wellcome.."
    return render_template('index.html', message=site)

@app.route('/iletisim')
def iletisim():
    telno = ["Ankara = 031245554478", "Istanbul = 0212545878559"]
    return render_template('iletisim.html', object=telno)
@app.route('/hata')
def hata():
    return '<h1> Aradiginiz sayfa bulunamamaktadir</h1>'

if __name__ == ("__main__"):
    app.run(debug=True)
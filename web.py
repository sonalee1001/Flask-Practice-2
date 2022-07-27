from flask import Flask, redirect,url_for,render_template
app = Flask(__name__)
@app.route('/user/<name>')
def name():
    return 'hello soma'

@app.route('/Home')
def Home():
    return render_template('in.html')

@app.route('/login')
def login():
    return render_template('lg.html')

@app.route('/logout')
def logout():
    return redirect(url_for('Home'))

if __name__=="__main__":
 app.run(debug=True)

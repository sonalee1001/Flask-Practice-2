from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/admin')
def admin():
    return 'hello admin'

@app.route('/guest/<guest>')
def guest(guest):
    return 'hello %s as guest '%guest

@app.route('/user/<name>')
def name():
    if name=='admin':
        return redirect(url_for("hello admin"))
    else:
        return redirect(url_for("hello guest",guest=name))


if __name__=="__main__":
    app.run(debug=True)

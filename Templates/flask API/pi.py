from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/soma')
def soma():
    return 'hello '
def sum(a,b):
    return a+b
def avg(a,b):
    return a+b/2 
@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum=0
    order=len(str(n))
    copy=n
    while(n>0):
        digit=n%10
        sum+=digit**order
        n=n/10
    if(sum==copy):
        print(f"{copy} is an armstrong number")
        result={'number':copy,
               'armstrong':True,
                'server ip':'12.66.789'
            }
    else:
        print(f"{copy} is not an armstrong number")
        result={'number':copy,
               'armstrong':False,
                'server ip':'12.66.789'
            }
    return jsonify(result)
    

if __name__=="__main__":
    app.run(debug=True)

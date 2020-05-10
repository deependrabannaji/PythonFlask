from flask import Flask, render_template,url_for,request,redirect
import json

import config

app = Flask(__name__)
app.config.from_object('config')

def getjson():
    abc=None
    with open("db.json") as db:
        abc=json.load(db)

    return (abc)

def addjson(name,age):
    abc=None
    with open("db.json","r+") as dbs:
        newdt=json.load(dbs)
        print("here",type(newdt))
        newdt.append({"Name":name,"Age":age})
        dbs.seek(0)
        jsonobj=json.dumps(newdt)
        print(jsonobj)
        dbs.write(jsonobj)

@app.route('/', methods=["POST","GET"])
def index():
    data=None
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        addjson(name,age)
        return redirect('/')
        
    else:
        
        data=getjson()
        return render_template("index.html",value1=data)
        
    
    
    

if __name__=='__main__':
    app.run(debug=True)
from flask import Flask, session, redirect, render_template, request

app=Flask(__name__)

app.config['SECRET_KEY'] = 'jsu3cl3a87' 

@app.route("/")
def home():
    username = session.get('username')  # 取session
    if username:
        return redirect("/member/")
    else:
        return render_template("index.html")

@app.route("/signin",methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]
    
    if account=='test':
        if password =='test':
            session['username'] = account
            session['password'] = password
            return redirect("/member/")
        else:
            return redirect("/error/")
    else:
        return redirect("/error/")

@app.route("/member/")
def member():
    username = session.get('username')  # 取session
    if username:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error/")
def error():
    return render_template("error.html")

@app.route("/signout")
def signout():
    session.pop('username', None)
    return redirect("/")

if __name__=="__main__":
    app.run(port=3000)
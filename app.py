from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=("GET", "POST"))
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # print(request.url,  # 绝对路径
        #       request.path,  # 相对路径
        #       request.host)
        # print(request.values,
        #       request.args,  # get传参
        #       request.form,  # post传参
        #       request.data,
        #       request.json)
        usrename = request.form['username']
        password = request.form['password']

        return render_template("home.html",msg = usrename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

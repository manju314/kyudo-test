from flask import Flask, render_template,request, jsonify
import random, json
from opponents import opponents

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", opponents=opponents)

@app.route("/kanteki", methods=["GET", "POST"])
def kanteki():
    if request.method == "POST":
        opponent = request.form["opponent"]
        hit = int(request.form["hit"])
        if request.form.get("mode") == "on":
            mode = "on"
        else:
            mode = "off"


        res = ["○"]*24
        if hit != 24:
            count = 24 - hit
            num_list = []
            while count > 0:
                print(num_list)
                num = random.randint(0,23)
                if not num in num_list:
                    num_list.append(num)
                    res[num]="×"
                    count -= 1
            print(num_list)
        
        data = {
            "res": res,
            "mode": mode
        }

        def save_json(data):    
            with open('static/data.json', 'w', encoding='utf-8') as f:
                json.dump(data,f, indent=4, ensure_ascii=False)
        
        save_json(data)
        
        return render_template("kanteki.html", opponent=opponent, res=res, mode=mode)
    else:
        return render_template("index.html", opponents=opponents)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, session
import random, json, secrets, os
from flask_session import Session
from opponents import opponents

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
# if not app.secret_key:
#     raise ValueError("SECRET_KEY is not set")

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "data" not in session: 
        num_of_people = 4
        cell_num = num_of_people * 4
        num = random.randint(0, len(opponents)-1)
        opponent = opponents[num]
        print(opponent)
        lowHit = cell_num/2
        highHit = cell_num
        mode = "off"
    else:
        data = session.get("data")
        num_of_people = data["num_of_people"]
        cell_num = data["cell_num"]
        opponent = data["opponent"]
        lowHit = data["lowHit"]
        highHit = data["highHit"]
        mode = data["mode"]
        print(num_of_people)
    return render_template("index.html", opponents=opponents, num_of_people=num_of_people, cell_num=cell_num, opponent=opponent, lowHit=lowHit, highHit=highHit, mode=mode)

@app.route("/kanteki", methods=["GET", "POST"])
def kanteki():
    if request.method == "POST":
        opponent = request.form["opponent"]
        nop = int(request.form["NumOfPeople"])
        lowHit = int(request.form["lowHit"])
        highHit = request.form.get("highHit")
        if not highHit is None:
            highHit = int(highHit)
        else:
            print("None")
            # highHit = 16

        if request.form.get("mode") == "on":
            mode = "on"
        else:
            mode = "off"

        cell_num = nop*4
        res = ["○"]*(cell_num)
        hit = random.randint(lowHit, highHit)
        if hit != cell_num:
            count = cell_num - hit
            num_list = []
            while count > 0:
                print(num_list)
                num = random.randint(0,cell_num-1)
                if not num in num_list:
                    num_list.append(num)
                    res[num]="×"
                    count -= 1
            print(num_list)
        
        data = {
            "opponent": opponent,
            "num_of_people": nop,
            "cell_num": cell_num,
            "lowHit": lowHit,
            "highHit": highHit,
            "mode": mode
        }

        session["data"] = data
        print(session)

        mode_data = {
            "mode": mode
        }

        def save_json(data):    
            with open('static/mode.json', 'w', encoding='utf-8') as f:
                json.dump(data,f, indent=4, ensure_ascii=False)
        
        save_json(mode_data)

        return render_template("kanteki.html", opponent=opponent, nop=nop, res=res, hit=hit)
    else:
        return render_template("index.html", opponents=opponents)
    
@app.route("/kyousya", methods=["GET", "POST"])
def kyousya():
    data = session.get("data")
    opponent = data["opponent"]
    nop = data["num_of_people"]
    maxHit = int(data["cell_num"]/2)

    minHit = int(maxHit/2)
    res = ["○"]*maxHit
    hit = random.randint(minHit, maxHit)
    if hit != 12:
        count = maxHit - hit
        num_list = []
        while count > 0:
            print(num_list)
            num = random.randint(0,maxHit-1)
            if not num in num_list:
                num_list.append(num)
                res[num]="×"
                count -= 1
        print(num_list)
    
    return render_template("kyousya.html", opponent=opponent, nop=nop, res=res, hit=hit)

@app.route("/kyousya2", methods=["GET", "POST"])
def kyousya2():
    data = session.get("data")
    opponent = data["opponent"]
    nop = data["num_of_people"]
    maxHit = int(data["cell_num"]/4)

    minHit = int(maxHit/2)
    res = ["○"]*maxHit
    hit = random.randint(minHit, maxHit)
    if hit != 12:
        count = maxHit - hit
        num_list = []
        while count > 0:
            print(num_list)
            num = random.randint(0,maxHit-1)
            if not num in num_list:
                num_list.append(num)
                res[num]="×"
                count -= 1
        print(num_list)
    
    return render_template("kyousya2.html", opponent=opponent, nop=nop, res=res, hit=hit)


if __name__ == "__main__":
    app.run(debug=True)
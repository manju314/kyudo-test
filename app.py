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
        if lowHit <= highHit:
            hit = random.randint(lowHit, highHit)
        else:
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

        def save_json(data):    
            with open('static/data.json', 'w', encoding='utf-8') as f:
                json.dump(data,f, indent=4, ensure_ascii=False)
        
        save_json(data)
        
        return render_template("kanteki.html", opponent=opponent, nop=nop, res=res, hit=hit)
    else:
        return render_template("index.html", opponents=opponents)
    
@app.route("/kyousya", methods=["GET", "POST"])
def kyousya():
    with open('./static/data.json') as f:
        d = json.load(f)
    opponent = d['opponent']
    nop = d["num_of_people"]
    maxHit = int(d["cell_num"]/2)

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
    with open('./static/data.json') as f:
        d = json.load(f)
    opponent = d['opponent']
    nop = d["num_of_people"]
    maxHit = int(d["cell_num"]/4)

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
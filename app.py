from flask import Flask, render_template,request
import random
from opponents import opponents

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", opponents=opponents)

@app.route("/kanteki", methods=["GET", "POST"])
def kanteki():
    def generate_table(rows=4, cols=6):
        table = [[0]*cols for _ in range(rows)]
        return table
    
    table = generate_table(4, 6)

    if request.method == "POST":
        opponent = request.form["opponent"]
        hit = int(request.form["hit"])

        res = ["◯"]*24
        if hit != 24:
            count = 24 - hit
            num_list = []
            while count > 0:
                print(num_list)
                num = random.randint(0,23)
                if not num in num_list:
                    num_list.append(num)
                    res[num]="X"
                    count -= 1
            print(num_list)

        # resIndex = 0
        # for r in range(4-1, -1, -1):          # 下の行 → 上の行
        #     for c in range(6-1, -1, -1):      # 右 → 左
        #         table[r][c] = res[resIndex]
        #         resIndex += 1
        
        return render_template("kanteki.html", opponent=opponent, res=res)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run()
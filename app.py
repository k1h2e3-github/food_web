from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/naver')
def naver():
    return render_template('index.html')

@app.route('/food')
def food():
    foodlist = ['삼겹살', '낙곱새', '연어덮밥', '피자', '돈까스']
    foodname = random.choice(foodlist)
    return render_template('food.html', data = foodname)  

if __name__ == '__main__':
    app.run()
    #app.run(host = "0.0.0.0", port=80)
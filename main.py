from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def RESTFUL():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        text = request.form['texts']     # request.form converts data to python dictionary already
        response = request.post(url="http://nameOfTheService:8010/backend")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

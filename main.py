from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])        # Allow the REST API endpoint to take in GET/POST request(s)
def RESTFUL():
    if request.method == 'GET':                 # [IMPORTANT] By default, when the client first enters the URL, he is in fact sending a GET request
        return render_template('index.html')

    elif request.method == 'POST':              # [IMPORTANT] A POST request will be triggered/sent to the rest API whenever a FORM (via html) is submitted
        response = request.post(url="http://backend-service:8010/")      # [SUPER IMPORTANT] This sends the request to ANOTHER REST API to carry out the processing
        return render_template('index.html', content=response.text)             # "response.text"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

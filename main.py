from flask import Flask, request, render_template
import requests
import pymongo

# Establish conenction to MongoDB and create a database + collection
client = pymongo.MongoClient('mongodb://localhost:27017')               # using "localhost" as we will be downloading MongoDB within the SAME container, and not a seperate deployment
# Creating a database and initializing an Object "db" for it
db = client['TEST-Database']
# Creating a collection
information = db.data_collection


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])        # Allow the REST API endpoint to take in GET/POST request(s)
def RESTFUL():
    if request.method == 'GET':                 # [IMPORTANT] By default, when the client first enters the URL, he is in fact sending a GET request
        return render_template('index.html')

    elif request.method == 'POST':              # [IMPORTANT] A POST request will be triggered/sent to the rest API whenever a FORM (via html) is submitted
        input_text = request.form['texts']
        data = {"data": input_text}
        response = requests.post(url="http://backend-service:6010/", json=data)      # [SUPER IMPORTANT] This sends the request to ANOTHER REST API to carry out the processing
        
        # Inserting Data into MongoDB Database via its collection
        record = [{
            "Type":"Text"
            "text":response.text                      # "response.text" extracts the text data from the REST API RESPONSE
        }]        
        information.insert_many(record)
        
        # Pulling/Retrieving Data from MongoDB Database via its collection
        texts=[]
        for x in information.find({"Type":"Text"}):
            text = x["text"]
            texts.append(text)
            
        return render_template('index.html', content=texts[len(texts)-1])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)

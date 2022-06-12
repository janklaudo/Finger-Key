
from flask import Flask,jsonify, request
import requests

app = Flask(__name__)


from Keys import Key

@app.route('/External', methods=['GET'])
def  ExternalAppi():
   url = "https://api.apilayer.com/exchangerates_data/convert?to=GBP&from=EUR&amount=5"
   payload = {}
   headers= {"apikey": "UKCeXybh6ET4Uo7TtcwUFv5TpWrUmtDi"}
   response = requests.request("GET", url, headers=headers, data = payload)
   status_code = response.status_code
   return response.text

@app.route('/ping', methods=['GET'])

def ping():
    return jsonify({"message":"pong"})

@app.route('/Keys',methods=['GET'])
def GetKeys():
    return jsonify({"Keys":Key})

@app.route('/Keys/<string:id>')
def GetKey(id):
    keyFound = [keys for keys in Key if keys['ID'] == id]
    if (len(keyFound)> 0):
       return  jsonify({"Key":keyFound[0]})
    return  jsonify({"Mensaje":"Key not found"})

@app.route('/Keys',methods=['POST'])
def Mattricular():
    newKey = {
        "name": request.json['name'],
        "key": request.json['key'],
        "ID": request.json['ID']
    }
    Key.append(newKey)
    return jsonify({"Mensaje":"Key agregada", "Keys": Key})


@app.route('/Keys/<string:id>',methods=['PUT'])
def UpdateKey(id):
    keyFound = [keys for keys in Key if keys['ID'] == id]
    if (len(keyFound)> 0):
        keyFound[0]['ID']= request.json['ID']
        keyFound[0]['name']= request.json['name']
        keyFound[0]['key']= request.json['key']
        return  jsonify({"Mensaje":"Key Update","Key":keyFound[0]})
    return  jsonify({"Mensaje":"Key not foud"})

@app.route('/Keys/<string:id>',methods=['DELETE'])
def DeleteKey(id):
    keyFound = [keys for keys in Key if keys['ID'] == id]
    if (len(keyFound)> 0):
        Key.remove(keyFound[0])      
        return  jsonify({"Mensaje":"Key Delete"})
    return  jsonify({"Mensaje":"Key not foud"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
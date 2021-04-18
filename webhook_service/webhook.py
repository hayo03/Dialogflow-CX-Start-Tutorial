import json
from flask import request, jsonify, make_response
from flask import Flask
from flask import Response
import requests

app = Flask(__name__)


@app.route('/my_webhook', methods=['POST'])
def post_webhook_dialogflow():
    body = request.get_json(silent=True)
    session_id = body['detectIntentResponseId']
    print(session_id)
    #The tag used to identify which fulfillment is being called.
    fulfillment = body['fulfillmentInfo']['tag']
    slots = []
    for key, value in body['sessionInfo']['parameters'].items():
        slots.append({'name':key,'value':value})
       
    print (slots)
    # msg = 'hi'
    msg = invoke_api(fulfillment, slots)
    return answer_webhook(msg, session_id)


def answer_webhook(msg, session_id):
    message= {"fulfillment_response": {
      
        "messages": [
        {
          "text": {
            "text": [msg]
          }
        }
      ]
    }
    }
    return Response(json.dumps(message), 200, mimetype='application/json')
#get API credential given API name and attribute 
def getAPI_credential(api_name, api_attribute):
    data = json.load (open('API_credentials.json',))
    return data[api_name][api_attribute]

def invoke_api(fulfillment, slots):
    print("\n\n\n\n\n=========> CALL API ",fulfillment)
    if fulfillment == "GetWeather_fulfillment":
        for slot in slots:
             if slot['name']=="city":
                 q=str(slot['value'])
        appid=getAPI_credential('api.openweathermap','appid')
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+q+'&appid='+appid
        result = requests.get(url)
        jsonResult = result.json()
        if result.status_code == 200:
            weatherCondition = jsonResult['weather'][0]['description']
            reply = "There is {} in there.".format(weatherCondition)
            print(reply)
            return reply
        else:
            return "Something wrong with the API."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)

#### minimal set of required modules
import json
from flask import Flask
from flask import Response, request
import requests


###create a web app using Flask
app = Flask(__name__)



### Define a Route 
@app.route('/my_webhook', methods=['POST'])

### Define the function that will be executed when the associated route is called
def post_webhook_dialogflow():
#1) Getting information from dialogflow agent request 
    body = request.get_json(silent=True)
#Get tag used to identify which fulfillment is being called.
    fulfillment = body['fulfillmentInfo']['tag']
#Get parameters that are required to handle the desired action
    prameters = []
    for key, value in body['sessionInfo']['parameters'].items():
         prameters.append({'name':key,'value':value})

#2) Execute action
    msg = invoke_action(fulfillment,  prameters)
#3) provide a webhook Response to the Dialogflow Agent
    WebhookResponse=answer_webhook(msg)
    return WebhookResponse

### Exploit parameters and incorporate them in the text response   
def invoke_action(fulfillment, prameters):
    print("\n\n\n\n\n=========> CALL API ",fulfillment)
    if fulfillment == "GetWeather_fulfillment":
        for prameter in prameters:
             if prameter['name']=="city":
                 city=str(prameter['value'])
        appid="25e5d7b2fff948d0749a8b9e9e14f5f9"
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+appid
        result = requests.get(url)
        jsonResult = result.json()
        if result.status_code == 200:
            weatherCondition = jsonResult['weather'][0]['description']
            reply = "There is {} in there.".format(weatherCondition)
            print(reply)
            return reply
        else:
            return "Something wrong with the API."

#### Processes the webhook answer which should follow a particular JSON format
def answer_webhook(msg):
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
### Run a webhook on localhost
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
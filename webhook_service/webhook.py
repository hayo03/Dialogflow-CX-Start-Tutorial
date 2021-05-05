#### minimal set of required modules
import json
from flask import Flask
from flask import Response, request
import requests


#### initialize a flask app for our webhook
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
def invoke_action(fulfillment,  prameters):
    print("\n\n\n\n\n=========> CALL ",fulfillment)
    if fulfillment == "GetWeather_fulfillment":
        city=str( prameters[0]['value'])
        msg="There are overcast clouds in "+city
        return msg

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

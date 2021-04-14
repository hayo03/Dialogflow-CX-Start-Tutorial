# Dialogflow-CX-Start-Tutorial (In progress)

### Content
- ##### [Introduction](#intro)
- ##### [Dialogflow CX Setup ](#Setup)
- ##### [Creating a simple welcome message](#welcomemessage)
- ##### [Managing Flows & Pages](#FlowsandPages)
- ##### [Reusing information between flows](#reuseinformatione)
- ##### [Building a webhook](#webhook)
- ##### [Testing the completed agent](#Testing)
- ##### [Conclusion](#conclu)


## <a name="intro"></a>Introduction
This guide shows how to use the Dialogflow CX Console to build and test a simple demo agent. When interacting with this agent, you can ask for getting the weather forecast information, search for a restaurant and make a table reservation. Your completed agent for this guide will be graphed by the console like the following:

## <a name="Setup"></a>Dialogflow CX Setup 
1. To use services provided by Google Cloud, you need to create a project using [Google Cloud Console](https://console.cloud.google.com/) and enable the Dialogflow API.
2. Using [DF-CX console](https://dialogflow.cloud.google.com/cx/projects), choose the project you just created and click Create agent.<br>
3. Complete the form for basic agent settings:<br>
   *You can choose any name.<br>
   *Select your preferred location. <br>
   *Select your preferred time zone.<br>
   *Select the default language for your agent.<br>
4. Click Save.<br> 

## <a name="welcomemessage "></a>Exploring the created agent 
The created agent has a default Start Flow with a start page that comes with default welcome intent. Withing this default setting, the agent can handle a basic conversation with only a welcome message. 

![tt](images/agent_default.png)

To test your new agent:
1. Click the Test Agent button to open the simulator.
2. Enter hello in the text entry and press enter.
3. The agent responds with a default welcome response.
4. Close the simulator 

To edit the welcome response message:
1. Click the Build tab.
2. Select the Default Start Flow in the Flows section.
3. Click the Start node in the graph. This is the start page for the Default Start Flow.
4. Find the intent route with the Default Welcome Intent as an intent requirement and click it. This opens a panel to edit the intent route information.
5. Find the fulfillment section and delete all response messages, then add "Hello, this is a demo virtual agent. How can I help you? as the only response".
6. Click Save and Close the intent route editing panel.
7. Test the updated welcome response message

## <a name="FlowsandPages"></a>Managing Flows & Pages
So far, the agent has one flow with the start page. In this section, we will add two flows that handle requests about the weather forecast and restaurant reservations. The design of these flows is like the following:

![tt](images/flows.svg)

<b> Weather forecast flow: </b> it is trriggred when users ask about weather forecast information in a given city. To create this flow: 

1.Click the Start node in the graph <br>
2.Click Routes add + button. The route editing panel opens.<br>
3. In the transition section, choose Flow option and select New flow and name it as "Weather forecast". <br>
4. Back to the Intent section, select New intent and create the following intent and enter its training phrases: <br>
<b> Intent: </b> weather.current <br>
<b> Training utterances:</b> [utterances.text] (https://github.com/hayo03/Dialogflow-CX-Start-Tutorial/blob/main/intents/SearchRestaurant.txt) <br>
4. Click Save <br>
As you notice city parameter is not detected automatically so we have to create it, but we need to first create its entity type "geo-city"
     <b> Parameter:</b> city<br>
     <b> Entity type:</b> geo-city<br>
5. Select the Manage tab and Click on Entity Types, click +Create, set the name to size geo-city, add some entity entries for the city (Paris, Lyon, Evry, ) and click Save<br>
6. Back to intents tab and slect "weather.current" intent. For each phrase that contains a city, annotate the city with a city parameter and the @geo-city custom entity type and  Click Save <br>





## <a name="reuseinformation"></a>Reusing information between flows
## <a name="webhook "></a>Building a webhook

## <a name="Testing"></a>Testing the completed agent

## <a name="conclu"></a>Conclusion



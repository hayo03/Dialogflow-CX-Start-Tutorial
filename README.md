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
   - You can choose any name.<br>
   - Select your preferred location. <br>
   - Select your preferred time zone.<br>
   - Select the default language for your agent.<br>
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

<b> Weather forecast flow: </b> allows users to ask about weather forecast information in a given city. Before building it, we need to create the intent that once matched, the flow will be called to handle the user request. <br>
<b>Create intent: </b>
1. Select the Manage tab.
2. Click Intents, click Create, enter weather.current as an intent name and enter the training phrases in [utterances.text](https://github.com/hayo03/Dialogflow-CX-Start-Tutorial/blob/main/intents/GetWeather.txt).
3. Click Save 

<b>Create entity types and parameters:</b> <br>
As you notice the city parameter is not detected automatically so we have to create it, but we need to first create its entity type "geo-city". <br>
  - <b> Parameter:</b> city<br>
  - <b> Entity type:</b> geo-city<br>
1. Select the Manage tab and Click on Entity Types, click +Create, set the name to size geo-city, add some entity entries for the city (Paris, Lyon, Evry, ) and click Save. <br>
2. Back to the Intents tab and select "weather.current" intent. For each phrase that contains a city, annotate the city with a city parameter and the @geo-city custom entity type and  Click Save.

<b>Create Flow : </b> 
1. Select the Build tab.
2. Click Flows, click Create, enter Weather forecast as an flow name. 

<b>Create Page : </b> <br>
Bu defaut, the Weather forecast flow has a special page named Start. When a flow initially becomes active, this page becomes the current, active page. A start page does not have parameters or responses messages like normal pages. So we need to create page that will collect city information from user and handle its request (i.e., provide answer to the user). <br>
 1. Click on "Start" page in Weather forecast flow 
 2. Click the add add button in the Pages section.
 3. Enter "Get current Weather" as a display name for the page.
 4. Click the settings more_vert button next to the page display name and select Edit.
 5. Create a new parameter:<br>
   - Parameter name: city<br>
   - Entity type: @geo-city<br>
   - Check "Required"<br>
   - Fulfillement (Agent says): What is your city name?<br>

<b> Create Routes: </b> <br> 
As you notice there is no link between different flows (i.e., Default Start Flow and Weather forecast Flow)  and the newly created page (get current weather). Without those links, the conversation between bot and user can not be handled. Therefore, Routes are introduced to define such links. We need to define three routes as follows: 
1. Create a Route that transitions from the default start flow to  Weather forecast flow. This route should be called when the end-user asks for weather forecast information. To create this route:  <br>
  - Select the Default Start Flow in the Flows section.
  - Click the Start node in the graph. 
  - Add the following intent route:
      - Intent: weather.current
      - Transition: choose Flow  and select “Weather forecast” flow
  - Click Save

2. Create a Route that transitions from the start page of the Weather forecast flow to get current weather page.  This route should be called when the intent “weather.current” is matched”. To create this route: <br> 
   - Select the Weather forecast” Flow in the Flows section.
   - Click the Start node in the graph. 
   - Add the following intent route:
       - Intent: weather.current
       - Transition: choose Page  and select “Get current weather” page
    - Click Save

3. Create a route that transitions from “get current weather page” to End Flow page: this route should be called when all parameters are fulfilled. To create this route: <br> 
   - Select the Weather forecast” Flow in the Flows section.
   - Click the Start node in the graph. 
   - Add the following intent route:
       - condition: $page.params.status="FINAL"
       - Fulfillement (What the Agent will aswer to the user):  There is clear sky in $session.params.city
       - Transition: choose Page  and select “End Flow” page
   - Click Save

Congratulations! Now you can test your agent to test whether your flow is correctly defined:

<b> Test the Weather forecast: </b><br>
1. Click the Test Agent button to open the simulator.<br>
2. Enter "What does the weather forecast look like?" and press enter.<br>
3. The agent will provides you the weather forecast information.<br>

## Exercice
Create and test the Restaurant reservation flow. [Here](https://github.com/hayo03/Dialogflow-CX-Start-Tutorial/tree/main/Exercice) we provide some guidance steps.
## <a name="reuseinformation"></a>Reusing information between flows
## <a name="webhook "></a>Building a webhook

## <a name="Testing"></a>Testing the completed agent

## <a name="conclu"></a>Conclusion



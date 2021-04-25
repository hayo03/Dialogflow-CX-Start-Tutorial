## Designing the Restaurant reservation flow 
After adding the design of the restaurant reservation flow, the whole agent design should be as follow: 

<p align="center">
  <img src="images/Restaurant-search-flow (1).png">
</p>

## Creating Restaurant reservation flow 
To create this flow, you will almost follow the steps taken for Weather forecast Flow. 
1. Create intent
   - Intent: restaurant.search
     - Utterances: [SearchRestaurant.txt](https://github.com/hayo03/Dialogflow-CX-Start-Tutorial/blob/main/intents/SearchRestaurant.txt).
     - Parameters: 
        - name: Location; Entity type: @sys.geo_city
        - name: food; Entity type: You have to create a new entity type and name it @food, where entity entries can be like Italian, Chinese, Turkish, Indian, Tunisian, etc.       
2. Create Flow named "Restaurant reservation flow"
3. Create a Route that transitions from the default start flow to Restaurant reservation flow. 
      - Intent: restaurant.search
      - Transition to the Flow: Restaurant reservation flow
4. Create Page named "Search restaurant" that will collect the location information where users search in and kind of food they prefer. 
    - Parameters: 
        - name: Location; Entity type: @sys.geo_city
        - name: food; Entity type: @food; 
5. Create a Route that transitions from the Restaurant reservation flow to Search restaurant page. 
      - Intent: restaurant.search
      - Transition to the Page: Search restaurant
6. Create a Route that transitions from the search restaurant page to EndFlow page. 
      - Condition: $page.params.status="FINAL"
      - Fulfillement:  This one serves $session.params.food food: Helow world Restaurant, Phone: +0000000, address : Helow world street, $session.params.location
      - Transition to the Page: End Flow


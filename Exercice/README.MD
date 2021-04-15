<b> Create Restaurant reservation flow (Exercice) </b> <br>
Restaurant reservation flow  allows users to search for restaurants and make reservations in a restaurant of their choice. To create this flow, you will almost follow the steps taken for Weather forecast Flow. 
1. Create intents 
   - Intent: restaurant.search
     - Utterances: [SearchRestaurant.txt](https://github.com/hayo03/Dialogflow-CX-Start-Tutorial/blob/main/intents/SearchRestaurant.txt).
     - Parameters: 
        - name: Location; Entity type: @geo_city
        - name: food; Entity type: @food; entity entries: Italian, Chinese, Turkish, Indian, Tunisian, etc.
   - Intent: restaurant.reservation.yes
     - Utterances: Yes, Sure, Yeah, 
   - Intent: restaurant.reservation.No
     - Utterances: No, not now, 
2. Create Flow named "Restaurant reservation flow"
3. Create a Route that transitions from the default start flow to Restaurant reservation flow. 
      - Intent: restaurant.search
      - Transition to the Flow: Restaurant reservation flow
2. Create Page named "Search restaurant" that will collect the location information where users search in and kind of food they prefer. 
    - Parameters: 
        - name: Location; Entity type: @geo_city
        - name: food; Entity type: @food; 
4. Create a Route that transitions from the Restaurant reservation flow to Search restaurant page. 
      - Intent: restaurant.search
      - Transition to the Page: Search restaurant
 5. Create Page named "Reservation" that will ask user if he/she whant to make a reservvation in restaurant:
      - Fulfulment: Would you like to make a reservation? 
 4. Create a Route that transitions from the search restaurant page to Reservation page. 
      - Condition: $page.params.status="FINAL"
      - Fulfillement:  This one serves $session.params.food food: Helow world Restaurant, Phone: +0000000, address : Helow world street, $session.params.location
      - Transition to the Page: Reservation
  5. Find by yourself the next steps toward complete the whole flow that should lead to a conversation like the following conversation example:
  ![tt](examples/reservation_conversation.pdf)

# Euro-Football-Project
Create, manage, and follow up each tournament using your own Tournament Model.

- Files starting with "top_level_..." are the speficic players' position creators. Set the skills a player needs and assign points or other category to their characteristics.

- team_factory.py consists of the building instance attributes, as well as functions to get other data such as points, yellow and red cards.

- game_factory.py - Game is the class that manages each games' statistics

- tournament_factory.py - this is the class that takes care of the table of the tournament

Each of the classes has its own "id" attribute in order to make the instances unique.

Check the requirements.txt file for the required libraries. Although the competition table can be printed as a multiline string,
numpy and pandas are imported as a next step tools to get some insights from the dataset.

Enjoy!

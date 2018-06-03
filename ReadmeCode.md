EZNutriPal Source code

In this code we are trying to calculate the nutrient values of the food items expressed in a sentence.

The EZNutriPal function accepts 5 inputs:

1. FN: is a list of food items in the sentence tagged by our Named Entity Recognition block
2. Size: is a list of portion sizes in the sentence tagged by our Named Entity Recognition block
3. Unit: is a list of unit of measurements such as pound, gram, etc.
4. Threshold: This is a value between 0 and 1 for putting a threshold on the similarity between the food item in the sentence and the items in the database.
5. raw: is the raw sentence expressed by the user

First it tries to locate the food items in the database.
Then it tries to map the information in the sentence to their associated food item.
The units expressed in the sentences should be converted to a form that is understandable by the database. Therefore we perform a unit matching.

Then nutrient calculator function is called by EZNutriPal. Using the extracted information different nutrient values are calculated such as calorie, ash, carb, etc.

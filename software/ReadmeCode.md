EZNutriPal Source code

The EZNutriPal function share here  aims to calculate the nutrient values of the food items expressed in an input sentence.

The function accepts five inputs:

FN: is a list of food items in the sentence tagged by our Named Entity Recognition block
Size: is a list of portion sizes in the sentence tagged by our Named Entity Recognition block
Unit: is a list of unit of measurements such as pound, gram, etc.
Threshold: This is a value between 0 and 1 for putting a threshold on the similarity between the food item in the sentence and the items in the database.
raw: is the raw sentence expressed by the user
First it tries to locate the food items in the database. Then it tries to map the information in the sentence to their associated food item. The units expressed in the sentences should be converted to a form that is understandable by the database. Therefore we perform a unit matching.

Then nutrient calculator function is called by EZNutriPal. Using the extracted information, different nutrient values are calculated such as calorie, ash, carb, etc.

# UNIT-PROJECT-1


## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use your coding skills in Python accurately.
- Organize Your Code into modules & (or packages)
- Use git & Github to track changes in your code.

## Example Project :  An online Grocery Store :

#### Overview : An online store that sells fruits to customers. This online store has 2 main users. The customer and the manager of the store . Each one of them should be able to do the following tasks for the store to function properly . 

### Features & User Stories
#### As a customer I should be able to do the following :
- Browse  Products . 
- View the product info (summary, specs, price, quantity , etc.)
- Search for Products.
- Get recommendations for my next purchase based on my purchase history.
- Add Products to the shopping cart .
- Remove a product from the shopping cart.
- List the products in my shopping cart. 
- Continue to checkout . 
- Fill in my address for delivery.
- Get receipt of my purchases.
- Check delivery status . 



#### Usage :
 Explain to the user how to use your project . 
 for example:
 - type in search product_name to search for a product.
 - type in list_products to show all the products in the grocery.
 - type in show product_name to get information about this product.
 - type in buy product_name to buy the product . 
 - and so on...


### For your project. Edit this README.md file to include your own project name,  overview, user stories, and usage. 

### NOTE: before submitting the final project, please do the following command:
`pip freeze > requirements.txt` to enable use to know & use the packages used in your project.



# 🎬 CINEQUIZ: The Ultimate Movie Trivia CLI

## Overview
A Python-based Command Line Interface (CLI) game that tests your movie knowledge using real-time data from the Open Trivia Database API.

## Features
- **Dynamic Questions:** Fetches 10 fresh movie questions every round.
- **Difficulty Selection:** Choose between Easy, Medium, and Hard.
- **Persistent Leaderboard:** Scores are saved to a JSON file and can be viewed from the main menu.
- **Smart Formatting:** Handles HTML characters (like quotes) for clean reading.

## How to Use
1. Run `python main.py`.
2. Select **[1]** to Play.
3. Enter your name and choose a difficulty.
4. Use **A, B, C, or D** to answer.
5. Select **[2]** from the main menu to see the Top 5 High Scores.

## Technical Skills Used
- **OOP:** Player class manages state and ranking logic.
- **API Integration:** Uses `requests` to fetch external data.
- **File I/O:** Saves and reads data using `json` and file `append` mode.
- **Decorators:** Custom `@game_banner` for UI consistency.
- **Error Handling:** Try/Except blocks for API calls and file reading.

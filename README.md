Test Automation - Python + Selenium Web Driver 27/05/2025

This project automates a search in Mercado Libre Mexico (https://www.mercadolibre.com.mx/) to print the Name and Price of the first 5 products ordered from Highest price to Lowest price (**PlayStation 5**).

## INSTRUCTIONS

Exercise:

	-Enter the website.

	-Select Mexico as country

	-Search by the term "playstation 5

	-Filter by condition “New” -Filter by condition ‘New’ -Filter by location “Cdmx”.

	-Filter by location “Cdmx” -Sort by ‘Cdmx’ -Sort by “highest to ”lowest".

	-Sort by “highest to ”lowest price

	-Obtain the name and price of the first 5 products.

	-Print these products in the console

## IMPORTANT NOTE ## **LIMITATION ON LOCATION FILTERS

**Limitation on location and condition filters**.

During script development, an attempt was made to automate the interaction with the location (CDMX) and product condition (New) filters. However, these actions triggered Mercado Libre's anti-bot security systems, which redirects the user to an authentication window, interrupting the automated flow.

This behavior suggests that such elements are protected by automation detection mechanisms (such as behavioral validation or hidden CAPTCHA's), which prevents their manipulation without an authenticated session and human control.

As a result, location and condition filters were not integrated into the final script to maintain stable execution and avoid crashes or redirects.

## Features

- Performs automatic search for the desired term.
- Sorts results by **Highest Price**.
- Extract and display in console:
  - Product title
  - Product price

## Technologies used

- VisualStudioCode
- Python** 3.11+
- **Selenium** 4.0+
- **Google Chrome** and **ChromeDriver** **ChromeDriver** **Chromium** 4.0+

## Requirements

1. Have [Python] installed.
2. Have [Google Chrome] and the corresponding [ChromeDriver].
3. Install the necessary dependencies with:

pip install selenium webdriver-manager

selenium>=4.10.0
webdriver-manager>=4.0.1

## Steps for script execution

## OPTION 1

1- Open a new terminal -> execute the command : 
python .test_automation_challenge.py
2-Visualize and validate the steps described in the test
3-Check the data extracted from the first 5 products sorted in the terminal. 

## OPTION 2

1- Run the .exe file found in the repository in the pythonprojects folder.
2-Visualize and validate the steps described in the test.
3-Check the data extracted from the first 5 products sorted in the script console.

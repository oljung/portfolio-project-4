# Dinner Wizard
Dinner Wizard is a web aplpication for planning your dinners over a period of time, and then quickly making a shopping list from the recipes that you want to make. By creating and saving your own favourite recipies for later use, or borwsing recipes created by other users, you will be able to quickly plan a couble of dinners, then by a simple click on a button you will have a complete shopping lsit of all the items included as ingredients for your recipes. <br>
Link to the deployed site: https://dinner-wizard.herokuapp.com/


### Table of Contents
**[1. User Experience](#1-user-experience)**<br>
**[2. Features](#2-features)**<br>
**[3. Data Model](#3-data-model)**<br>
**[4. Technologies Used](#4-technologies-used)**<br>
**[5. Testing](#5-testing)**<br>
**[6. Deployment](#6-deployment)**<br>
**[7. Credits](#7-credits)**<br>


## 1. User Experience

### 1.1 Project introduction

The goal of this app is to make planning dinners as easy, quick and simple as possible. The average family usually have 10-20 different recipes that cicle, and wouldn't it then be nice to have them saved in a way that a few simple clicks will generate the dinners for a week, and then automatically transform into a shopping list? After all, dinner planning and grocery shopping can be quite the task, espacially for parents with smaller kids. That's is where Dinner Wizard can really help you speed things up in every day life.
### 1.2 Design guidelines

The aim when designing the app is to give it a clean design, where the different fucntions of the app will be in focus. In order for as many users as possible to be able to use the app, it is important that all functions, buttons and lists are placed in an intuitve way, and that creating and editing items will be done in a logical way even to users with less computer experience. Here lies the biggest challange when designing the app.<br>

Click [here](static/media/DinnerWizard.pdf) to view the wireframe showing a draft of the page layout

### 1.3 Project goals

- Provide a way for users to save their favourite and most used recipes

- Provide a way for users to plan what to eat during a week or short period of time

- Help users with dinner inspiration by being able to find new recipes from other users

- Provide a way to quickly create a shopping list to ease grocery shopping

### 1.4 Target audience

The main audience for this application are people who have a few recipes that they use often and want a way to add them to a dinner plan, as well as users who struggle to find inspiration and recipes for their dinners and need a quick way to find recipes. Many people also find it tedius to create a list of groceries before going shopping. We therefore have 3 main type of users

- User who want a way to save recipes to be able to quickly chose from their most used recipes in the future: <br>
**Needs:** A way to save recipes for quick access in the future<br>
**Goal:** Provide every tool necessary for a user to create a recipe and save it to a database<br>
**How:** Create a database model that will hold necessary information about recipes and allow users to choose categories to quickly find them later on, and the ability to mark recipes as "favourite"

- User who wants to find recipes to add new dinner experiences:<br>
**Needs:** A way to search for recipes by name of category<br>
**Goal:** Implement a filter system that works with both name search and categories<br>
**How:** Adding fields in the database model for categories to recipes and provide a search bar to enter recipe names and search

- User who wants to quickly and automatically create a shopping list from the selected recipes:<br>
**Needs:** A way to create a shopping list from the selected recipes without writing things down
**Goal:** To have a simple button click send every item of ingredient from the selected recipes to a shoppinglist
**How:** Create a database model for holding shopping lists and a template connected to a view where all the items are shown and are interactable

### 1.5 User stories

- As an owner, I want to make sure I can remove items where mistakes were mage
- As an owner, I want to be able to handle user information to help users who have lost their information
- As a user, I want to be able to create an account to save my information
- As a user, I want to be able to save my recipes
- As a user, I want to be able to create a dinner plan for a period of time
- As a user, I want to be able to add new types of ingredients to my recipes
- As a user, I want to be able to mark recipes as my favourites for quick and easy access in the future
- As a user, I want to be able to add categories to my recipes to quickly show what type of food they are
- As a user, I want to be able to search for new recipes using categories or name
- As a user, I want to be able to quickly create a shopping list from the recipes I have selected
- As a user, I want to be able to edit the recipes I have created
- As a user, I want to be able to modify and save other peoples recipes
- As a user, I want to be albe to edit the dinner plans I have created
- As a user, I want to be able to create dinner plans for the future, to be inactive until it is time
- As a user, I want to be able to reuse previously active dinner plans

## 2. Features
This application has a full CRUD functionality for creating a recipe plan, recipes and ingredients. All these can be user created in order to provide a wide functionality. For a more in-depth guide to the different features on Dinner Wizard, please check out the [about page](https://dinner-wizard.herokuapp.com/about/) for the site.

## 3. Data Model

## 4. Technologies used

## 5. Testing
The forms and models used in this project were tested using the python TestCase module. These files have a 100% test coverage. In order to run tests, you must comment out the database information in the settings.py, and instead uncomment the database information that is provided by default. This is due to limitations to the free edition of Heroku postgres database. The views were not tested to full extent, this due to django-allauth making testing user driven content in views very complicated. The entire project was tested in minute detail manually by me (the creator of the site) and some very appreciated help from friends.
### 5.1 Validator testing
- All pages of the site were tested using this [validator](https://validator.w3.org/). All pages passe without warning or errors.
- The css file style.css was tested using this [validator](https://jigsaw.w3.org/). It passes with no errors and no warnings.
- The JavaScript file of the project was tested using [JSHint](https://jshint.com/) and returned no warnings or errors.
- All .py files edited by the user with the exception of the "settings.py" (this file will fail pep8 due to the nature of some of the data. It also has a commented out database, for switching between testing and deoplyed database) and no errors were found.

### 5.2 Bugs
- As of this moment, there are no longer any known bugs.
- *SOLVED* Upon deploying the site and allowing other users to test it, an issue creating accounts using email was found. Whenever a user entered the optional email field, they would recieve a "500 server not found" error. This was likely linked to allauth wanting email verification, so turning this off in settings ```ACCOUNT_EMAIL_VERIFICATION = 'none'``` solved this issue fixing the bug and allowing users to sign up with or without email.
### 5.3 Testing user Stories
- As an owner, I want to make sure I can remove items where mistakes were made
- As an owner, I want to be able to handle user information to help users who have lost their information
- As a user, I want to be able to create an account to save my information
- As a user, I want to be able to save my recipes
- As a user, I want to be able to create a dinner plan for a period of time
- As a user, I want to be able to add new types of ingredients to my recipes
- As a user, I want to be able to mark recipes as my favourites for quick and easy access in the future
- As a user, I want to be able to add categories to my recipes to quickly show what type of food they are
- As a user, I want to be able to search for new recipes using categories or name
- As a user, I want to be able to quickly create a shopping list from the recipes I have selected
- As a user, I want to be able to edit the recipes I have created
- As a user, I want to be able to modify and save other peoples recipes
- As a user, I want to be albe to edit the dinner plans I have created
- As a user, I want to be able to create dinner plans for the future, to be inactive until it is time
- As a user, I want to be able to reuse previously active dinner plans

## 6. Deployment


### 6.1 Make a clone
To clone the repository to make a local copy of it, follow these steps:
1. Login to [GitHub](https://github.com/) and locate the [repository](https://github.com/oljung/portfolio-project-two)
1. Under the repository name, click "Clone or download"
1. To clone the repository using HTTPS copy the link under "clone with HTTPS"
1. Open Git Bash
1. Change directory to where you want the clone to be saved
1. Use the command "git clone" and then paste the url you copied from step 3
```
$ git clone https://github.com/oljung/portfolio-project-two
```
7. Your clone will now be saved, and any commits will be saved to your new repository

### 6.2 Deploy on Heroku


## 7. Credits

### Code


### Testing


### Special Mentions

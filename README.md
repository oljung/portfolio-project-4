# Dinner Wizard
Dinner Wizard is a web aplpication for planning your dinners over a period of time, and then quickly making a shopping list from the recipes that you want to make. By creating and saving your own favourite recipies for later use, or borwsing recipes created by other users, you will be able to quickly plan a couble of dinners, then by a simple click on a button you will have a complete shopping lsit of all the items included as ingredients for your recipes.


### Table of Contents
**[1. User Experience](#1-user-experience)**<br>
**[2. Features](#2-features)**<br>
**[3. Data Model](#3-data-model)**<br>
**[4. Testing](#4-testing)**<br>
**[5. Deployment](#5-deployment)**<br>
**[6. Credits](#6-credits)**<br>


## 1. User Experience

### 1.1 Project introduction

The goal of this app is to make planning dinners as easy, quick and simple as possible. The average family usually have 10-20 different recipes that cicle, and wouldn't it then be nice to have them saved in a way that a few simple clicks will generate the dinners for a week, and then automatically transform into a shopping list? After all, dinner planning and grocery shopping can be quite the task, espacially for parents with smaller kids. That's is where Dinner Wizard can really help you speed things up in every day life.
### 1.2 Design guidelines

The aim when designing the app is to give it a clean design, where the different fucntions of the app will be in focus. In order for as many users as possible to be able to use the app, it is important that all functions, buttons and lists are placed in an intuitve way, and that creating and editing items will be done in a logical way even to users with less computer experience. Here lies the biggest challange when designing the app.

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


## 3. Data Model

## 4. Testing

### 4.1 Validator testing


### 4.2 Bugs

### 4.4 Testing user Stories

## 5. Deployment


### 5.1 Make a clone
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

### 5.2 Deploy on Heroku


## 6. Credits

### Code


### Testing


### Special Mentions

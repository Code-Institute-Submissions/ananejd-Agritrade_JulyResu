!# AGRITRADE
## Full Stack Framework with Django



The project is a Database-driven Ecommerce shop Agricultural products in relation in poultry production.
The project allows a user to view a collection of poultry farming related products under various categories and trade offers, 
whiles reviewing their prices and moving desired items to the basket where payment can be made.

<hr>
Find a live version <a href="http://ami.responsivedesign.is/?url=https://jd-agritrade.herokuapp.com/">here</a>


## UX Design

My design was inspired by the code institute video lecture on full stack web development with Django. 
The design displays a beautiful picture of a chick on the homepage with a shop now button which opens up to the store.
Users of the website are able to view the various products on sale at the shop under the categories of pricing, rating and whether or
not the product is feed related or a poultry product. 
The search input area in the header allows users to search for the product they are shoping for.
Users have the option to create an account using the Account button. 
The basket is on display for users who have made purchases with the total cost of their purchase on display.
Overall, the colour green has been used in designing the website to depict the greenery associated with Agriculture.


##Scope
A MVP (minimum viable product) includes:

- landing page displaying a picture of a lovely looking chick 
- A search input area for looking for products
- An Area for accessing your account or setting up one.
- A basket button 
- A library button acting as a dropdown menu for various categories of products
- A shop now button that displays all products on offer.


### User stories

**ID** | **As a/an** | **I want to be able to...** | **So that I can**
--- | --- | --- | ---
1 | Site User | Register to the site | Log in to my account 
2 | Site User | Log In and Log Out | View my profile
3 | Site User | Receive email confirmation | Confirm successful registration
4 | Site User | Have a user profile | View my purchases, and be able to check my order history
5 | Potential customer | View some crafts | Select to purchase
6 | Potential customer | View details of the craft | See price and description
7 | Potential customer | Pay for the craft i like | Buy
8 | Customer | View craft in my bag | Check the cost to review
9 | Customer | Enter payment information and see that process is secure | Checkout without issues
11 | Administrator | Add new catergory of crafts | To make them visible to customer
12 | Administrator | Edit or update various categories | To change a pric and/or description 
13 | Administrator | Delete a category of craft | To remove from a site

## Features

### home

The home page greets farmers with a picture of a beautiful chick with a SHOP NOW button. 
The SHOP NOW button invites farmers to take a look at the various products on offer.
Farmers are also informed of a delivery fee waiver over a specific amount.
Various icons in the header helps summarize the various products the site offers to the visitor of the website.

### SEARCH AREA 

the search area allows users of the website to directly search for their product of interest without combing through the site.

### MY ACCOUNT

The MY ACCOUNT icon allows users to setup an account on the website or accessing their existing account on the website.

### ALL PRODUCTS 

The ALL PRODUCTS icon when clicked on offers the site user a categorisation of the products on offer. 
ie by pricing, rating and a view of all products.

### POULTRY PRODUCTS 

This link allows the user of the website to assess specific poultry products being sold on the site.
ie Eggs, Dressed Chicken, Live Birds and Point of lay chicks.

### POULTRY FEED 

This links allows the users of the website to assess Poultry feeds sold on the website

### Basket

The basket button on the right side of the navigation bar is meant to hold a list of items 
that have been reviewed by the site user awaiting payment.

### Wireframes

- Home Page

    <details><summary>Desktop (click to view)</summary>

    ![](<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2F9eOMIaCWLS6u7WBXtREDNX%2Fcraftstore%3Fnode-id%3D1%253A27" allowfullscreen></iframe>)
    </details>
    
    
    ![](static/images/Wireframe.png)
    </details>
## Technologies Used

- Python 3.8.8
- Django3.2.4
- BootStrap 4
- Coverage 5.5
- JavaScript
- CSS
- HTML
- figma for wireframing

## Database Schema

Database contains 3 table:
- user
- categories
- products

I use Django default databases SQLite in gitpod environment and PostgreSQL database with Heroku as production enviroment.


### Security

All sensitive access keys are stored as `Config Vars` on Heroku cloud application platform.
Django allauth was used to meet security requirements.

## Deployment
This project was built using Python 3.8.6 and Flask 1.1.2.
1. The project was deployed to Heroku with config vars:
1. created requirements.txt that Heroku knows which packages are required for the application to run and install them.
1. created Procfile that Heroku knows what kind of application this is.
1. project eventually deployed at 
<a href="https://jd-agritrade.herokuapp.com/">here</a>">

#### Challenges 
The developer was constrained by time in studying and executing all the desired functionalities for the project within an 
expected time frame. He however hopes to bring the project to completion in due course.

There was a difficulty in linking the database to the heroku app for which the developer continues to work on.

### project inspiration: 

1. inspiration for this project were largely drawn from tutorials on the Youtube channel of Very Academy.
1. Git ignore file was adopted from www.toptal.com/developers/gitignore/api
1. Appreciation goes to the code institute student support team for being very supportive throughout my period
   study with the code institute
1. Im grateful to my mentor Seun Owonikoko for her time.


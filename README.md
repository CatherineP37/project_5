# Chocolate Treats Ecommerce Website

This is an ecommerce store that sells handmade chocolate bars.

Link to the deployed project:

[Deployed website](https://doctor-appointment-booker-567ff6ab7202.herokuapp.com/)

## Scope

The following must be included in the project:

- Products page
- Page showing information about an individual product
- Accounts
- Shopping bag
- Checkout

## Sitemap

![Sitemap](images/map.png)

## User Stories

Here is a picture of the GitHub project board for this project:

![Project board](images/user_stories.png)

Epic - Navigation

- As a shopper I want to view a list of products so that I can choose a product.

- As a shopper I want to view product details easily so that I can know enough information to make a choice.

- As a shopper I want to easily view the total cost of my purchases so that I can avoid spending too much money.
  
Epic - User accounts

- As a site user I want to easily make an account so that I can more easily make purchases.

- As a site user I want to login and logout so that I can access my account.

- As a site user I can easily login to my account if I forget my password.

- As a site user I can receive an email confirmation after making an account.

- As a site user I can have my own user profile so that I can view my order history and save my payment information.

Epic - Shopping bag

- As a shopper I can easily select the quantity of a product in my shopping bag.

- As a shopper I can easily view items in my shopping bag.

Epic - Checkout

- As a shopper I can easily enter my payment details so that I can make a purchase.

- As a shopper I can view an order confirmation after making an order.

- As a shopper I get an email confirmation after making an order.

Epic - Store management

- As a store owner I can easily add new items to my store.

- As a store owner I can edit product details.

- As a store owner I can delete products from my store.

## Wireframes

These are wireframes for the mobile screens.

![wireframes](images/wireframes.png)

## Database Schema

![database schema](images/database.png)

## Features

### Header

![Header](images/header.png)

### Menu for users who are not signed in

![Menu for users who are not signed in](images/menu_1.png)

### Landing page

![Landing page](images/landing_page.png)

### Sign up form

![Sign up form](images/sign_up.png)

### Login form

![Login form](images/login.png)

### User account home page

![User account home page](images/account.png)

### Appointment booking form

![Appointment booking form](images/booking.png)

### Booked appointments page

![Booked appointments page](images/bookings.png)

### Sign out

![Sign out](images/sign_out.png)

## Bugs

There are no current bugs in the project.

These are some of the bugs that occurred during the development of the project:

There was an issue with trying to get the dropdown menu to work. By mistake I hadn't put the link to the JavaScript file in the html file. After I added the link, the dropdown menu worked but was only showing the dropdown part while it was being pressed. Also the words were not visible and the width of the dropdown was very narrow and that's probably why the words weren't on it. I solved the issue by changing the css.

The header was set to position: fixed and was covering the content. To solve this I increased the size of the margin at the top of the main section.

I had problems deploying my project to Heroku. This was solved by adding the correct Config Vars to Heroku.

The navigation menu was showing the same things for signed in users as signed out users. This was solved by changing the urls.

The text on the buttons was not fitting on the buttons in the mobile view so I set the font size in percentage instead of pixels.

I was trying to prevent double bookings by filtering out appointments that had been booked. It wasn't working and the booked appointments were still showing up on the list of available appointments. This was solved by editing the booking view.

## Testing

### W3C HTML Test

The project passed the W3C HTML test.

![W3C HTML Test](images/html.png)

### W3C CSS Test

The project passed the W3C CSS test.

![W3C CSS Test](images/CSS.png)

### JSHint Test 

The JavaScript was tested with JSHint and no problems were found.

### CI Python Linter Test

Python was tested with the CI Python Linter. No major issues were found.

### Browser Testing

The website was tested on a variety of browsers. It was also tested in Google 
Chrome DevTools to see what it looks like in a variety of screen sizes.

### Lighthouse Testing

This is the Lighthouse test result:

![Lighthouse test result](images/lighthouse.png)

### Manual Testing

As I went through the project I manually tested each user story thoroughly. I tested the views, 
the models, the booking form and the authentication. The user can create an account so that they
can log in. They can log in with their details. They can view the appointments that they've
already booked and they can update or delete the bookings. They can use the booking form to book
an appointment and they can choose from a list of available appointments.

## Deployment

This project was deployed using Heroku.

A Procfile and a requirements.txt was added to the project.

A new app was set up in Heroku and the config vars were added to the app.

GitHub was selected as the deployment menthod and the GitHub repository was linked to Heroku.

"Deploy Branch" was selected to manually deploy the project.

## Credits

w3 schools 

Code Institute

stackoverflow


## Acknowledgements





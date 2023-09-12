# Milestone Project 3 - Live Music Cardiff

## Purpose

This website was created for Code Institue's Milestone Project 3 assignment. The Purpose of the project is to demonstrate an understanding of working with a database where users are able to Create, Read, Update and Delete data entirely within the website. A full list of technologies used can be found in the technologies section of this readme.

## Live Music Cardiff Responsive Website

This project is a website where users are able to view advertisements for which they, or other users have created. Users will have to login to add events to the website. Users will not need to log in to view events. Users who have created events will need to login in order to edit or delete events they have created. Once logged in users will only be able to edit or delete events which belong to them.

# User Experience Design 

## User Stories

### As a first time user, I want:

    1. To be able to easily understand the purpose of the site
    2. To be able to view events that have allready been added by other users
    3. To be able to create an account and list my own event
    4. To be able to edit or delete the events I create

### As a returning user, I want:

    1. To be able to see if any new events have been added.
    2. To be able to edit or delete events which I have added.
    3. To be able to add new events.
    4. To see all of the events which I have added. 
   
### As a frequent user, I want:

    1. For other users not to be able to edit or delete my events.



# Structure

## Bootstrap

Bootstrap 5 was used to structure the website. As this site is data driven the minimum about of elements were put in place first. This way any elements added to increase visual appeal only service the websites core CRUD functionality.

## Base.html

A base html template was used to create the navbar (header) and footer of the website. This is to ensure that the navbar and footer remain consistent in design as the user moves through thr website. 

### Nav Bar

In the nav bar an if/else statement was used to control which nav elements a user can see dependant on weather they are logged in or not. 

### Footer

A simple call to action button with a if/else statement controlling what a user sees dependant on if they are logged in. If the user is not logged in, a button promping them to create an account is visible. If they are a button promping them to add an event is visible.

## Home

Simple landing page with image of one of Cardiffs premier venues. Text explaining purpose of website with button prompt for user to view all events. Log in not required.

## Signup

A form where users are able to create their account. First name, email address and password. The password field appears twice to ensure user types password correctly. Checks in place to ensure email address is valid and not allready in use by another user account.

## My Events (user events)

After signing in the user will be redirected to this page. This page displays all events which the user had created, along with opeion to edit or delete each event. Clicking delete calls a modal where the user is asked to confirm event deletion. Clicking edit on any event will take the user to the edit event page. If the user has not created an event they are prompted to create their first event. Login is required to view this page.

## Add Event

A form where users can add the relevant information for their event. Once submit is clicked the event is added to the database and will appear publically for all users to see (signed in and not signed in). The user will then be redirected to the 'My Events' page where event they created will be displayed.


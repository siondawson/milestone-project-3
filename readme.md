# Milestone Project 3 - Live Music Cardiff

![multi device mockup](/assets/multi-device-mockup.png)

## Purpose

This website was created for Code Institue's Milestone Project 3 assignment. The Purpose of the project is to demonstrate an understanding of working with a database where users are able to Create, Read, Update and Delete data entirely within the website. A full list of technologies used can be found in the technologies section of this readme.

## Live Music Cardiff Responsive Website

This project is a website where users are able to view advertisements for which they, or other users have created. Users will have to login to add events to the website. Users will not need to log in to view events. Users who have created events will need to login in order to edit or delete events they have created. Once logged in users will only be able to edit or delete events which belong to them.

# User Experience Design 

## User Stories

### As a first time user, I want:

1. To be able to easily understand the purpose of the site.
2. To easily navigate the website.
3. To be able to view events that have allready been added by other users
4. To learn more details of each event.
5. To be able to create an acccount.
6. To list my own event
7. To be able to edit or delete the events I create

### As a returning user, I want:

1. To be able to see if any new events have been added.
2. To be able to edit or delete events which I have added.
3. To be able to add new events.
4. To see all of the events which I have added. 
5. To easily navigate the website.
6. For other users not to be able to edit or delete my events.
7. To learn more details of other users events.
8. To be able to log in

### As a frequent user, I want:

1. For other users not to be able to edit or delete my events.
2. To add new events
3. To edit my events
4. To delete my events
5. To see what new events have been added by other users. 
6. To learn more details of events added by other users. 
7. To be able to log in

# Structure

## Bootstrap

Bootstrap 5 was used to structure the website. As this site is data driven the minimum about of elements were put in place first. This way any elements added to increase visual appeal only service the websites core CRUD functionality.

## Base.html

A base html template was used to create the navbar (header) and footer of the website. This is to ensure that the navbar and footer remain consistent in design as the user moves through thr website. 

This allows the user to easily navigate the website with a consistent nav and footer throughout.

### Nav Bar

In the nav bar an if/else statement was used to control which nav elements a user can see dependant on weather they are logged in or not.

This allows the user to know if they are logged in or out. Hidden nav links to pages that require login ensure non logged in users cannot access pages such as 'my events'.

### Footer

A simple call to action button with a if/else statement controlling what a user sees dependant on if they are logged in. If the user is not logged in, a button promping them to create an account is visible. If they are a button promping them to add an event is visible.

This allows users to easily navigate the webite.

## Home Page

Simple landing page with image of one of Cardiffs premier venues. Text explaining purpose of website with button prompt for user to view all events. 'How it works' section added towards completion of project. See differnces to design section. 

Log in not required. 

This helps first time users understand the purpose of the site, navigate to see other users events and create an account if they wish.

Returning and frequent users can use this landing page to easily navigate to any page of the website they please within on or two clicks. 

## Signup Page

A form where users are able to create their account. First name, email address and password. The password field appears twice to ensure user types password correctly. Checks in place to ensure email address is valid and not allready in use by another user account.

This page allows first time and returning users to create an account. Frequent users who use the website to only view events may easily create an account if they have an event to add.

## Login page

Once a user has created their account they are automatically logged in. A login page was created so that if a user is logged out they may log back in. Simple form for users to complete with login credenitals that they created. 

## My Events Page (user events)

After signing in the user will be redirected to this page. This page displays all events which the user had created, along with opeion to edit or delete each event. Clicking delete calls a modal where the user is asked to confirm event deletion. Clicking edit on any event will take the user to the edit event page. If the user has not created an event they are prompted to create their first event. Login is required to view this page.

This Allows all users who have added one or more events to view events which belong to them at a glance. Buttons on each event allow users to quickly and easily delete an event if they wish. Users may also click 'edit' on each respective event to make changes. 

Fulfiling:

first time user stories: 

1. To be able to edit or delete the events I create

Returning user stories: 

1. To be able to see if any new events have been added.
2. To be able to edit or delete events which I have added.
3. To see all of the events which I have added.
4. To easily navigate the website.

Frequent user stores:

1. To add new events
2. To edit my events

## Add Event Page

A form where users can add the relevant information for their event. Once submit is clicked the event is added to the database and will appear publically for all users to see (signed in and not signed in). The user will then be redirected to the 'My Events' page where event they created will be displayed.

Page allows all logged in users to create a new event.

## Edit event Page

Accessible from the users 'my events' page. When the user clicks edit they are taken to this page where a similar form to the 'add event' page will be pre populated with full information from the event that they have allready supplied ready for editing. 

This page allows all logged in users to update their event.

Functionality has been added to prevent users from manually navigating to an event with an ID which they do not own. A user manually navigate to edit another event by changing the event ID at the end of the url to another. If they do this an the event does not belong to them they will be flashed a message to advise them that they do not have permission to edit the event.

This fulfils user story: For other users not to be able to edit or delete my events.

## All Events Page

Accessible with or without loggin in. This page displays all upcoming events in chronologial order on a series of cards generated by a jinja for loop. Once an event has passed it is no longer displayed on this page, but not deleted from the database. The user may click link provided on each card to view full info for each event individually.

This fulfils user stories: 
    1. To easily navigate the website.
    2. To be able to view events that have allready been added by other users
    3. To learn more details of each event.

## Event Page

Accessible with or without logging in. This page displays all information available from the database for the event which the user has selected on the 'All Events' page. 

This fulfuils user story: To learn more details of each event.

# Design

This projects purpose is to demonstrate ability to work with a database and perform CRUD functionality. Therefore overall design has been kept fairly simple with the goal of facilitating CRUD functionality without complicating visual features. 

## Appearence

A simple clean layout which facilitates the CRUD functionality of the website. 

### Images

Only a single image of a well known important Cardiff venue is used. 

# CRUD - Create, Read, Update, Delete

### Authentication

An athentication system was required so that users may log in and view events that they have created. They are also able to edit and delete. Authentication system prevents other users from editing or deleting data which they have not created. Authticaton system also prevents non registered users from creating, updating and deleting, restricting their usage to read only. Authentication system was created with [this tutorial](https://www.youtube.com/watch?v=dam0GPOAvVI).

## Database Schema

![er diagram](/assets/er-diagram.png)

A straighforward database schema. of USER and EVENT. The user id appears in the EVENT table as a FOREIGN KEY. The database has been designed this way for comparing of current user id to the user_id of each event. In the early stages of the project design that users must not be able to update or delete events which they have created. 

### Create Functionality

Data is captured via the use of forms. Standard bootsrap forms suited this purpose with layout modifed for intended purpose.

#### Signup

Users can create their user data with use of the signup form. Data is stores in the 'User' table. The id column is the primary key. Once this login data is created there is currently no means of updating. This will be left to a future version. 

#### Add event

Users can create data by navigating to the add event page. Data is stored in the 'Event' table. Each event has a unique id. The user_id column is a foreign key from the'User' table. 

Use of the foreign key allows users to 'own' events. Data may be read relating to only one event. 

### Read Functionality

Data is read from the database in two ways.

1. Cards. Bootstrap cards were used to present data at a glance for:
    1. All Events: Where a user logged in or not can view shorthand information for every event listed including title, venue, date and time.
    2. User Events: Where logged in users can view events that they have created in a manner similar to above. With added options for them to edit or delete the event.
2. Event Page. Accessible via a link on each event on the 'All Events'. All available information is displayed on a single page for the spesific event user the has selected.

### Update functionality 

Similar use of forms to 'Create 'Functionality'. Accessed via link in cards on the 'User Events' page. The 'Create Event' Form was duplicated and repurposed for update functionality. Existing event data is pre populated into the form ready for the user to edit.

This was implements to that users are able to update events that they have created. Measures built into the code prevent users from updating event data which they have not created. 

### Delete functionality

Accessed via link in cards on the 'User Events' page. Defensive programming first opens a bootstrap modal on clicking 'delete'. User is warned that confriming deletion will pernamently delete the event. 

To add new events
    3. To edit my events

## Favicon

A favicon was added so a user can better recognise the website among multiple browser tabs. The same color used in nav bar was used along with the initals of the website name: LMC.

## Wireframes

[Wireframes can be found here.](https://github.com/siondawson/milestone-project-3/tree/main/wireframes)

## Differences to design

During implementation some small design changes were made to better meet user stories.

1. 'How it works' section added to home page. A small section explaining the purpose of the website to a first time user. 3 large font awesome icons with short sentence inform user that they may browse events without signing up, create an account if they have an event to list and add the event once they have created their account. 

This helps fulfil all first time user stories.

2. Button added to event.html. A friend who I asked to test the website suggested adding a 'back button' to the event info page so that the site be more easily navigated. 

This helps fulfil user story: I want to be able to easily navigate the website.

3. 'More info' button added to event cards in all events. In wireframing I intented to use anchor links in the title of each event to link users to the events full info. On using CSS to change the link color to black it became clear that users will require a more of a visual cue to know that further information on each event is available. 

This helps fulfil user stories: 
    1. I want to be able to easily navigate the website. 
    2. To learn more details of events added by other users.

4. Dark background added to homepage jumbotron. Added to avoid contrast issues with text on background image.

This helps fulfil user stories:

To be able to easily understand the purpose of the site and to easily navigate the website. 



# Technologies Used

* HTML
  * HTML was used to complete the structure of the website
* CSS
  * CSS was used for custom styling on the website
* Python
  * This website is a python package. Python is used to render the website and pass data between the database (back-end) and the front-end.
* Flask
  * Flask was used..
* SQL Alchemy
  * Used for database management
* Elephant SQL
  * Free plan (Tiny Turtle) used to host database on deployed version.
* Heroku
  * Used for deployment of live site.
* Jquery
  * Used primarily for datepicker and timepicker. 
* Techsini
  * Used to create apple device mockup for readme.
* Fontawesome
  * Used for calendar icons and info icons on homepage.
* Google fonts
  * Used for project font styling.

# Testing

This project is a fully interactive website where users can:

1. View events (with or without logging in)
2. Create an account
3. Create events 
4. Edit events
5. Delete Events

Testing will be performed on:

1. The websites visual appearence accross all screen sizes.
2. CRUD functionality.
3. Login/ Logout/ Signup Functionality

# Test Users

These Test users were created on the live site and may be logged into for testing.

test@email.com, password: sun3451, first name: Sion
test@test.com, password: 1234567, first name: Tester1 

Feel free to use these test accounts or create your own account. 

# Test Cases

[Full testing can be found here.](/testing/live-Music-cardiff-testing.pdf)

## High level tests against user stories

### As a first time user, I want

    

1. To be able to easily understand the purpose of the site.
    * All content displays correctly on all screen sizes.
2. To easily navigate the website.
    * Simple to use nav system impemented and tested. 
3. To be able to view events that have allready been added by other users
    * Non loged in users can view all listed events in the same way logged in users can. 
4. To learn more details of each event.
    * All users logged in or not can view full event info without logging in 
5. To be able to create an acccount.
    * Signup page implemented so users can add their information to the 'user' table. 
6. To list my own event
    * Add event page implemented to users can create event infomation and add it to the 'event' table. 
7. To be able to edit or delete the events I create
    * Edit and delete functionality so users can peform these tasks within a user interface they will be able to learn to use on the first pass. 

### As a returning user, I want

1. To be able to see if any new events have been added.
    * All events page updates as new events are added. Events in past are removed from this page so it does not appear cluttered. 
2. To be able to edit or delete events which I have added.
    *  Edit and delete functionality so users can peform these tasks within a user interface they will be able to learn to use on the first pass.
3. To be able to add new events.
    * Logged in users can easily add events to the event table via the add event page
4. To see all of the events which I have added. 
    * My events displays all events the logged in user has created. Past events are displayed so that a user may amend if a similar future event is planned, or delete as they prefer. 
5. To easily navigate the website.
    * Easy to use UI implemented to users may do this.
6. For other users not to be able to edit or delete my events.
    * Measures built into the code to check if an event belongs to the user before allowing user to edit. Deletion of event not created by another is not possible. An admin user able to delete or edit any event would useful in a future version.
7. To learn more details of other users events.
    * All users can access event info for all added events both logged in and logged out.
8. To be able to log out
    * Log out button provided in nav bar. Visible at all times to logged in users. Function tested.

 
### As a frequent user, I want

1. For other users not to be able to edit or delete my events.
    *  Measures built into the code to check if an event belongs to the user before allowing user to edit. Deletion of event not created by another is not possible. An admin user able to delete or edit any event would useful in a future version.
2. To add new events
    * Logged in users can easily add new events to events table.
3. To edit my events
    * Logged in users can edit event they have added by going to my events and clicking edit.  
4. To delete my events
    * Users can delete events they have added from the my events page.
5. To see what new events have been added by other users. 
    * Users both logged in and out can view all events added by all users.
6. To learn more details of events added by other users.
    * All users can access event info for all added events both logged in and logged out.
7. To be able to log out
    * Log out button provided in nav bar. Visible at all times to logged in users. Function tested.


## Code Validator testing

HTML ran through validator with no errors found.

CSS ran through validator with no errors found.

Validator screen shots can be found [here](https://github.com/siondawson/milestone-project-3/tree/main/testing).

## Issues found during testing 

1. Datepicker formatting not working on deployed website, but working when ran locally.
2. Issues with updating time field.
   1. Time data not being read by timepicker on loading update event page.
   2. Time format causing DataError 

# Deployment 

This project was created using the code institute template.

## Version Control

This project was created using Visual Studio Code editor and pushed to 'milestone-project-3', a remote repository in github.

Throughout the project these commands were used to save work and push changes to github via the command line terminal.

1. Type: git add .
    * This command adds files to the staging area before committing.
2. Type: git commit -m "a message goes in here explaining what chanes were made"
   * This command commits changes to the local repository
3. Type: git push
    * This command commits all changes to the remote GitHub repository.

## Clone the repository to your machine

Navigate to the github repository

1. Click on the code drop down button.
2. Click HTTPS
3. Copy repository link
4. Open your IDE (git must be installed)
5. Type git clone (copied git url) into the terminal.
6. The project will now have been cloned on your machine.


## Heroku

This project is deployed via Heroku. Heroku is connected to this projects github repository. With every push the deployed Heroku app is updated.

## Database (Elephant SQL)

The deployed website is connected to a database hosted by Elephant SQL.

### Project deployed via Heroku with the following steps.

1. Open command line terminal and type command: pip freeze --local > requirements.txt. This creates a requirements.txt file in the root directory of the repository.
2. Create Procfile. 
   1. Create new file in root directory.
   2. Name it "Procfile"
   3. Enter following command in the file: "web: python3 app.py"
3. Commit new files to github
4. Navigate to Heroku
5. Click create new app
6. Name the app (live-music-cardiff)
7. Enter confirg vars:
   1. DATABASE_URL : (ElephantSQL URL)
   2. IP: "0.0.0.0"
   3. PORT: "5000"
   4. SECRET_KEY: 
8. Navigate to Heroku deploy tab
9. Click connect to github
   1. Search for correct repository
   2. Connect
10. Click Deploy
11. Add tables to database
    1. Click 'more'
    2. Run console
    3. Type command: python3
    4. type command: from live_music_cardiff import db
    5. type command db.create_all()
    6. type command: exit()
12. Process complete

## Credits 

The code content of this software was createe by Sion Dawson

## Media 

One image was used on the home page. The source can be found [here](https://pixabay.com/photos/mermaid-quay-wales-cardiff-bay-89121/)

## Acknowledgement

Thankyou to my tutor Daisy McGirr for her help and guidance in this project. Thanks also to my wife Samantha (code institute alumni) for helping me overcome problems and discussing ideas.

  


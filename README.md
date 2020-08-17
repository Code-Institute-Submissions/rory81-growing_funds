
<img src=".\static\img\main_logo.jpg" alt="logo" height="25%" width="25%">

# Growing Funds 
###### Disclaimer: *this app is made for educational use only.*

# Index
1. [ Goal of GrowingFunds ](#goal)

<a name="goal"></a>
## Goal of GrowingFunds
Nowadays it isn't easy to get money from a bank or get investors for a new product/project when there aren't some garantees it will be successfull.
Furthermore, peoples dreams aren't considered much profitable. That's where crowdfunding fills the gap in the market.
Suddenly, cold hard facts aren't the only reasons to get funding anymore and likebility, sympathy and pure curiosity become very important.

This project gives people a change to get funding for their own hobby project, their life long dream project or solving heartaches projects. 

## UX and Features
To make sure all user stories were made or **not** made for a specific reason an Excel file was made with the following fields:
- Perspective: from which user's point of view am I looking
- Regarding: which part of the site does it apply to
- I want to be able to: what would that specific user want
- So that I can: what goal does that specific user want to achieve with that action
- Status: options were '*Not Started*', '*Ongoing*' or '*Done*' to maintain overview of the status of the entire backlog.

The User Stories where made for two kind of users:
1) The site user, looking for an interesting project to pledge to
2) A crowdfunding host, wanting to present its project to the public and get money to realise the project.

Some aspects are relevant to both group of users, like:
- able to register easily
- get an email after registration
- login and logout with emailaddress
- possibility to reset password
- able to email the site owner in case of misuse or fraud or any other questions
- able to update personal/delivery information in the profile page

These items are also beneficial for the admin, eventhough the admin isn't mentioned as a separate group,  If these elements go smoothly the less work it is for the admin to support the app.
Three user stories were not finished:
1) See how many people actually have donated. This wasn't done, because the site has the number of views to determine popularity of a project and percentage raised (and a progress bar) to see how far the host is from reaching the goal.
2) Adding Favorites, so that the user can decide on a later date if they want to pledge and if so can easily find them. This issue will be added to the backlog.
3) The host can see which reward and corresponding amount is most popular by the users like a dashboard for the host.This issue will be added to the backlog.

Below the several (future) functionalities are mentioned, per user group.

##### The Site User
At first instance the user will look to the most popular projects or the newest projects. 
To see the newest project, the top-5 newest projects are displayed on the homepage.

To show the popularity the user is given the number of views the projects has had. Furthermore, on the homepage the top-3 highest earners are displayed to see what is trending.
The simplest form to get more funding is word of mouth. So, everytime the page is looked at one view is added to the total number of views of that specific project. 
To increase the word of mouth the user has the ability to share the link of a certain project on all kinds of social media.

Secondly, the user has personal interests and wants to easily find projects that fit their personal interests.
Therefore, the projects are categorised by set categories and these categories are displayed on every page throughout the site (by putting the categories in a contexts.py).
When a user selects a certain category a table with all the projects is displayed. The table has pagination showing 2 projects by default, but has an option to select 5, 10, 25 or 50 projects per page.
If the user has a (part of the) name of an interesting project it can use the searchbar in the table to look for it in this particular genre.

Other ways to search for a particular project is to use the search bar present that searches through **all** projects.
Every searchbar searches for words within the title as well as the description.

If a user is deciding rather of not to pledge it is important to tell them what's in it for them. In each project the project owner has to name 3 possible rewards.
The more enticing the rewards the higher the change people will pledge. For now it is necessary to fill in all three project so people can pledge to reward no. 1, 2 or 3.
The user can only pledge to a project when logged on and can enter an amount of their own choosing to pledge, though Stripe needs it to be higher or equal to $0.50.
For that reason the default value is 1 and when a user accidentally enters a value lower than 1 it will return an error.

In the backlog there are a few more items to further develop this section:
1) user can select only the number of rewards that that specific project has when making a pledge.
2) when the pledged amount is lower than the amount needed for the selected reward, it should raise an error.

If the user has any questions for the host, the envelope in the project's page creates an email with the email address of the host as the recipient as well as the project title in the subject.
Once the user has pledged the user will get an email confirmation with the order number, the amount pledged and the name of the project.
Furthermore, the pledge will be shown in the projects table on the user's profile page. This way the user can see back to which projects it has pledged to and can easily return to those project pages.
On this same profile page can the user change their delivery information (address etc), although this information can also be updated when a user makes a pledge.


##### The Crowdfunding host
A project can only be started when logged on and the user has to agree to the conditions of the site to be able to publish the project. 
The content of the terms and conditions are now all made up, but are accessible by the information button next to the "Your Project" title.
Also when the host doesn't agree to the terms and conditions the arising error will give a link to the Terms and Conditions page.

The crowdfunding host wants to be able to tell their story, in order to entice people to pledge to their project.
The CKeditor is added to enable the host to put some styling in to the story and therefore make it more attractive.
A dropdown with predefined categories are given so that their isn't a proliferation of categories, making it harder for users to find a specific project.
When there isn't an image added to the project a default image will be shown.

In the backlog there are a few more items to further develop this section:
1) crowdfunding host only obligated to fill in 1 reward, but can also make more than 3 rewards if they want to.
2) host can enter a to and from amount, so that it can be used to check if the amount for the reward is consistent with the reward chosen by the site's user.
3) host can add pictures and format them on the site so that layout consistency is maintained.


Any fields that have an asterisk are obligated and will raise an error:

<em>Standard Errors</em>
- Fill in these fields or this field is required , if obligated fields are empty
- Select an item in the list, if no category has been selected

Some fields needed extra help to validate and were customised:
<em>Customised Errors</em>
- Please enter a goal  higher than 0, if the goal is lower or equal to 0
- A project should be at least 30 days. If the number of days between the date of creation and the end date are lower than that an error will occur.
- As mentioned before, the host has to agree to the terms and conditions. If there is no agreement an error will occur.
- Value should be higher or equal to 1 if the amount to be pledged is lower than one.

When a project is created the project will appear in the profile page. On the profile page the host can easily see how many days are left and how much it has raised as of yet.
In the same table there are buttons for the host to edit or delete the project. This way only the user that created the project can edit or delete it.
If a project is deleted, but a pledge has been made, the order history table will still show the pledge with the order number and the pledged amount.
However, the project title corresponding to this pledge will display <em>This project has been deleted</em>.
When a project is edited the goal and end date of the project are not shown and therefore not editable. 
This is to avoid a host extending the project every time it is almost ended or to manipulate the goal to their advantage.

If a user makes a pledge to the project of the host, the host will receive an email with:
- the amount, 
- the project name (just in case the host has multiple project)
- the reward chosen and
- the delivery information. The delivery information will **not** be send if the selected option for reward is "*Nothing*".

One issue will be placed on the backlog to further improve this latter section:
1) instead of the basic email with the order details the crowdfunding host will only get an email that a new order has been placed and can see the order details in a dashboard where all placed orders can be seen and sorted through.
The host will then be able to mark them as finished if the reward has been sent.

##### admin
In case the user is an administrator the option '<em>Project Management</em>' is available to easily get access to the admin functionality from Django.
The projects, categories, email addresses, users, orders and site name can also be managed from the project management page.

##### function of the different HTML pages
The following pages were made for the users:
- project_category.html: to display all projects per selected category
- projectdetail.html: show the details for one specific project
- projects.html: homepage, showing the top-3 top earners and the last 5 projects that were newly added
- search_projects.html: page showing the results from the top searchbar. Not using the homepage as there are filters (top-3 and top-5) on the projects
- startprojectform.html: form to create and publish your own project
- terms_and_conditions.html: terms and conditions the host has to agree to.
- checkout.html: the form where the user can pledge an amount of their choosing to a project the user is interested in.
- payment_success.html: shows the results of an succeeded payment
- profile.html: shows the order history and the created projects of a user with the delivery info of the user.
- terms_and_conditions.html: the user has to agree to the terms and conditions before publishing the project. It is only fair that they can read the terms before agreeing.
- search_projects.html: if the search bar in the header is used the results will be displayed on this page.


## Technologies used
- [JavaScript](https://www.javascript.com/): to make Stripe elements, ShareThis button and dataTables work and to add the django-countries dropdown.
- [Django](https://www.djangoproject.com/): web framework version 3.0.8
- [Python](https://www.python.org/): Python3 is used as programming language
- [Whitenoise](http://whitenoise.evans.io/en/stable/): to serve the static files. Which is an alternative to AWS if you do not have an amazon account and a creditcard.
- [Pillow](https://pillow.readthedocs.io/en/stable/): to be able to upload images
- [Allauth](https://django-allauth.readthedocs.io/en/latest/): addressing authentication, registration and account management
- [Stripe](https://stripe.com/en-nl): to enable the user to make payments and check credit cards
- [CKeditor](https://django-ckeditor.readthedocs.io/en/latest/): to be able to format the text entered by the user.
- [Crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): to easily make the forms and make them userfriendly.
- [Bootstrap](https://getbootstrap.com/): to customise the html and make it responsive to different devices.
- [JQuery](https://jquery.com): to simplify DOM manipulation.
- [Gitpod](https://gitpod.io/): used as IDE
- [Herokus](www.heroku.com): used as deployment platform
- [Trello](https://trello.com/): to register the user stories and issues, so to pick up a set of issues in a certain week
- [dbdiagram.io](dbdiagram.io): to make the data schema picture



## Template Code Institute
The template provided by Code Institute is used as basis (https://github.com/Code-Institute-Org/gitpod-full-template.git) and with this template a repository was created on GitHub by choosing the green *Use this template* button.

## How to create a django project
To use Django it needs to be installed first, so *pip3 install django==1.11.29* was used to install Django. To create a Django project where the necessary files are immediately created enter *django-admin startproject <name_project> .*
The '.' in the end is needed so the project is created in the root directory.
This will automatically create the `manage.py` file, but isn't necesarily an executable yet. So enter *chmod +x `manage.py`* in the terminal to flag this file as an executable. 

To initialize the database enter */manage.py migrate* in the terminal.
To see if the Django project is setup correctly run the project by using *python3 runserver manage.py* or *./manage.py runserver*. 
Depending on the IDE you may get an error that there is an invalid HTTP_HOST in ALLOWED_HOSTS. 
When this occurs go to the folder with your project name (in this case growing_funds) and open the *settings.py* file. Search in this file for the phrase "ALLOWED_HOSTS".
Enter the address given in the error message in the given brackets, like ALLOWED_HOSTS = ['127.0.0.1'] for instance. When the project is deployed to heroku the heroku address has to be added to this ALLOWED_HOSTS array.



### How to create an app within the main project
Within one project multiple apps can exists, each with their own urls, models, forms, etc. By adding the urls to the urls.py file in the main project, those apps become integrated in the project.

There are multiple apps in this project:
- **projects: ** contains everything regarding the content of a crowdfunding page
- **profile: ** contains everything to make a profile page with user specific information
- **checkout: ** contains everything needed to pledge to project

To add an app to the project enter python3 manage.py startapp <Name app> to the terminal. A directory with the app name will be created in the main directory.

There are few standard files/folders that come along with the creation of an app:
- **__init__.py:** An empty file that tells Python that this directory should be considered a Python package.
- **admin.py:** see next chapter *Django admin backend*
- **migrations folder:** migrations are entirely derived from your models file, and are essentially just a history that Django can roll through to update your database schema to match your current models.
- **models.py:** A model is the single, definitive source of truth about your data. It contains the essential fields and behaviors of the data you’re storing. 
- **tests.py:** for testing scripts
- **views.py:** A view function, or view for short, is a Python function that takes a Web request and returns a Web response.
- **apps.py:** to register the app in the settings.py file under ))INSTALLED_APPS =** . This settings.py is created when making the Django project. This way the apps are integrated in the project.

Some files/folders are created when needed:
- **templates folder for the html files.** Besides the created apps, the main directory has also a templates folder. In the latter the base.html and the allauth html files (for authorisation) are located
- **forms.py:** here the data for the forms are defined
- **contexts.py:** to display the categories on every single page a context.py is needed. As categories are part of the projects app, the context.py file is located in this app.
- **urls.py:** per app the urls are defined. The urls are sort of linked to a view. When this url is entered in the web browser, it will call the corresponding view and will display the html output connected to that view.


## Django admin backend
To access the django portal in the browser, simply add */admin* after the main url (like: <your url.com>/admin).
The portal requests a username and password. This username and password can be created in the terminal by entering *./manage.py createsuperuser*

To be able to see/add/change data from the models in this backend view you need to register the model in the admin.py file.
So in this case to make the fields/data from the app Projects visible in the backend, I need to add the underlining code to the admin.py file (from the Projects folder):

*from django.contrib import admin*
*from .models import Project*

*admin.site.register(Project)*

## Data schema
As the apps are integrated in the project the models from these apps can also interact with each other. So all the models combined will give the data schema for this whole project.
The picture below is the data schema for this project generated with [https://dbdiagram.io/] :

<img src=".\static\img\data_schema.png" alt="data schema" height="25%" width="100%">

The user part is from django.contrib.auth.models that is connected to UserProfile with a OneToMany relation.
UserProfile is connected to the projects and the order model, because the app needs to know who made the project and who pledges to a project.
Category is a single table, making it easier to adjust as an admin from the admin backend, used in the contexts.py
This category table is connected to the projects table in order to link a project to a certain category via a dropdown menu.

## Git(Hub) version control
Git is used to track the changes made and with that to have version control. The following steps are needed to track the changes made in the local repository:

**Step 1: $ git add [file]** Snapshots the file in preparation for versioning. For [file] fill in the (path to the) filename to be versioned.

**Step 2: $ git commit -m "[descriptive message]"** Records file snapshots permanently in version history. In the descriptive message a short description of the changes made are stated.

**Step 3: $ git push [file]** Uploads the local commits to GitHub

Branches where created to experiment with new features by using:
**Step 1: $ git branch [branch name]** To create the branch
**Step 2: $ git checkout [branch name]** To go to that branch to work on and the previous steps to add, commit and push applies.

After the work on the branch is deemed good enough to be deployed it will be merged tot the master branch:
**Step 1: $ git checkout master** To go to the master branch
**Step 2: $ git merge [branch name]** To merge the branch into the master branch


## Deployment on Heroku
When logged on to Heroku (https://www.heroku.com/, registration needed) click the button 'New' and select the option 'Create new app'.
Give the app a name, but be aware that this should be an unique name and not previously used by you or another app on heroku.

Choose region closest by you, because then Heroku will select the edge server that is in that region, making the delivery a bit quicker.
In this case Europe was choosen.

To login to Heroku on the IDE enter 'heroku login' in the terminal and enter your credentials as requested.
However, this will not work on Gitpod. Enter 'heroku login -i' instead and enter your credentials as requested.

By login to Heroku in the IDE a connection is created between the application in the IDE and Heroku 
that would allow to push changes (using Git) to update the application at any given time.

To check if the newly created app is connected enter 'heroku apps' in the terminal. Underneath your e-mail address a list of apps will be listed.
For this particular app 'the-reading-list (eu)' is shown.

As we have already created a Git repository by using the Code Institute template, 
the next step is to add the files needed for this app to the repository by entering:
1. '$ git add .' in the terminal,
2. followed by a '$ git commit -m "message of choice"'

To associate the Heroku app as the master branch enter:
$ heroku git:remote -a the-reading_list

When you push to Heroku at this point it will fail, because two additional files are needed to succesfully deploy to Heroku:
1. requirements.txt : the requirements text file will contain a list of the application that are required for Heroku to run the application.
To create this file enter 'pip3 freeze --local>requirements.txt' in the terminal. A file is then generated and contains the underlining content:

    - asgiref==3.2.10
    - click==7.1.2
    - dj-database-url==0.5.0
    - Django==3.0.8
    - django-allauth==0.42.0
    - django-ckeditor==5.9.0
    - django-countries==6.1.2
    - django-crispy-forms==1.9.1
    - django-js-asset==1.2.2
    - gunicorn==20.0.4
    - itsdangerous==1.1.0
    - oauthlib==3.1.0
    - Pillow==7.2.0
    - psycopg2-binary==2.8.5
    - python3-openid==3.2.0
    - pytz==2020.1
    - requests-oauthlib==1.3.0
    - sqlparse==0.3.1
    - stripe==2.49.0
    - whitenoise==5.1.0

2. Procfile (note that there isn't an extension) : the Procfile is an instruction to Heroku as to which file is used as our entry point at the application.
In other words, which file is used to call the application and run it. To create a Procfile enter 'echo web: python app.py > Procfile'.
A file is created which contains the content: 

    **web: gunicorn growing_funds.wsgi:application**.

Do not forget to add the two files to GitHub, using the previously mentioned git add and git commit.

Now that all files are in place the content can be pushed to Heroku by entering 'git push heroku master' to the terminal.
To run the application with Heroku enter 'heroku ps:scale web=1' to the terminal. 

For the free version only one dyno can be used. 
Dynos are isolated, virtualized Linux containers that are designed to execute code based on a user-specified command.
In this case the web dyno is used. Web dynos are of the "web" process type that is defined in the previously generated Procfile. Only web dynos recieve HTTP traffic from routers.

When this command has run succesfully the sentence 'Scaling dynos... done, now running web at 1:Free' will appear.

The only thing left to do is to specify the IP and port by adding them as configuration variables in Heroku.
1. Login to Heroku and go to the app
2. select the Settings button from the navigation
3. Go to the section 'Config Vars' and click the Add-button
    a. set the Key to 'DATABASE_URL'. Set the value of the postgress address provided by Heroku
    b. set the Key to 'DISABLE_COLLECTSTATIC' if you do not want Heroku to run collectstatic on your behalf.
    c. set the Key to 'EMAIL_HOST_PASS'. Set the value provided by the email host, in this case gmail.
    d. set the Key to 'EMAIL_HOST_USER'. Set the value provided by the email host, in this case an email address from gmail.
    e. set the Key to 'SECRET_KEY'. Set the value to provide cryptographic signing. This key kan be regenerated on https://miniwebtool.com/django-secret-key-generator/
    f. set the Key to 'STRIPE_SECRET_KEY'. API key provided by Stripe Your account’s secret API key can perform any API request to Stripe without restriction.
    g. set the Key to 'STRIPE_PUBLIC_KEY'. API key provided by Stripe are meant solely to identify your account with StripePublishable keys only have the power to create tokens.

Now that it is all setup click the button 'Open app' and the app is deployed.
If a "404 Not Found" appears it is probably due to a missing url in a urls.py. After ('<app_name>/') come the routes needed to make this website work for the purposes specified in the views and named in the urls.py.

## Run Locally
To run locally, this repository can be cloned directly into the editor of your choice by pasting git clone  into your terminal. To cut ties with this GitHub repository, type git remote rm origin into the terminal.

The underlining steps are needed to clone this GitHub repository to another local repository:

**Step 1:** navigate to the repository for this Reading List (login needed) *https://github.com/rory81/the_reading_list*

**Step 2:** click on the green button saying **Clone or download**

**Step 3:** In the Clone with HTTPs section, copy the clone URL (https://github.com/rory81/the_reading_list.git) for the repository

**Step 4:** Go to the IDE that you are using (like for instance Gitpod) and open the terminal

**Step 5:** Type `git clone [URL]`. For [URL] fill in the URL that was copied in step 3 and press Enter


## Testing
1. The pages are validated using:
[HTML validation](https://validator.w3.org/#validate_by_input): the django elements will create an error.
Therefor the pages where run with Chrome and **CTRL+U** was used to "view page source". This source code was entered into the validator.

The following pages where checked and ok.
- project_category.html
- projectdetail.html
- projects.html
- search_projects.html
- startprojectform.html
- terms_and_conditions.html
- checkout.html
- payment_success.html
- profile.html

[CSS validation](https://jigsaw.w3.org/css-validator/#validate_by_input):
[JS validation](https://jshint.com/):
[Python validation](https://extendsclass.com/python-tester.html):
- f'strings aren't recognised in this validator


2. The console was checked for errors:
Only Same-site-cookie warnings where displayed

3. Check forms:

validations were checked:
a) login with a email address unknown to database
b) login with wrong password
c) register with an email address already in database
d) register and not entering the same password twice
e) add a book with amazon link en picture not using the right format
f) check the required fields if they are really required.

4. Check pagination:
There are 5 books per page. The above mentioned number of books per genre were used to test the pagination. Some genres have exactly ten books (exactly 2 pages), 
other genres have one or two books less/more, so that standard number of 5 books per pages do no longer apply, to see if pagination still works.



6. Tested on multiple devices:
Used the standard dev tools from Chrome to test the different devices. Also tested it live on:
- on a 1920 x 1080 screen and one size bigger screen
- tested it on an iPad (old version)
- tested it on an iPhone
- tested it on a android (Samsung Galaxy S20)
- put the project in the peer-code-review put didn't get any comments



## Acknowledgements
- For the basic setup of the environment of the app and its documentation the video's from Code Institute were used
and the Heroku site for a more detailed explanation of some terminology used by Heroku.

- logo picture: https://www.freepik.com/free-vector/piggy-bank-happy-piggy-bank-background_1137678.htm
- stackoverflow: every error that I got went almost through Stack Overflow
- http://gregblogs.com/the-little-things-tlt-django-creating-a-drop-down-list-with-django/
- https://www.youtube.com/watch?v=US_3XvufMLU: to set footer on the bottom of the page
- picture for when no picture is made available: Alsero-Budget-spiekozijn lqkunststoffen.nl
- https://datatables.net/manual/installation for the datatable in the category page
- https://stackoverflow.com/questions/51758405/django-give-date-field-default-value-of-one-month-from-today
- https://stripe.com/docs: to get the payments for a variable amount working
- https://www.youtube.com/watch?v=mF5jzSXb1dc&feature=youtu.be: to get the CKeditor added
- https://sharethis.com/: to get the share button to social media implemented
- the tutors from Code Institute for helping and sparring
- people on Slack when having questions
- my mentor, Maranatha Ilesanmi,for supporting and helping me when needed.
- friends and family willing to test the site for me


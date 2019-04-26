# 551_Python 

## Introduction

This program is 551 Python class individual project written by _**Xinghan Qin**_.

Woo is standed for "world" and "woo", which means say hi to the world. It is a post application which is designed for people to post their daily life and also you can check other's post from the whole world.
For nowaday social app, you can normally only see the posts from people you add friends or the people subscripted. however, on this webside, when people post, no matter who are they and where they from, you can see their post. Everyday can have suprise.

* **Important:** This project's test will be present as a doc file "test.doc"

##

## To run

* On python3, install flask, flask-bcrypt, flask-login, flask mail, flask-sqlalchemy, flask-wtf, markupsafe, pillow, sqlalchemy, wtfform, bcypt, requests

* Go to /Woo

* On terminal: python3 run.py

* Go to a browser and go to localhost/5000 to view the home page

## Features

* Create account:
You can regist an account with username, email and password. the username and email have to be unique

* Update account:
You can change the username, email, password and profile picture of your account

* Delete account:
You can delete your own account

* Post:
You can create a post with title, contents and you can even add a picture

* Update post:
You can modify your post' title contents and picture, where sometimes you find there are some small mistake on your post, you don't have to delete the whole post and create a new one.

* Delete post:
You can delete your own post which you don't want

* Check all posts:
You can check all posts at the home page

* Check user's posts:
You can check a specific user's post by click his or her name

##

## Functions

* **Registor**

  * Username
  
    * Minimum size 2
    * Maximum size 20

  * Email
  
    * An email format
    
  * Password
  
    * will be hashed when account is created
  
  * Comfirm password
  
  * Database:
  
    * All information of this user will be saved in database
  
* **Login**

  * Username
  
    * Minimum size 2
    * Maximum size 20
    * Check username exist in database

  * Password
  
    * According to the username check the password in database

* **Update account**

  * Username
  
    * User's username will be displayed at the begining
    * Minimum size 2
    * Maximum size 20
    * Check username exist in database
    
  * Email
  
    * User's email will be displayed at the begining
    * Check username exist in database

  * Profile picture
  
    * Update a jpg or png file
    
  * Password
  
    * Verify the email to send an link to user's email to change password
    
  * Database:
  
    * All information of this user will be updated in database
    
* **Delete account**

  * Username
  
    * Minimum size 2
    * Maximum size 20
    * Check username exist in database

  * Password
  
    * According to the username check the password in database
    
  * Database:
    
    * All information of this user will be deleted from database
    * All the posts of user will be deleted
    * Profile picture will be deleted from local static path
    
* **Create post**

  * Title

  * Content
  
  * Picture
  
    * Update a jpg or png file
    * Can be empty
    
  * Database:
  
    * All information of this post will be saved in database
    
* **Update post**

  * User
  
    * User has to be the author of this post 

  * Title
  
    * Post's title will be displayed at the begining

  * Content
  
    * Post's contents will be displayed at the begining
  
  * Picture
  
    * Post's picture path will be displayed at the begining
    * Update a jpg or png file
    * Can be empty
    
  * Database:
  
    * All information of this user will be updated in database
    
* **Delete post**
    
  * Database:
  
    * All information of this post will be deleted from database
    * Post picture will be deleted from local static path
    
* **View post**

  * Home
  
    * All posts from world can be seen
    
    * Each page will contain 5 post
    
    * Page bar is at the bottom of the home page
    
  * User
  
    * User's post can be showed by click the User's name on the Post
    
    * All posts from user can be seen
    
    * Each page will contain 5 post
    
    * Page bar is at the bottom of the home page

##

## Design 

* Without login:
  
  * Memu Bar:
  
    * Home
    * About
    * Login
    * Registor
    
  * Posts
  
* With login:
  
  * Memu Bar:
  
    * Home
    * About
    * New Post
    * Account
    * Logout
    
  * Posts

##

## Implementations and Methods

The main methods implement is flask where can create database, and pass the information from UI to database. The website create is from the the Youtube Tutorial:https://www.youtube.com/watch?v=Wfx4YBzg16s

##

## Further Developement

* Improve UI

* Add comment and like function

* Add chat function

## Author

* Xinghan Qin

##

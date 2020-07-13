# Xero Api Workshop - Completed Repository
A workshop given by Xero in collaboration with Women Who Code 

## Introduction

Hi! We're really glad to have you learning with us. This repository is the completed repository for this workshop.  Fork this repository to create your own copy. Then, clone that using your terminal. You'll also want to set up the link between your local version and remote repositories so that any changes you make can be pushed to your version of the master.

This repository has further endpoints. We recommend comparing these endpoints to the ones you've created yourself during this workshop. We also recommend using this as a practice project to take it further by adding a frontend, making more endpoints, or even connecting your own database. 

We've included the getting started section on this repository as well, so you can get the code up and running the way you did for the other workshop repository. 

## Getting Started
### Set Up Repo
* Fork this repository
* Clone your fork to your computer using your terminal

If you need help doing this, follow this tutorial: https://www.digitalocean.com/community/tutorials/fork-clone-make-changes-push-to-github .
### How to get the code running - Mac 
Run these commands in this order.

* pip install flask - this is to install it specifically on your computer 
* python3 -m venv venv
* virtualenv venv
* source venv/bin/activate - use this anytime you want to be in the virtual environment
* pip install flask - this is to install it to your virtual environment 
* Python 
* import flask - this is to check that the install worked 
* CONTROL + Z - to exit the python command line
* export FLASK_APP=storeapi.py - so flask can see our app for the first time
* flask run - run our app, we will keep doing this part over and over 


### How to get the code running - Windows 
If you are using Windows, you'll want to install Gitbash to run these commands. You can download Gitbash here: https://gitforwindows.org/ .

You'll also want to install Pip specifically for Windows, the guide to doing that is here: 
https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation .

Run these commands in this order.

* pip install flask - this is to install it specifically on your computer 
* python3 -m venv venv
* virtualenv venv
* venv\Scripts\activate - use this anytime you want to be in the virtual environment
* pip install flask - this is to install it to your virtual environment 
* Python 
* import flask - this is to check that the install worked 
* CONTROL + Z - to exit the python command line
* export FLASK_APP=storeapi.py - so flask can see our app for the first time
* flask run - run our app, we will keep doing this part over and over 

### How is the repository organized

This repository has all of the files organized based on what is being done in that file. There is a file specifically for the routes, a file for the application being run, and a file for the environmental variables for flask. 

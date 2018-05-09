# Workhub

Our web app is intended to smoothen the workflow between the users and those who are available to do that work.
Simple application with authentication and CRUD functionality using the Python Flask micro-framework.


## Introduction:

 As the crowd increases, the working environment becomes increasingly messy. It is hard to find the people who are available for the particular work that we want to get done. This basically hinders the communication between workers (term used hereon forward to describe those who are available to work) and users (term used hereon forward to describe those who want to employ workers to get their work done). This is where our app comes into play. It fundamentally acts as the intermediator between these two parties. 

## How does it work:
We will provide two login options. One as a user and other as a worker. Once the worker logs in s/he can update relevant information such as their skillset, their availability, experience, region, charge/hour and other professional info (we will keep on adding them to our app as we develop it). Similarly, when the user logs in s/he will have dashboard where the information of available workers extracted from the database (mySql). Workers will have their likes, dislikes display as well. This will be incorporated as the basic functionality for now...

## Future Scope:
We are hoping to further filter our UI such that it becomes minimal as well as modern. The ratings and feedback will be dynamic and associated with the database. User dashboard will have categorical display of workers related info. Info will be sorted based on user reviews, ratings and experience. We are hoping to use google maps API to display the location of workers as well. We will host the site to the live server. We want to provide the functionality to users to add works for future (at least a week). We will also update/alert available workers about this so that they can decide whether to take the work. If they decide to take the work, we will automatically help them to schedule their day. 

## Installation

To use this template, your computer needs:

- [Python 2 or 3](https://python.org)
- [Pip Package Manager](https://pypi.python.org/pypi)

### Backend

Backend uses MySQL Database.
 
Above mentioned workhubdatadump.sql(database dump file) contains database named 'myflaskapp' where all the tables required for this app to run.

### Running the app

```bash
python app.py
```



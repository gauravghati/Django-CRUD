# Django REST APIs

![](https://img.shields.io/badge/Gaurav-Ghati-red)
![](https://img.shields.io/github/languages/top/gauravghati/REST-Django)
![](https://img.shields.io/github/last-commit/gauravghati/REST-Django)

Basic Django - REST framework for learning REST architecture

I had Created a basic 2 REST APIs for Understanding architecture of the REST framework and implemented it with Django-rest-framework

## 1) Signup API
#### GET request: 
    Return the list of all the users, where each object of the list is python dictionary (JSON format)
    
    Example of object in list
    
    dict = {
      'name' : "gaurav",
      'age' : 20,
      'phone': "9999999999"
    }

#### POST request: 
    Get Data of the perticular user in the JSON given below
    
    dict = {
      'name' : "gaurav"
      'age' : 20,
      'phone': "9999999999"
    }
    
    Save or perform whatever backend logic on the data.
    Again, Returning the same data in form of JSON!

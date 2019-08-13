# jsonb_sqlalchemy
This project demonstrate use of JSONB feature of postgresql using flask-sqlalchemy.
Following are setps that needs to be followed for setting up this project

# Cretaing virtual env and installing packages
    $ virtualenv env
    
    $ source env/bin/activate
    
    $ pip install -r requirements.txt
    
# Setting up database
    -change SQLALCHEMY_DATABASE_URI located in config.py file according to your database configuration
    -Run commad 
    $ python create_db.py in project root folder to create necessary tables for project.
    
# Running application
   Run command : $ python run.py 

    
   

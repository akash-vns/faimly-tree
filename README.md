# family-tree

### About  ###

* Family tree is represent the nested structure of DB relation in Django
* Its sample of the tree based Data structure  
* we can create here child of child structure with n number of children 

(Docker) run and helpful commands
------------
App going to runn on 127.0.0.1:8001 
* for creating virtual env run, it will also install a project related requirements  
    - make setup_python_env
* to start project 
    - make start
* to dump dummy data (create a fixture file are into the todo app)
  - make dummy_data
* to rebuild app
  - make rebuild
* to restart
  - make restart
* to loaddata in to database (used fixture file from todo app)
  - make loaddata
* to perform or you have to run any terminal command you have to use
  - make shell
* to run test 
  - make test
* to migrate and run makemigrations 
  - make migrate / makemigrations
  

(Manually) run and helpful commands (Linux)
------------
* for initial setup  
    - sh setup.sh
  
* for initial data  
    - sh loaddata.sh
  
* for dump data to fixture data  
    - sh dumpdata.sh
* for runserver  
    - sh runserver.sh

For the Api's
------------
as of now API render with default rest api Template render response , to make simple as it is. 
and also you can filter the data with member (is family Model object) and relation (like children or sibling etc.)

- url : loclhost:8001/api/



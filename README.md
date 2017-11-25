# build-a-blog

Testing Plan:
1. Clone project into new directory
2. If necessary, install pymysql and sqlalchemy into your virtual environment
3. Initialize MAMP and open start page to add user account:

   username: build-a-blog
   
   password: buildablog
   
4. In project directory start python shell ($ python)
5. Initialize the db. In command line type: 

   a.  'from main import db, Blog'
   
   b.  'db.create_all()'
   
   c.  'db.session.commit()'
   
   d.  'exit()'
   
6. To run, type 'python main.py' in terminal
7. Navigate browser to 'localhost:5000'

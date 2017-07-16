from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:buildablog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(600))

    def __init__(self, title, body):
        self.title = title
        self.body = body


#TODO add helper functions, clean up /home
#TODO flash messages


@app.route('/', methods=['POST', 'GET'])
def index():

    '''
    route for homepage, checks against GET or POST requests, validates user input, displays applicable errors, submits info to db if no errors
    
    '''

    if request.method=='GET': # checks for GET request
        blog_id = request.args.get('id') # grabs blog id from query params
        if blog_id: # if query params exist...
            blog = Blog.query.filter_by(id=blog_id).first() # matches query param blog id with blog post in db 
            #selected_blog = Blog.query.filter_by(id=blog_id).first() 
            return render_template('home.html', blog_id=blog_id, body=blog.body, main_title=blog.title) # renders template with single blog post
        
        # if there are no query params in GET request, display ALL blogs
        blog = Blog.query.all() # gets all blog posts from db
        main_title = "Build a Blog" 
        return render_template('home.html', blog=blog, main_title=main_title) # renders template on /home with ALL blog posts
        
        

    error_title = "Please fill in the title"
    error_body = "Please fill in the body"

    if request.method == 'POST': # checks to see if user submitted blog post data
        
        title = request.form['title'] # grabs user input for blog title
        body = request.form['body'] # grabs user input for blog body
        if title and body != "": # checks to see if content has been entered   
            new_post = Blog(title,body) # storing blog title and body in a new variable
            db.session.add(new_post) # adding new blog post to session
            db.session.commit() # committing new blog post to db
            return redirect("/?id=" + str(new_post.id)) # redirects user to home page that only displays the newly submitted post

        if body == "": # shows error if no input for blog body
            return render_template('/newpost.html', error_body=error_body)

        if title == "": # shows error if no input for blog title
            return render_template('/newpost.html', error_title=error_title)



@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    '''
    route for newpost, renders newpost template
    
    '''

    return render_template('newpost.html')



if __name__ == '__main__':
    app.run()
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


@app.route('/', methods=['POST', 'GET'])
def index():

    error_title = "Please fill in the title"
    error_body = "Please fill in the body"

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        if title and body != "":    
            new_post = Blog(title,body)
            db.session.add(new_post)
            db.session.commit()

        if body == "":
                return render_template('/newpost.html', error_body=error_body)

        if title == "":
            return render_template('/newpost.html', error_title=error_title)

    #if request.method == 'GET':

        #query_params = request.args.get('body')
        #return render_template('home.html' + query_params)

    blog = Blog.query.all()
    #print(blog)
    return render_template('home.html', blog=blog)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():


    return render_template('newpost.html')



if __name__ == '__main__':
    app.run()
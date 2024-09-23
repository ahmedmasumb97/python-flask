from flask import Flask,request,render_template,jsonify
import requests
from models import db,Contact




app = Flask(__name__)


# database add


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# initialize the app with the extension
db.init_app(app)


# create database tables
with app.app_context():
    db.create_all()


@app.route('/')
def homepage():
    return 'Welcome to the API!'

@app.route('/welcome')
def welcome():
    return 'Welcome to page'

@app.route('/project')
@app.route('/project/task')
def project_task():
    return 'welcome to our page'
@app.route('/dashbord')
@app.route('/dashbord/<id>')
def dashboard(id= 'Guest'):
    return f'Welcome to dashboard {id}'

@app.route("/task/<int:greeting>/<int:username>")
def greeting(greeting,username):
    return f'Welcome to dashboard {greeting} {username}'

@app.route('/task_list')
def task_list():
    name = 'Ahmed masum'
    age = 18
    fruits = ['apple', 'banana', 'orange','multa','pineapple','mango','plum']
    return render_template('index.html',name = name,age= age, fruits = fruits)


@app.route('/login', methods = ["GET","POST"])
def login():
    error = True

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        message = request.form.get('message')
        
        new_contact = Contact(
            username = username,
            password = password,  
            email = username + "@example.com",
            message = message
        )
        
        db.session.add(new_contact)
        db.session.commit()

        # if username == 'admin' and password == 'admin':
        #     error = False
        #     return render_template('login.html' ,username=username,)
        # else:
        #     error = True
        #     return render_template('login.html', error = error)
    return render_template('login.html')



@app.route('/contacts')
def contact():
    contacts = Contact.query.all()
    return render_template('contact.html', contacts=contacts)
    
    
@app.route('/app/json')
def jsonfile():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    
    country = ['Bangladesh','United States', 'Canada', 'France', 'Germany', 'Italy']
    return jsonify({'data': data},{'country': country})


@app.route('/posts')
def posts():
    respose = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = respose.json()
    return render_template('json.html',data=data)


@app.route('/posts/<int:post_id>')
def post(post_id):


    respose = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    data = respose.json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
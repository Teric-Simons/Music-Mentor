from app import app
import smtplib
import os

#, db, login_manager
from .models import *
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
#from app.models import UserProfile
from flask_wtf.csrf import generate_csrf
from app.forms import LoginForm, UploadForm
from . import db
from werkzeug.security import check_password_hash
from flask import send_from_directory
from flask import jsonify
from functools import wraps
from .forms import *
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
###
# Routing for your application.
###
db.create_all()

def tokencheck(f):
    @wraps(f)
    def decorated_function(*args, **kws):
            login = ""
            if not 'Authorization' in request.headers:
                return jsonify({"error": "Incorrent token!"}), 400
            token = request.headers["Authorization"].split(" ")[1]
            try:
                login = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            except:
                return jsonify({"error": "token missing!"}), 400
            return f(*args, **kws)    
    return decorated_function



@app.route('/api/search',  methods=['GET','POST'])
def search():
    data = request.get_json()
    search = data['search'].lower()
    slist = search.split(" ")
    uploads = Upload.query.all()
    uploads2 = []

    for key in slist:
        for upload in uploads:
            print(key, upload.title)
            if upload.title.lower().find(key) != -1 and upload not in uploads2:
                print(upload.title)
                uploads2.append(upload)

        

    
    upload_List = []
    for upload in uploads2:
        upload_data = {
            'id': upload.id,
            'title': upload.title,
            'composer': upload.composer,
            'genre':upload.genre,
            'instrument':upload.instrument,
            'sheet': "/api/photo/"+ upload.sheet
            
        
        }
        upload_List.append(upload_data)
        
    return jsonify({'upload': upload_List})


@app.route("/api/photo/<filename>", methods=['GET'])
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)


@app.route('/api/getTutors',  methods=['GET','POST'])
def getTutors():

    tutors = db.session.query(Users, Tutors).filter(Users.email == Tutors.email).all()
    
    
    print(tutors)
    
    tutor_List = []
    for tutor in tutors:
        students = db.session.query(Users, Book).filter(Users.email == Book.email_booker, Book.email_bookee == tutor[0].email).all()
      
        tut = {
            'fname': tutor[0].firstname,
            'lname': tutor[0].lastname,
            'name': tutor[0].firstname + " " +tutor[0].lastname,
            'email': tutor[0].email,
            'instrument': tutor[1].instrument,
            'language': tutor[1].language,
            'description': tutor[1].description,
            'price': int(tutor[1].price) * 145,
            'isSuper':      tutor[1].isSuper,
            'isrlly':      "Yes" if tutor[1].isSuper else "No",
            'nationality': tutor[1].countryOfBirth,
            'numbook' : len(students),
            'imglink' : tutor[1].imglink,
            'video' : tutor[1].video
        }
        tutor_List.append(tut)
    print(tutor_List)
        
    return jsonify({'tutors': tutor_List})



@app.route('/api/getStudents',  methods=['GET','POST'])
def getStudents():
    
 
    tutors = db.session.query(Users, Book).filter(Users.email == Book.email_booker, Book.email_bookee == session['email']).all()
    print(tutors)

   
    
    tutor_List = []
    for tutor in tutors:
     
        tut = {
            'fname': tutor[0].firstname,
            'lname': tutor[0].lastname,
            'email': tutor[0].email,
            'start': tutor[1].fromm,
            'end': tutor[1].fromm
        }
        print(tut)
        tutor_List.append(tut)
    print(tutor_List)
        
    return jsonify({'tutors': tutor_List})




@app.route('/api/getMessages',  methods=['GET','POST'])
def getMessages():
    
    print("messagess")
    tutors = db.session.query(Users, Message).filter(Users.email == Message.fromm, Message.to == session['email']).all()


   
    
    tutor_List = []
    for tutor in tutors:
        date = tutor[1].date.date()
        print( tutor[1].message)
     
        tut = {
            'id': tutor[1].id,
            'fname': tutor[0].firstname,
            'lname': tutor[0].lastname,
            'email': tutor[0].email,
            'messsage': tutor[1].message,
            'date' : date
       
        
        }
        print(tut)
        tutor_List.append(tut)
    print(tutor_List)
        
    return jsonify({'tutors': tutor_List})


@app.route('/api/bee',  methods=['GET','POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        print("fsffd")
        title  = request.form['title']
        composer  = request.form['composer']
        genre = request.form['genre']
        instrument = request.form['instrument']
        sheet = request.files['file']
        filename = secure_filename(sheet.filename)
        sheet.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        
        # Save the movie to the database
        movie = Upload(title, composer, genre, instrument, filename)
        db.session.add(movie)
        db.session.commit()

        # Return a success message in JSON format
        response = {
            'message': 'Upload Succesful'
        }
        return jsonify(response)
    else:
        # Return a list of errors in JSON format
        errors = form_errors(form)
        response = {'errors': errors}
        print("hey")
        return jsonify(response), 400

       
@app.route("/api/register", methods=['GET','POST'])
def register():  
    form = RegisterForm()
    print("im here yay")
    if form.validate_on_submit():
        print("im here yay2")
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
    
        
  
        user = Users.query.filter_by(email=email).first()

       

        
        if user:
            print(jsonify({"error": "Email associated with another account"}))
            return jsonify({"errors": ["Email associated with another account"]}), 400
        
        if len(password) < 7:
             return jsonify({"errors": ["Password must be atleast 6 characters"]}), 400

        user = Users(password=generate_password_hash(password, method='pbkdf2:sha256'),firstname=firstname,lastname=lastname,email=email)

        db.session.add(user)
        try:
            db.session.commit()
            data = {}
            data['id'] = user.id
            session['id'] = user.id
            session['fname'] = user.firstname
            session['email'] = user.email
         
            token = jwt.encode({}, app.config["SECRET_KEY"], algorithm="HS256")
            tut = Tutors.query.filter_by(email = email).all()
            print(tut)
            if tut == None or len(tut) < 1:
                session['tutor'] = False
            else:
                session['tutor'] = "True"
            response ={
                "message": "User successfully logged in",
                        "token": token,
                        "fname": user.firstname,
                        "email":email,
                        'tutor':session['tutor']
             
            }
            return jsonify(response)
        except Exception as e:
            return jsonify({"error":"Failed to register"}), 400
    else: 
        errors = form_errors(form)
        response = {"errors": errors}
        return jsonify(response), 400
    

@app.route("/api/sendMessage", methods=["POST", "GET"])
def sendMessage():
    form = MessageForm()
    print("mess")
    if form.validate_on_submit():
        message = request.form['message']
        to = request.form["to"]
        message = Message(to = to, message = message, fromm = session['email'])
        
        db.session.add(message)
        db.session.commit()
        response ={
                "message": "Successfully registered",
             
            }
        return jsonify(response)
    else: 
        errors = form_errors(form)
        response = {"errors": errors}
        return jsonify(response), 400
    

    
@app.route("/api/book", methods=["POST", "GET"])
def book():
    data = request.get_json()
   

    print("mess")
 
    to = data['to']
    fromm = data['from']
    booker = data['booker']
    print(booker)
    book = Book(to = to, fromm = fromm, email_bookee = booker,  email_booker = session['email'])
    

    Message = "Congratulations " + session['fname'] + " you have successfully registered.\nPlease visit this link to continue attending classes -> [[examplezoomlink.com]]"
    subject = "MUSIC MENTOR"
    
    message = 'Subject: {}\n\n{}'.format(subject, Message)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('tericsimons12@gmail.com', 'ccan phrf rhau kozi')
    server.sendmail('tericsimons12@gmail.com', 'tericsimons12@gmail.com', message)
    db.session.add(book)
    db.session.commit()

    response ={
            "message": "Successfully registered",
            
        }
    return jsonify(response)

   
    


@app.route("/api/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    print("login1")
    if form.validate_on_submit():
        print("login2")
        email = request.form['email']
        password = request.form['password']
        user = Users.query.filter_by(email=email).first()
        tut = Tutors.query.filter_by(email = email).all()
        print(tut)
        if tut == None or len(tut) < 1:
            session['tutor'] = False
            session['price'] = 0
        else:
            session['tutor'] = "True"
            session['price'] = tut[0].price
        fail = False
        if user is None or not check_password_hash(user.password, password):
            if user.password.lower() != password.lower():
                flash('Incorrect login information')
                return jsonify({'errors': ["Incorrect Username or Password"]})
            
        data = {}
        data['id'] = user.id
        session['id'] = user.id
        session['fname'] = user.firstname
        session['email'] = user.email
        
        token = jwt.encode(data, app.config["SECRET_KEY"], algorithm="HS256")
      
        return jsonify({"message": "User successfully logged in",
                        "token": token,
                        "fname": user.firstname,
                        "email":email,
                        'tutor':session['tutor'],
                        "price" :session['price']
                        })
    else:
        errors = form_errors(form)
        response = {'errors': errors}
        return jsonify(response), 400
    



      

@app.route("/api/becomeTutor", methods=["POST", "GET"])
def becomeTutor():
    print(session['email'])
    tutor = Tutors(email = session['email'])
    db.session.add(tutor)
    try:
        db.session.commit()
        return jsonify({"message": "I became a tutor!"})
         
    except Exception as e:
        return jsonify({"error":"Failed to register"}), 400
    



@app.route("/api/v1/auth/logout", methods=["POST"])
def logout():
    return jsonify({"message": "Succesfully logged out"})


@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
 return jsonify({'csrf_token': generate_csrf()})

def find(title):
    dic = {"Title" : "Fur Elise piano Composition", "Composer": "Beethoven", "Genre" : "Hop Hop", "Instruments" : "Piano"}
    lit = []
    to_return = []
    for i in range(100):
        lit.append(dic)
    for i in lit:
        if title in dic["Title"]:
            to_return.append(i)
    print(to_return)
    return to_return


def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message =  (
                    error
                )
            error_messages.append(message)

    return error_messages

    













@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
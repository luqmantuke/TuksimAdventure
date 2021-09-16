# TuksimAdventure
This is a Tourism/Travel WebApp made with Python Django and Bootstrap. 

# Links
Visit the website <br> https://tuksim.herokuapp.com/ <br>
Watch Intro youtube video <br> https://www.youtube.com/watch?v=XGqU4iH1T5E

# Technologies Used
Python Django <br>
Bootstrap 4 <br>
AWS(For media storage) <br>
Heroku(For Hosting) <br>
Mylivechat(For livechat support) <br>


# Features
Admin Panel ✅  <br>
Tour Management System ✅ <br>
Booking System ✅ <br>
Email Automation Once Customer Contacts Or Book ✅ <br>
Live Support ✅ <br>
Blog ✅ <br>
Contact System ✅ <br>
Clean UI With Animations ✅  <br>
Responsive UI ✅  <br>
Dynamic Webapp ✅  <br>
Whatsapp  ✅  <br>

# Accessing the WebApp Admin 
Visit the admin page https://tuksim.herokuapp.com/revoltadmin <br>
Login with the following administration credentials <br>
 username: <b> tdc <br>
 password <b> 123456
# How To Use This WebApp

Firstly, this webapp is powered by Django Framework so you need Pyhon in your machine. Next, you need an AWS account for storing media. Create an AWS account
and create a bucket. This video might help you out. https://www.youtube.com/watch?v=i4YFFWcyeFM <br>

Next, you will need a private email I used a privateemail.com because I didn't have to worry about Gmail security issues that raise everytime when you use their smtp(But it's your choice)
<br>

# Configure Your App 
Head up to tuksimadventures/settings.py and edit these fields with your AWS bucket and email <br>
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'<br>
DEFAULT_FROM_EMAIL = 'EMAIL HERE EXAMPLE luqman@gmail.com'<br>
EMAIL_HOST = 'EMAIL HOST HERE EXAMPLE mail.gmail.com'<br>
EMAIL_HOST_USER = 'EMAIL HOST USER'<br>
EMAIL_HOST_PASSWORD = 'YOUR PASSWORD'<br>
EMAIL_PORT = 587<br>
EMAIL_USE_TLS = True<br>
FAIL_SILENTLY = False<br>

<br>
# AWS MEDIA FILE STORAGE
AWS_ACCESS_KEY_ID = 'AWS KEY ID HERE'<br>
AWS_SECRET_ACCESS_KEY = 'AWS SECRET KEY'<br>
AWS_STORAGE_BUCKET_NAME = 'AWS STORAGE NAME'<br>
 AWS_S3_REGION_NAME = 'us-east-'<br>
 AWS_S3_SIGNATURE_VERSION = 's3v4'<br>
AWS_S3_FILE_OVERWRITE = False<br>
AWS_DEFAULT_ACL = None<br>
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'<br>

Now search for all "tuksimadventures@gmail.com" and place your email that you need to get automated emails once they are automated by the smtp once the user contacts you, books e.t.c <br>

# Run Your WebApp
Clone the project git clone https://github.com/luqmantuke/TuksimAdventure.git  <br> 

Open the project and open terminal/cmd(make sure you've activated your Python environment)  <br> 
$ pip install -r requirements.txt to get packages  <br> 
$ python manage.py runserver to run your server

# Issues
If you've any issue throw me a DM on Twitter https://twitter.com/tuke2911 or open an issue.



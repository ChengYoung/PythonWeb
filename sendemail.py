import os
from flask import Flask
from flask_mail import Mail

#configuration
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.163.com'
app.config['MAIL_PORT']=25
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWARD']=os.environ.get('MAIL_PASSWARD')

mail = Mail(app)

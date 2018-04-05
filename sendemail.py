import os
from flask import Flask
from flask_mail import Mail
from flask_script import Manager

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.163.com'
app.config['MAIL_PORT']=465
#app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')

mail = Mail(app)
manager = Manager(app)


if __name__=='__main__':
    manager.run()

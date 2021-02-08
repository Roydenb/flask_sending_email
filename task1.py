from flask import render_template, Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/about/')
def about():
    return render_template("about.html")

from smtplib import SMTP
from configure import con

@app.route('/send-email/')
def mail():
    try:
        sender_email = "jaydendane2@gmail.com"
        receiver_email = "jaydendane2@gmail.com"
        password = ['password']
        server = SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(sender_email, password )
        server.sendmail(sender_email, receiver_email, 'This is a test email.')
        print("the message has been successfully sent")

    except Exception as err:
        print("Something went wrong..", err)
    finally:
        server.close()




# REMEMBER THAT THE REQUIREMENT FILE NEED TO BE ADDED TO GIT AS WELL IN ORDER TO HAVE IT PUSHED TO HEROKU
# NEED TO BE THE HEROKU MAIN (GIT PUSH HEROKU MAIN)
# HEROKU LOGS --TAIL ON THE TERMINAL IF YU DON'T UNDERSTAND
# --TAIL (GIVES YOU THE LAST 10 LINES) TO SEE THE LOGS OF A WEB SERVER

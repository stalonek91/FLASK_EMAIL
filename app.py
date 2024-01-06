from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sojka.sylwester.dev@gmail.com'
app.config['MAIL_PASSWORD'] = 'pidnvsncidfksqge'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = ('Sylwcio', 'sojka.sylwester.dev@gmail.com')
app.config['MAIL_DEBUG'] = True

mail = Mail()
mail.init_app(app)

@app.route('/')
def index():
    mail_message = Message("CZEMSC!",
                           sender=('PAN SYLWEK','sojka.sylwester.dev@gmail.com'),
                           recipients=['sojka.sylwester.dev@gmail.com']
                           )
    # mail_message.body = 'NO HEJKA! :)'
    mail_message.add_recipient('andrzejh07@gmail.com')
    #wersja z htmlem

    mail_message.html = '<h1>Kwiczek</h1>'

    # adding attachements

    with app.open_resource('ticket.pdf') as file:
        mail_message.attach('bilecik','application/pdf',file.read())

    mail.send(mail_message)

    return f'SENT!'

@app.route('/bulk')
def bulk():

    users = [
        {'name': 'Sylwek', 'email':'cykor13@gmail.com'},
        {'name': 'Kasia', 'email':'sojka.sylwester.dev@gmail.com'}
        ]
    
    with mail.connect() as conn:
        for user in users:
            msg = Message('Bulk_mail', recipients=[user['email']])
            msg.body = f'Siemka: {user["name"]}'
            conn.send(msg)
    
    return f'BULK POSOL'

if __name__ == '__main__':
    app.run(debug=True)
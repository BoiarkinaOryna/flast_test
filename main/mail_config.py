from .settings import main
from flask_mail import Mail, Message

main.config['MAIL_SERVER'] = 'smtp.gmail.com'
main.config['MAIL_PORT'] = 587
main.config['MAIL_USE_TLS'] = True
main.config['MAIL_USE_SSL'] = False
main.config['MAIL_USERNAME'] = 'boyarkina.ar@gmail.com'
main.config['MAIL_PASSWORD'] = 'jgli fgcl lnbu ieci'
# main.config['MAIL_PASSWORD'] = 'djiw yjpu zujg hxls'
main.config['MAIL_DEFAULT_SENDER'] = "boyarkina.ar@gmail.com"

mail = Mail(app = main)
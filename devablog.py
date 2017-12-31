from app import app, db
from app.models import User, Post

import os


# Configuring Devasoft Mail
"""
os.environ["MAIL_SERVER"] = "devasoft.com.br"
os.environ["MAIL_PORT"] = "465"
os.environ["MAIL_USE_TLS"] = "1"
os.environ["MAIL_USERNAME"] = "blog@devasoft.com.br"
os.environ["MAIL_PASSWORD"] = "senhablog"
"""

"""
export MAIL_SERVER="devasoft.com.br"
export MAIL_PORT="465"
export MAIL_USE_TLS="1"
export MAIL_USERNAME="blog@devasoft.com.br"
export MAIL_PASSWORD="senhablog"
"""




# Configuring Google Mail
"""
os.environ["MAIL_SERVER"] = "smtp.googlemail.com"
os.environ["MAIL_PORT"] = "587"
os.environ["MAIL_USE_TLS"] = "1"
os.environ["MAIL_USERNAME"] = "devanagarisoftware@gmail.com"
os.environ["MAIL_PASSWORD"] = "senhadeva"
"""

"""
export MAIL_SERVER="smtp.googlemail.com"
export MAIL_PORT="587"
export MAIL_USE_TLS="1"
export MAIL_USERNAME="devanagarisoftware@gmail.com"
export MAIL_PASSWORD="senhadeva"
"""


@app.shell_context_processor
def make_shell_context():
    context = dict()
    context['db'] = db;
    context['Post'] = Post;
    context['User'] = User;

    return context
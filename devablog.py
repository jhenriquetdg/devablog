import os

from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    context = dict()
    context['db'] = db;
    context['Post'] = Post;
    context['User'] = User;

    return context


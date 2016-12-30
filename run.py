# -*- coding: utf-8 -*-
_author_ = 'Pylar'
#!flask/bin/python
from app import create_app
import os
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.run(debug = True)

# -*- coding: utf-8 -*-
_author_ = 'Pylar'
from flask import Blueprint
auth = Blueprint('auth', __name__)

from . import views
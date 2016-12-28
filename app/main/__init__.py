# -*- coding: utf-8 -*-
_author_ = 'Pylar'
from flask import Blueprint
main = Blueprint('main', __name__)

from . import views, errors
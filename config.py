# -*- coding: utf-8 -*-
_author_ = 'Pylar'
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'haha'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 设置这一项是每次请求结束后都会自动提交数据库中的变动
    SQLALCHEMY_TRACK_MODIFICATIONS= True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'wxmy419@163.com'
    MAIL_PASSWORD = 'a123456'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'wxmy419@163.com'
    FLASKY_ADMIN = '1483287009@qq.com'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost:3306/test'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost:3306/test1'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost:3306/test2'


config = {

    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
from flask import Blueprint, g, jsonify, render_template, flash, redirect, url_for, request
from flask import current_app as app
from flask_restful import Api
from app.models.user import User

from app.api.resources.user_resource import UsersResource

API_BP = Blueprint('api', __name__)
API = Api(API_BP)

API.add_resource(UsersResource, '/users/')

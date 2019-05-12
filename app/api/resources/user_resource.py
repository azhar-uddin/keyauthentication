from flask_restful import Resource
from flask import current_app as app, request, render_template, make_response
from app.models.user import User
from app.decorators.key_authentication import require_appkey
from app.serializers.user import UserSchema

class UsersResource(Resource):

    @require_appkey
    def get(self):
        try:
            users = User.find_all()
            user_schema = UserSchema(many=True)
            return{"status": "success", "users":user_schema.dump(users).data}, 200
        except Exception as ex:
            return {'status': 'error', 'message': str(ex)}, 100

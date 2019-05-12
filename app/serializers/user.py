from app.models import ma

class UserSchema(ma.Schema):

    class Meta:
        fields = ('email', 'name')

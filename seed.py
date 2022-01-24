from app import db
from models import Pet

db.drop_all()
db.create_all()

mario = Pet(name='Mario', species='dog', photo_url='https://media.istockphoto.com/photos/tiny-funny-small-dog-picture-id186391783')
luigi = Pet(name='Luigi', species='dog', photo_url='https://i.ytimg.com/vi/JAT_oSFPvyc/hqdefault.jpg')
db.session.add_all([mario, luigi])
db.session.commit()

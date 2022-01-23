from app import db
from models import Pet

db.drop_all()
db.create_all()

# u = User(name="Jane", email="jane@jane.com")
mario = Pet(name='Mario', species='dog')
luigi = Pet(name='Luigi', species='dog')
db.session.add_all([mario, luigi])
db.session.commit()

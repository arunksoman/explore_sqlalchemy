from models import User, db

ins = User(username='arun12', email='arun12@gmail.com', password='abcde')
db.add(ins)
# u = db.query(User).filter_by(id=2).all()
u = User.query.all()
User.pretty_print(u)

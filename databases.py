from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name,size,color,price):
	product_object=Product(name=name, 
		size=size, 
		color=color,
		price=price)
	session.add(product_object)
	session.commit()
  #TODO: complete the functions (you will need to change the function's inputs)



def update_product(name,color):
	
	product_object = session.query(
		Product).filter_by(
		name=name).first()
	product_object.color=color
	session.commit()





  
  
def delete_product(name):
	session.query(Product).filter_by(
		name=name).delete()
	session.commit()

  

def get_product(id):
  pass

create_product("shirt",14,"yellow",50)
create_product("hat",6,"red",15)
update_product("hat", "blue")

delete_product("shirt")
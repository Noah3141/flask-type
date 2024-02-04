from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session as DbSession
from sqlalchemy.orm.session import sessionmaker

Base = automap_base()

engine = create_engine("mysql://root:hb3f12d5aefc3G2ga412bfBddG-bA6Fg@viaduct.proxy.rlwy.net:54672/railway")

Base.prepare(autoload_with=engine)


User = Base.classes.Users


Session = sessionmaker(bind=engine)
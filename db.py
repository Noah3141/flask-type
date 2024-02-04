from typing import NamedTuple
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker


engine = create_engine("mysql://root:hb3f12d5aefc3G2ga412bfBddG-bA6Fg@viaduct.proxy.rlwy.net:54672/railway")


AutoBase = automap_base()
AutoBase.prepare(autoload_with=engine)
Organization = AutoBase.classes.orgs

#

Session = sessionmaker(bind=engine)



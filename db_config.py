import motor

host = '127.0.0.1'
port = 27017

# todo add reading config from .yaml file
db_client = motor.MotorClient(host, port).db

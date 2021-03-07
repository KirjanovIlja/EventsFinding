import pymongo
from config import *


client = pymongo.MongoClient(
    'mongodb+srv://ilja1234:ilja1234@cluster0.vh3nn.mongodb.net/Events?retryWrites=true&w=majority'
    )

db = client.Events

concerts = db.concerts
from pymongo import MongoClient
client = MongoClient('mongodb+srv://amanmaurya8419:Aman1234@cluster0.cmojrdr.mongodb.net/?retryWrites=true&w=majority')
db = client['PORTFOLIOMANAGER']
user = db['users']
projects=db['projects']
tasks=db['tasks']
resource=db['resources']
activeUser=db['activeUser']
count=db['counter']
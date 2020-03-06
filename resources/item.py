import sqlite3
from flask_restful import  Resource, reqparse, request
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    

    parser = reqparse.RequestParser()
    parser.add_argument("features",
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    #@jwt_required()
    def get(self, name):  
        item =ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'},404     


    def post(self,name):
        if ItemModel.find_by_name(name):
            return{'message':'An item name: {} already exist'.format(name)},400

        data = request.get_json() 
        #data = Item.parser.parse_args()
        #for key, value in data["features"].:
            #print(key, value)
        #cordinates = data["features"]
        #Score = data["features"][0]['properties']['Score']
        meldID= data["meldID"]
        date =data["date"]
        toelichting = data["toelichting"]
        telephone = data["telephone"]
        Email = data["Email"]
        categorie = data["Email"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        #return {"message":cordinates[1]}
        #item =ItemModel(name, Score,cordinates[0],cordinates[1])
        item =ItemModel(meldID,date,name,telephone,Email,categorie,toelichting,latitude,longitude)

  

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"},500 #500 internal server error

        return item.json(), 201 # This returns the code for 201 which means created when the server creates data #202 is accepted delays creating items

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':'data deleted successfully'}


    def put(self, name):
        #data = Item.parser.parse_args()
        data = request.get_json()

       #Score = data["features"][0]['properties']['Score']
        meldID= data["meldID"]
        date =data["date"]
        toelichting = data["toelichting"]
        telephone = data["telephone"]
        Email = data["Email"]
        categorie = data["Email"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        #data = request.get_json()
        item =ItemModel.find_by_name(name)        
        updated_item = ItemModel(meldID,date,name,telephone,Email,categorie,toelichting,latitude,longitude)

        if item is None:
            item =ItemModel(meldID,date,name,telephone,Email,categorie,toelichting,latitude,longitude)
        else:
            item.Score = Score
            item.latitude = cordinates[0]
            item.longitude = cordinates[1]
        item.save_to_db()

        return updated_item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]} #list comprehension
        #{'items': list(map(lambda x:x.json(), ItemModel.query.all()))} lambda function 

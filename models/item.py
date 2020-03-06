import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__='geometry_columns'

    id = db.Column(db.Integer, primary_key=True)    
    meldID = db.Column(db.String(80)) 
    date = db.Column(db.String(80))
    name = db.Column(db.String(80))       
    telephone = db.Column(db.Integer(80))
    Email = db.Column(db.String(80))
    categorie = db.Column(db.String(80))
    toelichting = db.Column(db.String(80))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    

    def __init__(self, date,name, meldID, telephone,Email,categorie,toelichting,latitude,longitude):
        self.meldID = meldID
        self.date = date
        self.name = name
        self.Email=Email
        self.telephone=telephone
        self.categorie = categorie
        self.toelichting = toelichting
        self.latitude = latitude
        self.longitude = longitude

    def json(self):
        return{ 'id':self.meldID,"date":self.date,'name':self.name,'telephone':self.telephone,'email':self.Email,'categorie':self.categorie,'toelichting':self.toelichting,'latitude':self.latitude,'longitude':self.longitude}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1


  
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    #@classmethod
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()




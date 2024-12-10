from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PollingUnit(db.Model):
    __tablename__ = 'polling_unit'
    uniqueid = db.Column(db.Integer, primary_key=True)
    polling_unit_id = db.Column(db.Integer)
    ward_id = db.Column(db.Integer)
    lga_id = db.Column(db.Integer)
    state_id = db.Column(db.Integer)

class AnnouncedPUResults(db.Model):
    __tablename__ = 'announced_pu_results'
    result_id = db.Column(db.Integer, primary_key=True)
    polling_unit_uniqueid = db.Column(db.Integer, db.ForeignKey('polling_unit.uniqueid'))
    party_abbreviation = db.Column(db.String(4))
    party_score = db.Column(db.Integer)

class LGA(db.Model):
    __tablename__ = 'lga'
    uniqueid = db.Column(db.Integer, primary_key=True)
    lga_id = db.Column(db.Integer)
    lga_name = db.Column(db.String(50))
    state_id = db.Column(db.Integer)

class AnnouncedLGAResults(db.Model):
    __tablename__ = 'announced_lga_results'
    result_id = db.Column(db.Integer, primary_key=True)
    lga_name = db.Column(db.String(50))
    party_abbreviation = db.Column(db.String(4))
    party_score = db.Column(db.Integer)
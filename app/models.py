#!/usr/bin/env python3
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    sport = db.Column(db.String(50), nullable=False)
    team = db.Column(db.String(50))
    position = db.Column(db.String(50))
    stats = db.Column(db.JSON)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Player {self.name} ({self.sport})>"

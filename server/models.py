from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Must add a name")
        return name
    
    @validates('phone_number')
    def validate_number(self, key, phone):
        if len(phone) > 10 or len(phone) <10:
             raise ValueError("Phone bumber has to be 10 digits")
        return phone
    
    
        
    

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError("You must enter a title")
        validated_titles = ["Won't Believe", "Secret", "Top", "Guess"]
        if title not in validated_titles:
            raise ValueError("Title must be clickbait-y")
        return title

    
    
    @validates('content')
    def validate_Content(self, key, content):
        if len(content) < 250:
            raise ValueError("Must be over 250 characters! ")
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Post summary is a maximum of 250 characters")
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        valid_categories = ["Fiction", "Non-Fiction"]
        if category not in valid_categories:
            raise ValueError("Has to be either Fiction or Non-Fiction")
        return category


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'

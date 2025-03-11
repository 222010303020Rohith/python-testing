from fastapi import FastAPI, HTTPException
from mongoengine import connect, Document, StringField, FloatField
from pydantic import BaseModel
from typing import List

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017/test_db"
connect(host=MONGO_URI)

# FastAPI app
app = FastAPI()

# MongoEngine Model
class ItemModel(Document):
    name = StringField(required=True, max_length=100)
    description = StringField(required=True, max_length=255)
    price = FloatField(required=True)

    def to_dict(self):
        return {"id": str(self.id), "name": self.name, "description": self.description, "price": self.price}

# Pydantic Model
class Item(BaseModel):
    name: str
    description: str
    price: float

# Create an item
@app.post("/items/", response_model=dict)
def create_item(item: Item):
    new_item = ItemModel(**item.dict()).save()
    return new_item.to_dict()

# Read all items
@app.get("/items/", response_model=List[dict])
def get_items():
    items = ItemModel.objects()
    return [item.to_dict() for item in items]

# Read single item
@app.get("/items/{item_id}", response_model=dict)
def get_item(item_id: str):
    item = ItemModel.objects(id=item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.to_dict()

# Update an item
@app.put("/items/{item_id}", response_model=dict)
def update_item(item_id: str, item: Item):
    updated_item = ItemModel.objects(id=item_id).first()
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item.update(**item.dict())
    updated_item.reload()
    return updated_item.to_dict()

# Delete an item
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: str):
    item = ItemModel.objects(id=item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.delete()
    return item.to_dict()

# Run the server using: uvicorn filename:app --reload



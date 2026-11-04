from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Catálogo de Itens")


class ItemInput(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    in_stock: bool = True


class Item(ItemInput):
    id: int


items = [
    Item(id=1, name="Caderno", price=12.5, in_stock=True),
    Item(id=2, name="Caneta", price=3.0, in_stock=True),
]


@app.get("/items", response_model=list[Item])
def list_items():
    pass


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    pass


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemInput):
    pass


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemInput):
    pass


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    pass
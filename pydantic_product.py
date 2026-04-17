from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="The price must be greater than 0")
    tags: list[str] = []
    market: Market


product_data = {
    'name': "phone",
    'price': 490.90,
    'tags': ['electronics', 'smartphone'],
    'market': {
        'id': 1,
        'name': 'market_name',
    }
}

product = Product(**product_data)

print(product)
print(product.market.id)

new_product = Product(
    name='phone',
    price=490.90,
    tags=['electronics', 'smartphone'],
    market=Market(id=1, name='market_name')
)
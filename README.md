Products Service
Denne microservice håndterer produkter, herunder opbevaring og forespørgsler af produktinformation fra en SQLite database. Produkterne inkluderer data såsom titel, beskrivelse, kategori, pris, lagerbeholdning, brand, SKU, vægt, og billed-URLs.



## Installation

1. Clone dette repository:

```
git clone https://github.com/ITAKEA/products_service.git
cd products_service
docker build -t products_service .
docker run -it --rm -p 5000:5000 -v ${PWD}:/home/data products_service

```

Eller:    

2. pull docker image fra DockerHub

```
    docker run -it --rm -p 5000:5000 -v ${PWD}:/home/data clbo/products_service:0.0.1

```

## API Endpoints

### Get all products

- **URL:** `/product`
- **Method:** `GET`


```json
  {
    [
    {
        "id": 1,
        "title": "Product Title",
        "description": "Product Description",
        "category": "Category",
        "price": 100.0,
        "stock": 50,
        "brand": "Brand Name",
        "sku": "SKU123",
        "weight": 1.5,
        "image_url": "https://example.com/image.jpg",
        "thumbnail_url": "https://example.com/thumbnail.jpg"
    }
]

  }
```
### Get product by id

- **URL:** `/product/<int:id>`
- **Method:** `GET`

```
[
    {
        "id": 2,
        "title": "Product Title",
        "description": "Product Description",
        "category": "Category",
        "price": 50.0,
        "stock": 20,
        "brand": "Brand Name",
        "sku": "SKU456",
        "weight": 1.2,
        "image_url": "https://example.com/image2.jpg",
        "thumbnail_url": "https://example.com/thumbnail2.jpg"
    }
]
```


### Get product by Category (Virker ikke i nu)

- **URL:** `/product/category/<string:category>`
- **Method:** `GET`

```
[
    {
        "id": 2,
        "title": "Product Title",
        "description": "Product Description",
        "category": "Category",
        "price": 50.0,
        "stock": 20,
        "brand": "Brand Name",
        "sku": "SKU456",
        "weight": 1.2,
        "image_url": "https://example.com/image2.jpg",
        "thumbnail_url": "https://example.com/thumbnail2.jpg"
    }
]
```

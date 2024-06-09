# PC inventory API Documentation

This API provides endpoints for managing categories, brands, and components in a PC inventory system. It also includes authentication endpoints for user login and token management.

## Authentication Endpoints

The authentication endpoints are provided by the `djoser` library and are included in the API URLs.

- `POST /auth/users/`: Register a new user.
- `POST /auth/token/login/`: Obtain an authentication token.
- `POST /auth/token/logout/`: Logout and invalidate the authentication token.

For more information on the available authentication endpoints, refer to the [Djoser documentation](https://djoser.readthedocs.io/en/latest/getting_started.html).

## Category Endpoints

- `GET /api/categories/`: Retrieve a list of all categories.
- `POST /api/categories/`: Create a new category.
- `GET /api/categories/<slug:slug>/`: Retrieve details of a specific category.
- `PUT /api/categories/<slug:slug>/`: Update a specific category.
- `DELETE /api/categories/<slug:slug>/`: Delete a specific category.

## Brand Endpoints

- `GET /api/brands/`: Retrieve a list of all brands.
- `POST /api/brands/`: Create a new brand.
- `GET /api/brands/<slug:slug>/`: Retrieve details of a specific brand.
- `PUT /api/brands/<slug:slug>/`: Update a specific brand.
- `DELETE /api/brands/<slug:slug>/`: Delete a specific brand.

## Component Endpoints

- `GET /api/components/`: Retrieve a list of all components for the authenticated user.
- `POST /api/components/`: Create a new component for the authenticated user.
- `GET /api/components/<int:pk>/`: Retrieve details of a specific component for the authenticated user.
- `PUT /api/components/<int:pk>/`: Update a specific component for the authenticated user.
- `DELETE /api/components/<int:pk>/`: Delete a specific component for the authenticated user.

Please note that all component endpoints require authentication, and only components associated with the authenticated user will be accessible.

## Request and Response Formats

All requests and responses use JSON format.

### Category Request/Response Format

```json
{
    "id": 1,
    "slug": "motherboards",
    "title": "Motherboards"
}
```

### Brand Request/Response Format

```json
{
    "id": 1,
    "slug": "asus",
    "title": "ASUS"
}
```

### Component Request Format

```json
{
    "price": 99.99,
    "stock": 10,
    "name": "ASUS ROG Strix Z590-E Gaming WiFi",
    "category_id": 1,
    "brand_id": 1
}
```

### Component Response Format

```json
{
    "id": 1,
    "price": "99.99",
    "stock": 10,
    "name": "ASUS ROG Strix Z590-E Gaming WiFi",
    "date_creation": "08/06/2024 - 14:30",
    "category": {
        "id": 1,
        "slug": "motherboards",
        "title": "Motherboards"
    },
    "category_id": 1,
    "brand": {
        "id": 1,
        "slug": "asus",
        "title": "ASUS"
    },
    "brand_id": 1,
    "user": 1
}
```
## Installation
### Install pipenv
```
python3 -m pip install --user pipenv
```
### pipenv shell
### pipenv install
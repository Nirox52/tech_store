# FastAPI Project

## Installation and Setup
### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Nirox52/tech_store.git
   cd tech_store
   ```

2. Run docker:
   ```bash
   docker compose up -d --build
   ```

3. Go to the [Documentation page](http://localhost:5555/docs):

## Endpoints

### JWT
- `POST /jwt/register` - Create new user
- `POST /jwt/` - Login

### Users
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get user by id
- `DELETE /users/{user_id}` - Delete user by id
### Products
- `GET /products/` - Get all products
- `POST /products/` - Create product
- `GET /products/{product_id}` - Get product by id
- `GET /products/type/` - Get product by type
- `DELETE /products/{product_id}` - Delete product by id
### Orders
- `POST /orders/` - Create Order 
- `GET /orders/{order_id}` - Get order by id
- `DELETE /orders/{order_id}` - Delete order by id
- `GET /orders/user/date/` - Get user orders in date range
- `GET /orders/date/` - Get all orders in date range
- `GET /orders/status/{order_status}` Get orders by status
- `GET /orders/my/` - Get all users orders
- `GET /orders/pay/{order_id}` Pay the order
- `POST /orders/status/{order_id}` Change order status
## Configuration

### Environment Variables
Create a `.env` file in the root directory with the following variables:

```ini
DB_HOST=test_db
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=tech_shop
SECRET_KEY_PATH=cert/private_filename.pem
PUBLIC_KEY_PATH=cert/publick_filename.pem
JWT_ALGORITM=RS256
```

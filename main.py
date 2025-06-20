from fastapi import FastAPI
from database import Base, engine

#Routers
from users.router import router as user_router
from products.router import router as product_router
from orders.router import router as order_router
from auth.router import router as auth_router

app = FastAPI()

Base.metadata.drop_all(bind=engine) #Drop all tables on strat
Base.metadata.create_all(bind=engine) #Create all tables on start

#Add routers for all models
app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message":"Tech shop API"}

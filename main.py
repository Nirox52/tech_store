from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database import Base, engine

#Routers
from users.router import router as user_router
from products.router import router as product_router
from orders.router import router as order_router

app = FastAPI()

Base.metadata.drop_all(bind=engine) #Drop all tables on strat
Base.metadata.create_all(bind=engine) #Create all tables on start

#Add routers for all models
app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)

@app.get("/")
def root():
    return RedirectResponse('http://127.0.0.1:8000/docs') #Redirect to documentation

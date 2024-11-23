from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import menu, cart, orders

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(menu.router)
app.include_router(cart.router)
app.include_router(orders.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
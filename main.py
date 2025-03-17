from fastapi import FastAPI, HTTPException
import uvicorn
import pika
import json
import os
from pydantic import BaseModel

app = FastAPI()

# Define the Order model
class Order(BaseModel):
    item: str
    quantity: int
    price: float
    customer_name: str
    customer_address: str

# Get RabbitMQ connection details from environment variables
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'user')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASSWORD', 'password')

# Establish connection to RabbitMQ
def get_rabbitmq_connection():
    try:
        credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
        parameters = pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            credentials=credentials,
            connection_attempts=5,
            retry_delay=5
        )
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue="order_queue", durable=True)
        return connection, channel
    except Exception as e:
        print(f"Error connecting to RabbitMQ: {str(e)}")
        return None, None

@app.post("/order")
async def place_order(order: Order):
    """API to receive order and send it to RabbitMQ"""
    try:
        # Get RabbitMQ connection and channel
        connection, channel = get_rabbitmq_connection()
        
        if not connection or not channel:
            raise HTTPException(
                status_code=503,
                detail="Failed to connect to message queue service"
            )

        # Convert order data to JSON and send to RabbitMQ
        order_json = json.dumps(order.dict())
        try:
            channel.basic_publish(
                exchange="",
                routing_key="order_queue",
                body=order_json,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # Make message persistent
                ),
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to publish message: {str(e)}"
            )
        finally:
            if connection and not connection.is_closed:
                connection.close()

        return {"message": "Order placed successfully", "order": order.dict()}

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )

@app.get("/")
async def root():
    return {"message": "Order Service is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

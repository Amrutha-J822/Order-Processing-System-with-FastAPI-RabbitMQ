from fastapi import FastAPI
import uvicorn
import pika
import json
from pydantic import BaseModel

app = FastAPI()

# Define the Order model
class Order(BaseModel):
    item: str
    quantity: int
    price: float
    customer_name: str
    customer_address: str

# Establish connection to RabbitMQ
def get_rabbitmq_connection():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq")  # Use RabbitMQ container name
        )
        channel = connection.channel()
        channel.queue_declare(queue="order_queue", durable=True)  # Ensure queue exists
        return connection, channel
    except Exception as e:
        return None, None

@app.post("/order")
async def place_order(order: Order):
    """API to receive order and send it to RabbitMQ"""
    try:
        # Get RabbitMQ connection and channel
        connection, channel = get_rabbitmq_connection()

        if not connection or not channel:
            return {"error": "Failed to connect to RabbitMQ"}

        # Convert order data to JSON and send to RabbitMQ
        order_json = json.dumps(order.dict())
        channel.basic_publish(
            exchange="",
            routing_key="order_queue",
            body=order_json,
            properties=pika.BasicProperties(
                delivery_mode=2,  # Make message persistent
            ),
        )
        connection.close()

        return {"message": "Order placed successfully", "order": order.dict()}

    except Exception as e:
        # Catch any errors and return a detailed error response
        return {"error": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Order-Processing-System-with-FastAPI-RabbitMQ

A microservices-based Order Processing System built with FastAPI and RabbitMQ, containerized using Docker.

## 🚀 Features

- RESTful API for order processing
- Asynchronous message queuing with RabbitMQ
- Data validation using Pydantic models
- Containerized deployment with Docker
- Swagger UI for API documentation
- RabbitMQ Management Interface

## 💻 Technologies Used

- **FastAPI**: Modern Python web framework
- **RabbitMQ**: Message broker for asynchronous communication
- **Docker**: Containerization platform
- **Pydantic**: Data validation and serialization
- **Python 3.10**: Programming language

## 📋 Prerequisites

- Docker
- Docker Compose

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Order_Service
```

### 2. Start the Services

```bash
docker-compose up --build
```

### 3. Access the Services

- **FastAPI Swagger UI**: http://localhost:8000/docs
- **RabbitMQ Management UI**: http://localhost:15672
  - Username: `user`
  - Password: `password`

## 📝 API Usage

### Place an Order

**Endpoint**: `POST /order`

**Request Body**:
```json
{
    "item": "Product A",
    "quantity": 2,
    "price": 25.5,
    "customer_name": "John Doe",
    "customer_address": "123 Main St"
}
```

**Response**:
```json
{
    "message": "Order placed successfully",
    "order": {
        "item": "Product A",
        "quantity": 2,
        "price": 25.5,
        "customer_name": "John Doe",
        "customer_address": "123 Main St"
    }
}
```

## 🗃️ Project Structure
```Order_Service/
    ├── main.py # FastAPI application
    ├── worker.py # Message consumer (if implemented)
    ├── docker-compose.yml # Docker Compose configuration
    ├── Dockerfile # Docker configuration for the app
    └── requirements.txt # Python dependencies ```


## 🔧 Docker Commands

### Start Services
```bash
docker-compose up --build
```

### Stop Services
```bash
docker-compose down -v
```

### View Logs
```bash
docker-compose logs -f
```

### Check Service Status
```bash
docker-compose ps
```

## 🔍 Monitoring

- **RabbitMQ Management UI**: Monitor queues, connections, and channels
- **FastAPI Swagger UI**: Test API endpoints and view documentation

## 🔒 Security

- RabbitMQ authentication enabled
- Input validation using Pydantic models
- Secure container networking

## 🚀 Future Improvements

- Add message consumers for order processing
- Implement database integration
- Add authentication for API endpoints
- Implement monitoring and logging
- Add load balancing
- Implement order status tracking

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👥 Authors

- Amrutha Junnuri

## 🙏 Acknowledgments

- FastAPI documentation
- RabbitMQ documentation
- Docker documentation

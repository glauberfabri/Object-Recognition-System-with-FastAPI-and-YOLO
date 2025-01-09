
# Object Recognition System with FastAPI, YOLO, and PostgreSQL

## Overview

This project is an object recognition system built with **FastAPI**, **YOLO**, **PostgreSQL**, **LangChain**, and **Redis**, following the **MVC (Model-View-Controller)** design pattern. Users can upload images, and the system detects objects in the images, saves the results in a database, and provides a natural language summary of the detected objects. The system also includes authentication, caching, and the ability to store images in AWS S3.

---

## Features

- **Object Detection**: Utilizes YOLOv5 for object detection in uploaded images.
- **Authentication**: JWT-based authentication for secure API access.
- **User Management**: User registration and login.
- **Natural Language Summary**: Generates descriptive summaries using LangChain.
- **Caching**: Recently processed images and results are cached using Redis.
- **Cloud Storage**: Images are stored in AWS S3.
- **Logging**: Detailed application logging with Loguru.
- **Monitoring**: Application monitoring with Prometheus and Grafana.

---

## Technologies Used

- **Python**: Main programming language.
- **FastAPI**: Web framework for building APIs.
- **YOLOv5**: Object detection model.
- **PostgreSQL**: Database for storing user and analysis data.
- **Redis**: Caching system for improved performance.
- **LangChain**: For generating natural language summaries.
- **AWS S3**: Cloud storage for image files.
- **Docker**: Containerization for deployment.

---

## Project Structure

```
project/
│
├── app/
│   ├── main.py          # Application entry point
│   ├── models.py        # Database models and schemas
│   ├── views.py         # API endpoints
│   ├── controllers.py   # Image processing logic
│   ├── auth.py          # Authentication logic
│   ├── config.py        # Configuration (DB, Redis, AWS)
│   ├── storage.py       # Functions for AWS S3 integration
│   ├── summarizer.py    # LangChain integration for summaries
│   ├── logs/            # Log files
│   ├── yolov5/          # YOLOv5 implementation
│   └── utils.py         # Helper functions
│
├── tests/               # Automated tests
│   ├── test_views.py    # API endpoint tests
│   ├── test_models.py   # Database tests
│   ├── test_auth.py     # Authentication tests
│   └── test_utils.py    # Utility function tests
│
├── requirements.txt     # Project dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
└── README.md            # Project documentation
```

---

## Installation

### Prerequisites

- Python 3.9+
- PostgreSQL
- Redis
- AWS S3 credentials (optional)
- Docker (optional for containerization)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/object-recognition-system.git
   cd object-recognition-system
   ```

2. **Set up the environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure the environment variables**:
   Create a `.env` file in the project root:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   REDIS_URL=redis://localhost:6379
   AWS_ACCESS_KEY=your_aws_access_key
   AWS_SECRET_KEY=your_aws_secret_key
   S3_BUCKET=your_s3_bucket
   ```

4. **Set up the database**:
   ```bash
   python -m app.models
   ```

5. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Running with Docker

1. **Build the Docker image**:
   ```bash
   docker-compose build
   ```

2. **Start the containers**:
   ```bash
   docker-compose up
   ```

3. Access the API at: [http://localhost:8000](http://localhost:8000)

---

## API Endpoints

### Authentication

| Method | Endpoint          | Description                |
|--------|-------------------|----------------------------|
| POST   | `/auth/register`  | Register a new user        |
| POST   | `/auth/token`     | Login and get access token |

### Image Upload and Processing

| Method | Endpoint          | Description                     |
|--------|-------------------|---------------------------------|
| POST   | `/api/upload/`    | Upload an image for analysis   |

### User Analysis History

| Method | Endpoint          | Description                     |
|--------|-------------------|---------------------------------|
| GET    | `/api/history/`   | Get all analyses for the user  |

---

## Running Tests

Run the test suite to verify the application:

```bash
pytest --disable-warnings
```

To check code coverage:

```bash
pytest --cov=app tests/
```

---

## Monitoring and Logging

- **Logs**: Stored in the `logs/` directory. Rotates at 10MB per file.
- **Prometheus**: Metrics endpoint available at `/metrics`.
- **Grafana**: Connect to Prometheus for monitoring dashboards.

---

## Future Enhancements

- Add support for video processing.
- Extend authentication with OAuth2 providers (e.g., Google, GitHub).
- Implement rate-limiting for API endpoints.
- Build a front-end UI with React or Vue.js.

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or support, please contact: [gabriel@dynsoftware.net](mailto:gabriel@dynsoftware)

# Real-Time Chat Application

## A FastAPI WebSocket backend for an in-memory chat demo

This repository contains a small real-time chat backend built with FastAPI and WebSockets. It manages active connections, broadcasts messages to connected clients, and keeps a limited in-memory message history.

## Features

### Core Capabilities

- **WebSocket Connections**: Accepts multiple connected chat clients
- **Message Broadcasting**: Sends messages to active participants
- **Connection Lifecycle**: Handles client join and leave events
- **Message History**: Retains recent messages in memory for the active process
- **Health Endpoint**: Exposes a basic service-status route

## Technology Stack

- **Backend**: Python, FastAPI
- **Real-Time Transport**: WebSockets
- **ASGI Server**: Uvicorn
- **Storage**: In-memory process state

## Installation

### Requirements

- Python 3.9 or later recommended
- pip

### Setup

```bash
git clone https://github.com/Shiv-0707/real-time-chat-app.git
cd real-time-chat-app
python -m venv .venv
```

Activate the environment and install the runtime packages:

```bash
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install fastapi uvicorn
```

## Running the Application

```bash
uvicorn chat:app --reload
```

The server can then be inspected at:

```
http://127.0.0.1:8000/docs
```

## Project Structure

```
real-time-chat-app/
├── chat.py              # FastAPI application and WebSocket chat logic
└── README.md            # Project documentation
```

## Current Limitations

This project is a backend demonstration, not a production chat service. Messages are stored only in memory and are lost when the server restarts. The repository does not currently include a browser client, persistent storage, authentication, automated tests, or deployment configuration.

## Future Improvements

- Add a web or mobile chat client
- Add persistent message storage
- Add user authentication and authorization
- Add tests for health, history, and WebSocket behavior
- Configure trusted origins and deployment settings

## Contact

Shiv Pratap Singh — [GitHub](https://github.com/Shiv-0707) · shivpratap0709@gmail.com

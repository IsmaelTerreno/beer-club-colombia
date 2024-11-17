# Project Name

## Overview

This project is designed to manage and facilitate the operations of a beer club. It provides an API for managing beer
collections within the club. The system includes endpoints for creating, updating, and retrieving information about
beers, orders, and process payments in cash.

## Endpoints

### Base URL

`http://localhost:8000`

### API Endpoints documentation

The API contains Swagger documentation. It can be seen at the following local
link: [API Documentation](http://localhost:8000/docs)

## How to Run the Application

### Prerequisites

- Python 3.12.6

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/IsmaelTerreno/beer-club-colombia.git
   ```
2. Navigate to the project directory:
   ```sh
   cd beer-club-colombia
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
   Ensure you have the following packages installed:
    - click
    - coverage
    - pytest

### Running the Application

To start the application, run the following command for FastAPI framework:

```sh
uvicorn main:app --reload
```
# Flask Boilerplate

[![Black](https://github.com/abinthomasonline/flask-boilerplate/actions/workflows/black.yml/badge.svg)](https://github.com/abinthomasonline/flask-boilerplate/actions/workflows/black.yml)
[![Tests](https://github.com/abinthomasonline/flask-boilerplate/actions/workflows/tests.yml/badge.svg)](https://github.com/abinthomasonline/flask-boilerplate/actions/workflows/tests.yml)

A simple CRUD application using Flask.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [License](#license)

## Overview

This Flask Boilerplate is a simple [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (Create, Read, Update, Delete) application. It uses Flask for the web framework and SQLite with Flask-SQLAlchemy for data persistence.

## Features

- CRUD operations
- RESTful API endpoints
- Simple web interface for interacting with the data
- SQLite database for easy setup and portability
- Test suite with pytest
- Initial demo data for toys and games

## Requirements

- Python 3.12.3 (should work with other similar versions)
- pip 24.0 (should work with other similar versions)

## Folder Structure

```
flask-boilerplate/
├── app/
│ ├── static/           # static files
│ ├── templates/        # template files (for the web interface)
│ ├── toys/             # toys CRUD endpoints
│ ├── games/            # games CRUD endpoints
│ ├── main/             # template serving
│ ├── init.py           # app initialization
│ └── models.py         # database models
│ └── config.py         # configuration file
├── tests/              # test suite
├── .env                # environment variables
├── .gitignore          # git ignore file
├── requirements.txt    # dependencies
└── run.py              # entry point for development server
````

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/abinthomasonline/flask-boilerplate.git
   cd flask-boilerplate
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the development server:
   ```
   python run.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Use the web interface to manage toys and games, or interact with the API endpoints directly.

   Note: For demonstration purposes, the application initializes with 10 toy and 10 game entries. 
   This behavior can be modified or removed for real-world use by editing the `load_initial_data` 
   function in `app/__init__.py`.

### API Endpoints:
- Toys:
  - GET /toys
  - POST /toys
  - GET /toys/<id>
  - PUT /toys/<id>
  - DELETE /toys/<id>
- Games:
  - GET /games
  - POST /games
  - GET /games/<id>
  - PUT /games/<id>
  - DELETE /games/<id>

## Testing

Run the test suite using pytest:
```
pytest
```

To run tests with coverage:
```
pytest --cov=app
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)

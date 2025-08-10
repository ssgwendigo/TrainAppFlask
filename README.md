# Train App with Flask

A Flask-based web application built to serve as a backend for https://github.com/ssgwendigo/TrainAppFE and to demostrate how this API can be built using Python.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <path-to-your-fork>
   cd TrainAppFlask
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python run.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8000
   ```

## Configuration

Make sure to set up your environment variables in the `.env` file. A sample configuration can be found in `.env.example`. If you don't already have a WMATA api key, get one here: https://developer.wmata.com/

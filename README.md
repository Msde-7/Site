# Action Campaign Website

A campaign website for the school presidential campaign "Action".

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Mac/Linux:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

1. Make sure your virtual environment is activated
2. Run the Flask application:
```bash
python app.py
```
3. Open your web browser and visit: http://localhost:5000

The website will be available at http://localhost:5000 and includes the following pages:
- Home: http://localhost:5000/
- Who is Action: http://localhost:5000/who.html
- Our Fight: http://localhost:5000/goals.html
- Why Different: http://localhost:5000/difference.html

## Project Structure
```
.
├── app.py              # Flask web server
├── requirements.txt    # Python dependencies
├── index.html         # Home page
├── who.html          # Who is Action page
├── goals.html        # What Action is Fighting For page
├── difference.html   # How Action is Different page
├── styles.css        # Shared styles
└── images/           # Image assets
    └── logo.png      # Campaign logo
``` 
# create python environment
python -m venv/bin/activate

# activate virtual environment
venv\Scripts\activate

# Create requirements.txt file
pip freeze > requirements.txt

# Create requirements.txt file
pip install -r requirements.txt

# Run the project
python manage.py runserver 8001

# Create Tables in database
python manage.py makemigrations
python manage.py migrate
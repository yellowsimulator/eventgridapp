pip install -r requirements.txt
gunicorn -w 4 wsgi:app

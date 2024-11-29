runserver:
	python3 manage.py runserver

shell_plus:
	python3 manage.py shell_plus --ipython

restore-db:
	python3 manage.py restore_db

migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations book_manager
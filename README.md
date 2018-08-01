<H1> Django task </H1>

<H3> Python version: 3.6 </H3>
<H3> Django version: 2.0.7 </H3>
<H3> Virtual environment: Pipenv </H3>

1. Install Pipenv using `pip install pipenv` command. If you are using other OS than Linux, please refer to the [documentation](https://docs.pipenv.org/install/)
2. Clone repository (`git clone`) either via HTTPS or SSH. SSH is recommended as it is more secure
3. Go to the catalogue with Pipfile and Pipfile.lock and activate virtual environment - `pipenv shell`
4. Install dependencies - `pipenv install`
5. Go to the catalogue with manage.py and run application on development server by using `python manage.py runserver`. Default port for this server is 8000, but if you want to change it, just use `python manage.py runerver <port>`. You will find application on `http://localhost:8000/users/`
6. If you want to run tests, simply use `python manage.py test` command

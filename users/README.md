<H1>Django task

<H3>Python version: 3.6
<H3>Django version: 2.0.7
<H3>Virutal environment: Pipenv

In order to use this application, please follow instructions below:

1. Install Pipenv, a virtual environment. Use `pip install pipenv` command.
If you are using MacOS or other OS, please refer to the [documentation](https://docs.pipenv.org/install/)
2. Clone repository either via HTTPS or SSH - I recommend using SSH as it is more secure
3. In catalogue with Pipfile and Pipfile.lock run `pipenv shell` - this command activates virtual environment
4. Install dependencies - `pipenv install`
5. Run development server using `python manage.py runserver` command. The server runs on port 8000 on default. If you want to use different port then just run `python manage.py runserver <port>`. Application is available on `http://localhost:8000/users/`
6. If you want to run tests, use `python manage.py test` command
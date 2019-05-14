# keyauthentication

#### Environment
```commandline
python 3.7
``` 
#### [pipenv](https://docs.pipenv.org/)
pipenv is used for virtual environment.

Setup pipenv 
```commandline
pip install --user pipenv
```
Enable virtual environment
```commandline
pipenv shell
```
Install project dependencies
```commandline
pipenv install
```

Install specific package 
```commandline
pipenv install package_name=='version'
```

#### Configuration Environment Variables
```commandline
cp .env.sample .env
```
Enter respective values for environment variables
and create the corresponding Database in the Mysql

Create the tables in the Database with the following command:
```commandline
flask db upgrade
```

#### Start Application in Development
```commandline
flask run
```

Build the Docker Image and Run
```commandline
docker build -f Dockerfile -t keyauthentication .
docker run --rm -it -p 5000:5000 --env-file=.env keyauthentication
```

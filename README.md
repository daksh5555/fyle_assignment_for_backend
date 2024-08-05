This repository is a fork of @fyle-interview-intern-backend
 [https://github.com/original-username/original-repository](https://github.com/fylein/fyle-interview-intern-backend) and has been modified to include new features and improvements.

# Fyle Backend Challenge - How To  Run

### Development env: 
> Ubuntu 22.04 LTS
> 
>  python3.8.19

cd fyle-interview-intern-backend

virtualenv fylenv --python=python3.8
. fylenv/bin/activate

pip install -r requirements.txt
```

### Run tests using this cmd.
```
# Than reset DB
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
# lets run at
pytest -vvv -s tests/
```

### Than Start Server

```
# first reset DB
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
# then run
bash run.sh
```

### view the test coverage in the browser using this cmd.
```
# first reset DB
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
# lets go
pytest --cov --cov-report html
open htmlcov/index.html
```

### Build the docker container first using this cmd.
the cmd is meant to be used when you made some changes in your code or building for the first time. open your docker desktop first to start the docker engine and then run the following cmd command.
```
docker compose up --build -d
```

### Run docker container using this cmd.
```
docker compose up -d
```

### Shut docker container up using this cmd.
```
docker compose down
```

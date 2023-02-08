#!/bin/sh

create(){ 
    project_name=$1
    is_github_repo_create=$2
    django_version=$3

    path=" /home/eyakub/Desktop/DjangoProject"

    python3 create-django-project.py $project_name $is_github_repo_create
    if [ $? -ne 0 ]; then
        echo "Error: Python script failed to run"
        exit 1
    fi
    
    cd $path/$project_name
    python3 -m venv venv
    cd $path/$project_name
    . venv/bin/activate

    pip3 install django==$django_version
    django-admin startproject $project_name .
    pip3 freeze > requirements.txt

    # Create project directories and files
    mkdir templates
    mkdir static
    mkdir media
    mkdir apps
    mkdir nginx

    create_file_and_populate "$project_name"

    # configure git
    git init
    git rm -r --cached .
    git add .
    git commit -m "init commit"
    git remote add origin git@github.com:Eyakub/$project_name.git
    if [ "$is_github_repo_create" = "Y" ] || [ "$is_github_repo_create" = "y" ]
    then
        git push -u origin master
    fi

    code .
}

create_file_and_populate() {
    touch .dockerignore

# Create and write to .env sample file
    cat <<EOT > .env.sample
DEBUG=True
SECRET_KEY='something_key'
ALLOWED_HOST=*
DATABASE_URL=postgres://postgres:postgres@db:5432

# Postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
EOT

# Create and write the .gitignore file for Django
    cat <<EOT > .gitignore
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# If you are using PyCharm
.idea/
.vscode/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
__pycache__/
EOT

# writing the entrypoint file to run the server
    cat <<EOT > entrypoint.sh
#!/bin/bash

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
#/usr/local/bin/gunicorn jobs.wsgi:application -w 2 -b :8000
EOT
    # chmod +x entrypoint.sh

# writing a basic readme file
    echo "$1
=============================
## Introduction

Add description of your project here.

## Requirements

Add the required dependencies here.

## How to Run

Steps to run the project locally." > README.md

# creating a basic docker file
DockerHome="/usr/src/app"
echo "FROM python:3.10-slim-buster

ENV DockerHome=${DockerHome}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR \${DockerHome}

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt \${DockerHome}
RUN pip install -r requirements.txt

# copy project
COPY . \${DockerHome}
RUN cp .env.sample .env

EXPOSE 8000
RUN chmod +x entrypoint.sh

CMD [\"sh\", \"entrypoint.sh\"]" > Dockerfile

# creating basic docker compose command
echo "version: '3.8'

services:
  web:
    build: .
    command: ./entrypoint.sh
    ports:
      - 8000:8000
    volumes:
      - .:/app" > docker-compose.yml
}



echo "Enter your Project/Repo name (recommended pattern: my_django_app/myDjangoApp):"
read project_name

echo "Do you want to create respository on Github? (Y/N)"
read is_github_repo_create

echo "Enter the desired Django version: (Default: 4.0)"
read django_version

create "$project_name" "${is_github_repo_create:-N}" "${django_version:-4.0}"

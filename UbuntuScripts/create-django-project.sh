#!/bin/sh

create(){ 
    project_name=$1
    django_version=$2
    if [ $django_version -eq 0 ]
    then
        django_version="4.2"
    else
        django_version=$2
    fi

    python3 create-django-project.py $project_name
    cd /home/eyakub/Desktop/UbuntuWorkings/Django/$project_name
    python3 -m venv venv
    cd /home/eyakub/Desktop/UbuntuWorkings/Django/$project_name
    . venv/bin/activate

    pip3 install django
    django-admin startproject $project_name .
    pip3 freeze > requirements.txt

    # Create project directories and files
    mkdir templates
    mkdir static
    mkdir media
    mkdir apps
    touch README.md
    touch .gitignore

    # configure git
    git init
    git rm -r --cached .
    printf "### "$project_name> README.md
    printf "*/.vscode/*\n.vscode/*\n.vscode/\nvenv/\n/venv\n/.venv">.gitignore
    git add .
    git commit -m "init commit"
    git remote add origin https://github.com/eyakub/$project_name.git
    git push origin master

    code .
}


echo "Enter your Project/Repo name (recommended pattern: my_django_app/myDjangoApp):"
read project_name
echo "Enter the desired Django version: (Default: 4.2)"
read django_version

create $project_name $django_version

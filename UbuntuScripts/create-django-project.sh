#!/bin/sh

create(){ 
    project_name=$1
    is_github_repo_create=$2
    django_version=$3

    path=" /home/eyakub/Desktop/DjangoProject"

    python3 create-django-project.py $project_name $is_github_repo_create
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
    touch README.md
    touch .gitignore

    # configure git
    git init
    git rm -r --cached .
    printf "### "$project_name> README.md
    printf "*/.vscode/*\n.vscode/*\n.vscode/\nvenv/\n/venv\n/.venv">.gitignore
    git add .
    git commit -m "init commit"
    git remote add origin git@github.com:Eyakub/$project_name.git
    git push -u origin master

    code .
}


echo "Enter your Project/Repo name (recommended pattern: my_django_app/myDjangoApp):"
read project_name

echo "Do you want to create respository on Github? (Y/N)"
read is_github_repo_create
if [ -z "$is_github_repo_create"]; then
    is_github_repo_create="N"
fi

echo "Enter the desired Django version: (Default: 4.2)"
read django_version
if [ -z "$django_version" ]
then
    django_version="4.2"
fi

create $project_name $is_github_repo_create $django_version

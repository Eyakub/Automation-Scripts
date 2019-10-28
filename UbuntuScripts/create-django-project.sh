#!/bin/sh

create(){ 
    python3 create-django-project.py $1
    cd /mnt/1E4AC8FB4AC8D0A7/DjangoWeb/$1
    mkdir 'src'
    virtualenv venv
    cd /mnt/1E4AC8FB4AC8D0A7/DjangoWeb/$1
    . venv/bin/activate
    pip3 install django==2.2
    cd
    cd /mnt/1E4AC8FB4AC8D0A7/DjangoWeb/$1/src
    django-admin startproject $1 .

    cd ..
    git init
    git rm -r --cached .
    touch README.md
    printf "### "$1> README.md
    touch .gitignore
    touch requirements.txt
    printf "*/.vscode/*\n.vscode/*\n.vscode/\nvenv/\n/venv\n/.venv">.gitignore
    git add .
    git commit -m "init commit"
    git remote add origin https://github.com/eyakub/$1.git
    git push origin master

    code .
}


echo "Enter your Project/Repo name."
echo "NB: Recommanded pattern: my_django_app/myDjangoApp"
read projectName

create $projectName 

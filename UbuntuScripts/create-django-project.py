import sys
import os
from github import Github


path = "/Desktop/Eyakub/DjangoProject/"

username = ""
password = ""


def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + folderName)
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print('directory created', folderName)


if __name__ == "__main__":
    create()

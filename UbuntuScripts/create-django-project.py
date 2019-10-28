import sys
import os
from github import Github


path = "/mnt/1E4AC8FB4AC8D0A7/DjangoWeb/"

username = ""
password = ""


def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print('directory created', folderName)


if __name__ == "__main__":
    create()
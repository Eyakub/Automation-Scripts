import sys
import os
from github import Github


path = "/media/eyakub/Important/Django Projects/"

username = ""
password = ""


def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print('directory created')


if __name__ == "__main__":
    create()
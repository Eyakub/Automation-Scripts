import sys
import os
import json
import requests
# from github import Github


PATH = "/home/eyakub/Desktop/DjangoProject/"

PERSONAL_ACCESS_TOKEN = ""
API_BASE_URL = "https://api.github.com"


class CustomGithub:
    """ required github actions """
    def __init__(self, personal_access_token, api_base_url):
        self.personal_access_token = personal_access_token
        self.api_base_url = api_base_url
        self.headers = {
            "Authorization": f"Bearer {self.personal_access_token}",
            'Content-Type': 'application/json'
        }

    def __send_request(self, http_method, url, payload):
        """ making request with header and token """
        payload = json.dumps(payload)

        response = requests.request(http_method, url, headers=self.headers, data=payload, timeout=5)
        if not response.ok:
            print(f"Failed to process request: {response}")
        try:
            response = response.json()
        except json.decoder.JSONDecodeError:
            print("Parsing error")
        return response

    def create_repo(self, repo_name):
        """ create github repository """
        http_method = "POST"
        url = f"{self.api_base_url}/user/repos"
        payload = {
            "name": repo_name,
            "description": "New repository from script.",
            "private": True
        }
        return self.__send_request(
            http_method=http_method,
            url=url,
            payload=payload
        )


    def delete_repo(self):
        """ delete github repo """

    def update_repo(self):
        """ update github repo """


def create_local_directory(folder_name, is_github_repo_create):
    """create local directory for the project and calling the Github create repo api """
    os.mkdir(PATH + folder_name)
    if is_github_repo_create.lower() == 'y':
        repo_create = github_api.create_repo(folder_name)
    print(f'Directory & repository created: {folder_name}')


if __name__ == "__main__":
    github_api = CustomGithub(
        personal_access_token=PERSONAL_ACCESS_TOKEN,
        api_base_url=API_BASE_URL
    )
    folder_name = str(sys.argv[1])
    is_github_repo_create = str(sys.argv[2])

    create_local_directory(folder_name, is_github_repo_create)

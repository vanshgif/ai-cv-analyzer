import requests

def fetch_github_data(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "public_repos": data.get("public_repos", 0),
        "followers": data.get("followers", 0)
    }
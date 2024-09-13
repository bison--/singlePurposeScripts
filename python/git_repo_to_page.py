from urllib.parse import urlparse, urlunparse

git_urls = [
    'ssh://git@gitlab.spielmannsolutions.com:2289/spielmannspiel/godot-assets/spielmannspiel-intro.git',
    'git@github.com:godotengine/godot-asset-library.git',
    'https://github.com/godotengine/godot-asset-library.git'
]


def git_repo_to_page(_git_url):
    if _git_url.startswith('ssh://'):
        _git_url = _git_url.replace('ssh://', 'https://').replace('git@', '')
        parsed_url = urlparse(_git_url)
        netloc = parsed_url.hostname  # Remove port by only using hostname
        _git_url = f"{parsed_url.scheme}://{netloc}{parsed_url.path}"
    elif _git_url.startswith('git@'):
        _git_url = _git_url.replace(':', '/', 1).replace('git@', 'https://')
    if _git_url.endswith('.git'):
        _git_url = _git_url[:-4]
    return _git_url

for git_url in git_urls:
    print(git_repo_to_page(git_url))

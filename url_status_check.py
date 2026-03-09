"""URL Status Checker.

A simple utility that checks the HTTP status code of a given URL
and reports whether the request was successful.

Requires:
    requests: Install via ``pip install requests``.
"""

import requests

def check_status(url):
    """Check the HTTP status of a given URL and print the result.

    Prepends 'https://' if no scheme is provided, then sends a GET request
    and prints whether the request succeeded with a 200 status code.

    Args:
        url: The target URL or domain name to check (e.g. 'www.example.com').

    Raises:
        requests.exceptions.RequestException: Caught internally; prints an
            error message if the connection fails or times out.
    """
    if not url.startswith('http'):
        url = f"https://{url}"

    try:
        response = requests.get(url, timeout=5)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        if response.status_code -- 200:
            print("Success (200 OK)!")
        else:
            print("#FAIL or Redirect.")
    except requests.exceptions.RequestExceptions:
        print("Did Not connect -or- Request timed out.")

target_url = input("Enter a website URL: ")
# target_url = "www.cnn.com"
check_status(target_url)
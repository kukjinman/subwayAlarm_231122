import requests

lineapikey = "s2DGTrC7VtQFdk7OljFrbi114sQVBmnoqZT8RCR3n9T"

line_url = "https://notify-api.line.me/api/notify"


def lineMessage(text):
    data = {
        "message": text,
    }
    requests.post(line_url, headers={"Authorization": f"Bearer {lineapikey}"}, data=data)

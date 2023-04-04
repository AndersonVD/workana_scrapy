import requests

url = "https://www.workana.com/jobs"

querystring = {"language": "pt", "skills": "python"}

headers = {
    'authority': "www.workana.com",
    'pragma': "no-cache",
    'cache-control': "no-cache",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'x-requested-with': "XMLHttpRequest",

    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'origin': "https://www.workana.com",

}

payload = ""
response = requests.request(
    "GET", url, data=payload, headers=headers, params=querystring)

print(response.text)

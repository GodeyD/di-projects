import http.client

conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "f5f1a9c5b0msh646ff2a97d048ccp16a068jsna1f5daf62d31",
    'X-RapidAPI-Host': "covid-193.p.rapidapi.com"
    }

conn.request("GET", "/statistics", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

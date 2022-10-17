import http.client
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
payload = "{\r\n     \"exchange\": \"NSE\",\r\n    \"symboltoken\": \"3045\",\r\n     \"interval\": \"ONE_MINUTE\",\r\n  \"fromdate\": \"2021-02-08 09:30\",\r\n     \"todate\": \"2021-02-08 10:00\"\r\n}"
headers = {
  'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': '',
    'X-ClientPublicIP': '',
    'X-MACAddress': '',
    'X-PrivateKey': '',
    'Authorization': 'Bearer ', 
    'Content-Type': 'application/json'
}
conn.request("POST", "/rest/secure/angelbroking/historical/v1/getCandleData", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
import urllib.request
import http.client

http_response: http.client.HTTPResponse = urllib.request.urlopen("http://www.heise.de")
print(http_response.read())




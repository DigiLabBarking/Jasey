"""
Python Web Service
"""
#!/usr/bin/env python
import web
from requests import Session

url = "url"

urls = (
    '/classify/(.*)', 'clasify_string'
)

app = web.application(urls, globals())

class clasify_string:
    def GET(self, user):
        print(self)
        s = Session()
        s.verify = False
        s.auth = ('username', 'password')
        resp = s.get(url, params={'text': str(user)}, stream=True)
        content=resp.content
        return str(content.split('\n')[4].split('"')[3])

if __name__ == "__main__":
    app.run()

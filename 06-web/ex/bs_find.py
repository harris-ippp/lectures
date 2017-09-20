addr = "https://harris-ippp.github.io/lectures/"
resp = requests.get(addr)
html = resp.content
soup = bs(html, "html.parser")

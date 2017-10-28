l = [x.contents for x in soup.find_all("tr")[1:]]
[xc[0].contents for xc in l if "tr" in xc[2].get("class")[0]]


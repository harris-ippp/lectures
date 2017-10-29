l = [x.contents for x in soup.find_all("tr")[1:]]
[xc[0].contents[0] for xc in l if "Tr" in xc[2].contents[0]]


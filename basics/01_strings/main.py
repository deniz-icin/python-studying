URL = "https://meet.google.com/yig-qocf-xmc?pli=1"

nakedURL = URL

if nakedURL.startswith("https://"):
    nakedURL = nakedURL.replace("https://","")

if nakedURL.startswith("http://"):
    nakedURL = nakedURL.replace("http://","")

y = nakedURL.split("/")

print(y[0])


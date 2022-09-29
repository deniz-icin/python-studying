
URL_list = ["http://meet.google.com/yig-qocf-xmc?pli=1","https://meet.google.com/yig-qocf-xmc?pli=1","https://www.notion.so/balconyke/continue-7709144555a64d0191f270340bcb43840","www.codecademy.com/learn/paths/front-end-engineer-career-path"]

for URL in URL_list:



    # URL = "https://meet.google.com/yig-qocf-xmc?pli=1"

    nakedURL = URL

    if nakedURL.startswith("https://"):
        nakedURL = nakedURL.replace("https://","")

    if nakedURL.startswith("http://"):
        nakedURL = nakedURL.replace("http://","")

    y = nakedURL.split("/")

    print(y[0])


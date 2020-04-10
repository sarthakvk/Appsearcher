import re

import requests as req
from bs4 import BeautifulSoup as bs


def playStore(url):
    """
    function to scrap
    data from play store

    """

    data = req.get(url).content

    data = bs(data, features="html.parser")

    if data.title.text == "Not Found":
        return {"ERROR": True}

    strdata = bs.prettify(data)  # making data to str type

    icon = re.findall(r"<.*T75of sHb2Xb.*>", strdata)[0]

    icon = re.findall(r'(?<=src=)".*?"', icon)[0][1:-1]

    name = str(data.find("h1", class_="AHFaub"))

    name = re.findall(r"(?<=span>).*?(?=\<)", name)[0]

    devname = str(data.find("a", class_="hrTbp R8zArc"))

    devname = re.findall(r"(?<=\>).*?(?=\<)", devname)[0]

    discp = str(data.find("div", jsname="sngebd"))

    discp = re.sub(r"\<.*?\>", "", discp)

    if len(discp) > 200:
        discp = discp[:200] + "..."

    rating = str(data.find("div", class_="BHMmbe"))

    rating = re.sub(r"\<.*?\>", "", rating)

    downloads = str(data.select(".htlgb .IQ1z0d .htlgb")[2])

    downloads = re.sub(r"\<.*?\>", "", downloads)

    reviews = str(data.select(".AYi5wd.TBRnV")[0])

    reviews = re.sub(r"\<.*?\>", "", reviews)

    return {
        "ICON": icon,
        "APP_NAME": name,
        "DEV_NAME": devname,
        "DISCRIPTION": discp,
        "RATING": rating,
        "DOWNLOADS": downloads,
        "REVIEWS": reviews,
        "ERROR": False,
    }


def appStore(url):
    """
        function to scrap
        data from app store

        """
    data = req.get(url).content

    data = bs(data, features="html.parser")

    if str(data) == "":
        return {"ERROR": True}

    icon = data.find("picture").find("source")["srcset"].split(",")[0][:-3]

    name = str(data.select(".product-header__title.app-header__title"))

    name = name.split("\n")[1].strip()

    devname = str(
        data.select(".product-header__identity.app-header__identity"))

    devname = devname.split("\n")[-3].strip()

    discp = data.find_all("p")[1].text[:201] + "..."

    if len(discp) > 200:
        discp = discp[:200] + "..."

    rating = str(
        data.find("figcaption", class_="we-rating-count star-rating__count"))

    rating, reviews = re.sub(r"\<.*?\>", "", rating).split(", ")

    reviews = reviews.split()[0]

    downloads = "Not Available"

    return {
        "ICON": icon,
        "APP_NAME": name,
        "DEV_NAME": devname,
        "DISCRIPTION": discp,
        "RATING": rating,
        "DOWNLOADS": downloads,
        "REVIEWS": reviews,
        "ERROR": False,
    }

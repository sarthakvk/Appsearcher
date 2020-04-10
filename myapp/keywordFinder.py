import requests as req
from bs4 import BeautifulSoup as bs

from .models import Url, Keyword


class key_man(object):
    """
    Class for Keyword finding, recommanding and saving to database
    """

    def __init__(self, url):

        self.url = url

    def keyword_finder(self):
        """
        finding and returns the keywords of given
        URL

        :return list
        """

        head = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/"
            "537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
        }

        data = bs(req.get(self.url, headers=head).content, features="html.parser")

        keywords = []

        try:

            keywords = data.select_one('meta[name="keywords"]')["content"].split(",")

        except:

            pass

        try:

            keywords.append(
                data.select_one('meta[property="og:description"]')["content"]
            )

        except:

            pass

        try:

            keywords.append(data.select_one('meta[name="description"]')["content"])

        except:

            pass

        return keywords

    def related_urls(self, keywords):
        """
        recommend keywords to the
        given url based on the keywords
        in the database

        """

        dic = {}

        for keyword in keywords:

            key_list = (
                Keyword.objects.filter(name=keyword).exclude(url=self.url).values("url")
            )

            for i in key_list:

                try:
                    dic[i["url"]].append(keyword)

                except:

                    dic.setdefault(i["url"], [keyword])

        return dic  # dictionary with related urls from keywords of given url

    def recommender(self, dic):
        """

        :param dic: related_urls
        :return:
        """

        recom = []

        for i in list(dic.keys()):

            if len(dic[i]) >= 3:
                qs = (
                    Keyword.objects.filter(url=i)
                    .values("name")
                    .difference(Keyword.objects.filter(url=self.url).values("name"))
                )

                recom.extend(list(qs))

        # list of recommended keywords | format: list of dictionary(key: name)
        return recom

    def key_of_related_urls(self, dic):
        """

        :param dic: related_urls
        :return:
        """

        related_dic = {}

        for i in list(dic.keys()):
            related_dic[i] = list(
                Keyword.objects.exclude(name__in=dic[i]).values("name")
            )

        return related_dic  # dictionary with keyword of related urls in format of dict key:'name'

    def key_saver(self, keywords):
        """
        function to save keywords in data base
        :param keywords:
        :return:
        """
        if len(list(Url.objects.filter(url=self.url))) != 0:
            return 0

        for i in keywords:
            url = Url(self.url)
            url.save()
            Keyword(name=i, url=url).save()

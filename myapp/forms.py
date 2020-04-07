from django import forms

class Appform(forms.Form):

    play_app = forms.CharField(required=False)

    ios_app = forms.CharField(required=False)

    ios_app_no = forms.IntegerField(required=False)



###############################################################
# if pname == "":
#
#     play = False
#
#     pname = request.GET.get('app-name')
#
#     pid = request.GET.get('app-id')
#
#     print(pname, pid)
#
#
# else:
#
#     play = True
#
#     print(pname)
#
# if play:
#     url = "https://play.google.com/store/apps/details?id=" + pname
#     data = req.get(url)
#     data = bs(data, features="html.parser")
#     data = bs.prettify(data)  # making data to str type
#
#     icon = re.findall(r'<.*T75of sHb2Xb.*>', data)[0]
#     icon = re.findall(r'(?<=src=)".*?"', icon)[0][1:-1]
#     print(icon)
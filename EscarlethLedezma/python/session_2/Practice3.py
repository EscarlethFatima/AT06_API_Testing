# This function is to return a complete URL if exists


def url_is_present(text):
    if "http://" in text:
        complete_url = text[text.find("http://"):len(text)]
        return complete_url[0:complete_url.find(" ")]


print(url_is_present("this_is a url_http://google.com h"))
print(url_is_present("http://gmail.com "))
print(url_is_present("HTTP://gmail.com "))
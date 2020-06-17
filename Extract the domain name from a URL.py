def domain_name(url):
    if "www" in url:
        return url.split(".")[1].split(".")[-1]
    elif "http" in url:
        return url.split("//")[-1].split(".")[0]
    else:
        return url.split(".")[0].split(".")[0]

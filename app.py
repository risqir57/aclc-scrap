import rouninscrap as rc


def analyst_img(param):
    if 'audio' in param:
        return 'audio'
    elif 'infografis' in param:
        return 'infografis'
    elif 'buku' in param:
        return 'buku'
    elif 'audio-visual' in param:
        return 'audio-visual'
    elif 'boardgame' in param:
        return 'boardgame'
    elif 'website' in param:
        return 'website'


def get_html_by_schema(kat, typ, url):
    go_urls = rc.simple_get(url)
    find_h4 = go_urls.find_all("h4")
    return {
        "kat": kat,
        "sub": typ,
        "link": find_h4
    }
    # if len(find_h4) > 0:
    #     for abs in find_h4:
    #         return abs
    # return False


raw_html = rc.simple_get('https://aclc.kpk.go.id')
p = raw_html.find("li", id="menu-item-313").find_all('a', {"class": "dropdown-item"}, limit=6)
res_array = []
for out in p:
    to_category = rc.simple_get(out['href'])
    getTd = to_category.find("td", bgcolor="#e9ecef")
    if not getTd.find_all("a"):
        continue
    else:
        for sub_list in getTd.find_all("a"):
            types = analyst_img(sub_list['href'])
            to_mate = sub_list['href']
            toscheme = get_html_by_schema(out.text, types, to_mate)
            print(toscheme)

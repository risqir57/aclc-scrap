import rouninscrap as rc


def main():
    mig_data = []
    ignore_sub = ["visual-audio"]
    raw_html = rc.simple_get('https://aclc.kpk.go.id')
    p = raw_html.find("li", id="menu-item-313").find_all('a', {"class": "dropdown-item"}, limit=6)
    for out in p:
        to_category = rc.simple_get(out['href'])
        getTd = to_category.find("td", bgcolor="#e9ecef")
        if not getTd.find_all("a"):
            continue
        else:
            for sub_list in getTd.find_all("a"):
                types = analyst_img(sub_list['href'])
                to_mate = sub_list['href']
                if types not in ignore_sub:
                    toscheme = get_html_by_schema(out.text, types, to_mate)
                    mig_data.append(toscheme)
    print(mig_data)


def analyst_img(param):
    if 'audio-visual' in param:
        return 'audio-visual'
    elif 'infografis' in param:
        return 'infografis'
    elif 'buku' in param:
        return 'buku'
    elif 'audio' in param:
        return 'audio'
    elif 'boardgame' in param:
        return 'boardgame'
    elif 'website' in param:
        return 'website'


def get_html_by_schema(kat, typ, url):
    go_urls = rc.simple_get(url)
    if typ == "website" or typ == "boardgame" or typ == "audio":
        find_element = go_urls.find("td", width="70%").prettify()
    else:
        find_element = go_urls.find_all("h4")
    return {
        "kat": kat,
        "sub": typ,
        "link": find_element
    }


if __name__ == "__main__":
    main()


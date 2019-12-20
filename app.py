import rouninscrap as rc

raw_html = rc.simple_get('https://aclc.kpk.go.id')
p = raw_html.find("li", id="menu-item-313").find_all('a', {"class": "dropdown-item"}, limit=6)


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


def get_html_by_schema(types, url):
    go_urls = rc.simple_get(url)
    find_h4 = go_urls.find_all("h4")
    if not find_h4:
        if types == 'audio':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Audio Visual' and description data '*return step 1'
        elif types == 'infografis':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Infografis' and description data '*return step 1'
        elif types == 'buku':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Buku' and description data '*return step 1'
        elif types == 'audio-visual':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Audio Visual' and description data '*return step 1'
        elif types == 'boardgame':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Boardgame' and description data '*return step 1'
        elif types == 'website':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Website' and description data '*return step 1'
    else:
        if types == 'audio':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Audio Visual' and description data '*return step 1'
        elif types == 'infografis':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Infografis' and description data '*return step 1'
        elif types == 'buku':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Buku' and description data '*return step 1'
        elif types == 'audio-visual':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Audio Visual' and description data '*return step 1'
        elif types == 'boardgame':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Boardgame' and description data '*return step 1'
        elif types == 'website':
            # TODO: Get table > table > td:nth-child(-1) to get all data
            # TODO: Input to table with title 'Website' and description data '*return step 1'
        for ha4 in find_h4:
            # TODO: Get tag a from all h4
            a_tags = ha4.a
            links = a_tags['href']
            texts = a_tags.text
            print(links, texts)



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
            get_html_by_schema(types, to_mate)




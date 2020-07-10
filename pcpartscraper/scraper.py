import requests as rq
from bs4 import BeautifulSoup

class Part:

    def __init__(self,link):
        try:
            self.link = 'https://pcpartpicker.com' + str(link)
            req = rq.get(self.link,headers=rq.utils.default_headers())
            self.soup = BeautifulSoup(req.text,'html.parser')
        except:  raise AttributeError

    def name(self):
        try:  return self.soup.find('h1',class_='pageTitle').get_text()
        except:  return None

    def type(self):
        try:
            type_string = self.soup.find('section',class_='breadcrumb').find('ol')
            return type_string.find('li').find('a').get_text()
        except:  return None

    def amazon_link(self):
        try:
            links = self.soup.find_all('a',href=True)
            badlinks = [
            'https://www.facebook.com/pcpartpicker/',
            'https://www.instagram.com/pcpartpicker/',
            'http://discord.gg/pcpartpicker',
            'https://www.twitter.com/pcpartpicker/',
            'https://www.twitch.tv/pcpartpicker',
            'https://www.youtube.com/pcpartpicker/',
            'https://pcpartpicker.com/',
            'https://cyclingbuilder.com/'
            ]
            for link in links:
                if link['href'][:6] == 'https:' and link['href'] not in badlinks:
                    if 'youtube.com' not in link['href']:
                        if 'amazon.com/tryprimefree' not in link['href']:
                            return link['href']
        except:  return None

    def price(self):
        try:
            string = self.soup.find('td',class_='td__finalPrice')
            return float(string.find('a').get_text().replace('$',''))
        except:  return None

    def advanced_specs(self):
        groups = self.soup.find_all('div',class_='group group--spec')
        return_dict = {}
        for group in groups:
            head_text = str(group.find('h3').text).replace('\n','')
            body_text = str(group.find('div').get_text()).replace('\n','')
            return_dict[head_text] = body_text
        return return_dict

    def url(self):
        return self.link

    def rating(self):
        try:
            rating_html_code = self.soup.find('div',class_="actionBox actionBox__ratings")
            rating_html = rating_html_code.find('ul').find_all('li')[-1]
            num = rating_html.get_text().split(',')[1]
            return float(num.replace(' ','').replace('Average','')[:-1])
        except:  return None

    def reviews(self,results=1):
        reviews = self.soup.find_all('div',class_="partReviews__writeup markdown")
        if results > len(reviews):  results = len(reviews)
        return [x.find('p').text for x in reviews[:results]]

def Query(search_term,results=3,exclude_laptops=False,pages=1):
    try:
        base = 'https://pcpartpicker.com/search/?q='
        url = base + str(search_term).replace(' ','+')
        if results > 20:
            results = 20
        elif exclude_laptops:
            url += '+-laptop'
    except:  return None
    try:
        part_list = []
        for page_n in range(1,pages+1):
            real_url = url + '&page={}'.format(str(page_n))
            search = rq.get(real_url,headers=rq.utils.default_headers())
            html = BeautifulSoup(search.text,'html.parser')
            search_result = html.find('section', class_="search-results__pageContent")
            search_result_list = search_result.find_all('ul',class_='list-unstyled')
            i = 0
            for part in search_result_list:
                link = part.find('li').find('p').find('a',href=True)['href']
                part_list.append(Part(link))
                i += 1
                if i >= results:  break
                continue
        return part_list
    except:
        if len(part_list) > 0:  return part_list
        return None

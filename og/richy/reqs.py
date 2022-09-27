import requests
from rich import inspect, print
from bs4 import BeautifulSoup
from rich.table import Table


def get_html(url):
    r = requests.get(url)
    return r.text

def main():
    url = 'https://news.ycombinator.com/news'
    html_doc = get_html(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    main_table = soup.find('table', attrs={'id':'hnmain'})
    table_entries = main_table.find_all('tr', attrs={'class':'athing'})
    table = Table(title="Hacker News")
    table.add_column("Title", justify="left", style="bold green", no_wrap=True)
    table.add_column("Hyperlink", style="magenta")
    for entry in table_entries:
        link_obj = entry.find('a', attrs={'class':'titlelink'})
        link = link_obj.get('href')
        header = link_obj.text
        # my_str = f"[bold]{header}[/]  [blue]{link}[/]"
        # print(my_str)
        table.add_row(header, link)
    print(table)
    
    
    
main()
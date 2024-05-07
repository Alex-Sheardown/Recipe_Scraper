import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin




from set_Up import openProject
from set_Up import newProject

import requests

import colorama
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET

err_Set = set()
ext_Set = set()
int_Set = set()
con_Set = set()

currentPath = ""
g_Domain_Name = 0
total_urls_visited = 0

current_Limit = 50
count_Of_Urls = 0


#Need to rework this portion


regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$',
    re.IGNORECASE)


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
    # Print New Line on Complete
    """if iteration == total: 
        #print()
        x=0
    """

def is_valid(content):
    status = content.status_code
    if status > 199 or status < 300:
        return True
    else:
        return False


def get_all_website_links(url):

    global err_Set 
    global ext_Set 
    global int_Set
    global con_Set

    global count_Of_Urls
    global currentPath
    global g_Domain_Name
    
    urls = set()
    all_Urls = set()


    results = [[],[],[]]
    full_Connection = str(int_Set[str(url)]) + ": "


    soup = ""
    content = ""
    #header = {"Content-Type": "application",  'Connection': 'close', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    

    #print(url)
    try:
        
        content = requests.get(url)
        """
        with requests.get(url, stream=True) as r:
            content = r
        """
        soup = BeautifulSoup(content.text, 'lxml')
        #soup = BeautifulSoup(content, "html.parser")
        #soup = BeautifulSoup(open(content, 'r'),"html.parser",from_encoding="iso-8859-1")
        #soup = bs4.BeautifulSoup(page, 'lxml')
        x = 0
  
    except:
        f = open(currentPath + "/error.txt", "a", encoding="utf-8")
        #try except
        f.write(str(int_Set.get(url)) + ": " + str(url))
        f.write("\n")
        f.close()
        
        con_Set.add(int_Set[str(url)])
        f = open(currentPath + "/connection.txt", "a", encoding="utf-8")
        #try except
        f.write(url)
        f.write("\n")
        f.write(full_Connection + " NA")
        f.write("\n")
        f.close()
        return urls

    if not is_valid(content):
        f = open(currentPath + "/error.txt", "a", encoding="utf-8")
        #try except
        f.write(str(int_Set.get(url)) + ": " + str(url))
        f.write("\n")
        f.close()
        
        con_Set.add(int_Set[str(url)])
        f = open(currentPath + "/connection.txt", "a", encoding="utf-8")
        #try except
        f.write(str(url))
        f.write("\n")
        f.write(full_Connection + " NA")
        f.write("\n")
        f.close()
        return urls
  

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue

        try:
            href = urljoin(url, href)
        except:
            continue

        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if href in all_Urls:
            continue

        all_Urls.add(href)

        if href in urls:
            #print("repeated: " + href)
            continue

        if href in ext_Set:
            full_Connection = full_Connection + \
                    " " + str(ext_Set.get(href))
            continue

        if href in int_Set:
            full_Connection = full_Connection + \
                    " " + str(int_Set.get(href))
            continue

        if g_Domain_Name not in href:
            ext_Set[str(href)] = count_Of_Urls
            count_Of_Urls = count_Of_Urls + 1

            full_Connection = full_Connection + \
                " " + str(ext_Set.get(href))
            
            url_Num = ext_Set.get(href)
            link_Input = str(url_Num) + ": " + href 
            results[1].append(link_Input)
            
            #print(f"{GRAY}[!] External link: {href}{RESET}")
            continue

        else:
            int_Set[str(href)] = count_Of_Urls
            count_Of_Urls = count_Of_Urls + 1

            full_Connection = full_Connection + \
                " " + str(int_Set.get(href))

            url_Num = int_Set.get(href)
            link_Input = str(url_Num) + ": " + href 
            results[2].append(link_Input)

            #print(f"{GREEN}[*] Internal link: {href}{RESET}")
            urls.add(int_Set.get(href))
            continue
        
    # This fills text document

    #Internal
    #External
    #Error
    #Connection
    
    f = open(currentPath + "/external_links.txt", "a", encoding="utf-8")
    for use in results[1]:
        #try except
        f.write(str(use))
        f.write("\n")
    #f.write(results[1])
    #f.write("\n")
    f.close()
    
    #print(results)
    f = open(currentPath + "/internal_links.txt", "a", encoding="utf-8")
    for use in results[2]:
        #try except
        f.write(str(use))
        f.write("\n")
    #f.write(results[2])
    #f.write("\n")
    f.close()


    con_Set.add(int_Set[str(url)])
    f = open(currentPath + "/connection.txt", "a", encoding="utf-8")
    #try except
    f.write(url)
    f.write("\n")
    f.write(full_Connection)
    f.write("\n")
    f.close()
    return urls


def crawl(url, num):

    global currentPath
    global total_urls_visited
    global int_Set
    global current_Limit
    global count_Of_Urls

    

    if num == current_Limit:
        #print("Current limit reached")
        x = 0
    else:
        
        links = get_all_website_links(url)
        #print(links)
        if links == False:
            crawl(url, num+1)
        else:
            for link in links:
                new_Link = num_To_Url(link)
                    #print(new_Link)
                    #progress(len(total_urls_visited), len(int_Set), "crawling")
                printProgressBar(len(con_Set), len(int_Set.keys())-1, prefix = 'Progress:', suffix = 'Complete', length = 50)
                crawl(new_Link, num+1)
    return False


def num_To_Url(num):
    global int_Set
    return list(int_Set.keys())[list(int_Set.values()).index(num)]


def parseLink(url):
    
    global g_Domain_Name
    global currentPath
    
    g_Domain_Name = urlparse(url).netloc
    folder = urlparse(url).netloc
    currentPath = "./Project/" + folder
    return folder


def find_Missing_Link_To_Crawl():
    global int_Set
    global con_Set

    while len(con_Set) != len(int_Set.keys())-1:
        for key in list(int_Set):
            num = int_Set.get(key)
            if int(num) not in con_Set:            
                if int(num) == -1:
                    continue
                #print(num)
                #print("hello 1 " + key)
                crawl(key, 0)
    printProgressBar(len(con_Set), len(int_Set.keys())-1, prefix = 'Progress:', suffix = 'Complete', length = 50)
    print("This site has been crawled completely!")



def start(url):
    global currentPath
    global count_Of_Urls

    global err_Set 
    global ext_Set 
    global int_Set
    global con_Set

    folder_Name = parseLink(url)


    set_Up = openProject(parseLink(url)) 

    err_Set = set_Up[4]
    ext_Set = set_Up[5]
    int_Set = set_Up[6]
    con_Set = set_Up[7]

    count_Of_Urls = set_Up[3]
  

    if set_Up[0] or set_Up[1]:
        if not set_Up[2]:
            find_Missing_Link_To_Crawl()
    else:
        err_Set = {'test' : -1}
        ext_Set = {'test' : -1}
        int_Set = {'test' : -1}

        int_Set[url] = 0
        newProject(folder_Name)

        f = open(currentPath + "/internal_links.txt", "w", encoding="utf-8")
        f.write("0: " + url)
        f.write("\n")
        f.close()
        print("Starting crawl...")    
        crawl(url, 0)
        find_Missing_Link_To_Crawl()
    

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(
        description="Link Extractor Tool with Python")
    parser.add_argument("url", help="The URL to extract links from.")
    parser.add_argument("-m",
                        "--max-urls",
                        help="Number of max URLs to crawl, default is 30.",
                        default=30,
                        type=int)
    #parser.add_argument("-m", "--max-urls", help="Number of max URLs to crawl, default is 30.", default=30, type=int)

    args = parser.parse_args()
    url = args.url
    start(url)
    
    




    #print(set_Up)
    
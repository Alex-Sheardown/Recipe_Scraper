import networkx as nx
from pyvis.network import Network
from set_Up import openProject
from check_Links import parseLink
from check_Links import num_To_Url
import matplotlib.pyplot as plt

err_Set = set()
ext_Set = set()
int_Set = set()
con_Set = set()

G = nx.Graph()

folder = ""


def get_key(val):
    for key, value in int_Set.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def build_Graph(folder):
    
    global G
    global int_Set

    path = "./Project/" + folder
    print(get_key(str(122)))

    for x in int_Set:
        G.add_node(x)


    with open(str(path + "/connection.txt"), encoding='UTF8', errors='ignore') as fp:
        
        name_Of_Page = ""
        number = 0
        Lines = fp.readlines()
        
        for line in Lines:
    
            if line[0].isnumeric():
                for element in range(0, len(line)):
                    if ':' == (line[element]):
                        number = int(line[:element])

                        #G.add_node(get_key(str(number)))
                        arr = line[element+2:].split(" ")
                        for edge in arr:
                            G.add_edge(get_key(str(number)), get_key(str(edge)))
                        #print(line[element:])

                            
            
    result = [con_Set]
    return result

def start(url):

    global err_Set 
    global ext_Set 
    global int_Set
    global con_Set

    global G

    folder_Name = parseLink(url)
    set_Up = openProject(parseLink(url)) 

    err_Set = set_Up[4]
    ext_Set = set_Up[5]
    int_Set = set_Up[6]
    con_Set = set_Up[7]

    count_Of_Urls = set_Up[3]
  

    if set_Up[0] or set_Up[1]:
        if not set_Up[2]:
            print("Crawl is incomplete; partial visual network is being made...")
        else:
            print("Crawl is complete; visual network is being made...")
            build_Graph(folder_Name)
    else:
        print("There are missing files; visual network cannot be made.")



    print(f"digraph has {nx.number_of_nodes(G)} nodes with {nx.number_of_edges(G)} edges")
    
    """
    UG = G.to_undirected()
    print(nx.number_connected_components(UG), "connected components")
    options = {
        "node_color": "black",
        "node_size": 1,
        "edge_color": "gray",
        "linewidths": 0,
        "width": 0.1,
    }
    """
    
    

  
    
   
    nt = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
    nt.show_buttons(filter_=['physics'])
    nt.barnes_hut()
    nt.from_nx(G)
    nt.show('nx.html')
  
    

def start2():
    x = 0



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

    G = nx.Graph()



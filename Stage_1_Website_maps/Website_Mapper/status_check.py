import os
from set_Up import read_Con_File 
from set_Up import read_Int_File 

def write_to_file(text):
    f = open("Status of projects.txt", "a")
    f.write(text + "\n")
    f.close()




def main(path_for_site_info):
    
    cwd = os.getcwd()
    
    
    path_for_site_info = cwd + path_for_site_info
    path_for_site_info = path_for_site_info.replace("\\", "/")
    

    list_subfolders_with_paths = [f.path for f in os.scandir(path_for_site_info) if f.is_dir()]

    #print(list_subfolders_with_paths)
    
    f = open("Status of projects.txt", "w")
    f.close()
    for site in list_subfolders_with_paths:
    
        #site.replaceopenProject(("\\", "/")
        #print("is the crawl finished " + str(openProject(site)[2]))
        result = read_Con_File(site)
        con_Set = result[0]
        result = read_Int_File(site, 0)
        int_Set = result[0]

        site.replace("path_for_site_info", "")
        if len(con_Set) == len(int_Set.keys())-1:
            #print("This site has been crawled completely!")
            write_to_file(site + "      : Completed")

        else:
            #print("This site needs more work")
            write_to_file(site + "      : Incomplete")
        
  
   

main("/Collections/Version 8/Project")



#C:/Users/alexa/Desktop/Machine Learning/Recipe Project/Collections/Version 8/Project
#C:/Users/alexa/Desktop/Machine Learning/Recipe Project/Version 8/Project
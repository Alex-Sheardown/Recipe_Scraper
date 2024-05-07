
import os

#might replace with a simple hash check
def checkIfAllLinks(int_Set, con_Set):
    #print("Checking if Done..")
    
   
    if len(con_Set) != len(int_Set.keys())-1:
        return False
    
    
    for key in list(int_Set):
        num = int_Set.get(key)

        if int(num) not in con_Set:
            #print(num)
            if int(num) == -1:
                continue
            print(num)
            #print("Not all links are found...")
            #print("Resuming Crawl")
            return False
   #need to give check
    """
    print("Current Site has no new links!!!")
    printProgressBar(len(con_Set), len(int_Set.keys()), prefix = 'Progress:', suffix = 'Complete', length = 50)
    """
    return True




#redo
#Need number to keep track of Urls
def read_Err_File(path, count_Urls):
    err_Set = set()
    err_Set = {'test' : -1}
    with open(str(path + "/error.txt"), encoding='UTF8', errors='ignore') as fp:
        Lines = fp.readlines()
        for line in Lines:
            count_Urls = count_Urls + 1
            for element in range(0, len(line)):
                try:
                    if ':' == (line[element]):
                        url = str(line[2+element:-1])
                        number = int(float(line[:element]))
                        err_Set[url] = str(number)
                except:
                    break
    result = [err_Set, count_Urls]
    return result


def read_Ext_File(path, count_Urls):
    ext_Set = set()
    ext_Set = {'test' : -1}
    with open(str(path + "/external_links.txt"), encoding='UTF8', errors='ignore') as fp:
        Lines = fp.readlines()
        for line in Lines:
            count_Urls = count_Urls + 1
            for element in range(0, len(line)):
                try:
                    if ':' == (line[element]):
                        url = str(line[2+element:-1])
                        number = int(float(line[:element]))
                        ext_Set[url] = str(number)
                except:
                    break
    result = [ext_Set, count_Urls]
    return result


def read_Int_File(path, count_Urls):
    int_Set = set()
    int_Set = {'test' : -1}
    with open(str(path + "/internal_links.txt"), encoding='UTF8', errors='ignore') as fp:
        Lines = fp.readlines()
        for line in Lines:
            #print(line)
            
            for element in range(0, len(line)):
                try:
                    if ':' == (line[element]):
                        url = str(line[2+element:-1])
                        number = int(float(line[:element]))
                        int_Set[str(url)] = str(number)
                        count_Urls = count_Urls + 1
                except:
                    break
    
    result = [int_Set, count_Urls]
    return result 


def read_Con_File(path):
    con_Set = set()
    with open(str(path + "/connection.txt"), encoding='UTF8', errors='ignore') as fp:
        Lines = fp.readlines()
        for line in Lines:
            try:
                if line[0].isnumeric():
                    for element in range(0, len(line)):
                        if ':' == (line[element]):
                            number = int(line[:element])
                            con_Set.add(number)
            except:
                break
    result = [con_Set]
    return result


def newProject(folder):
    
    print("Creating New site folder...")
    currentPath = "./Project/" + folder
    
    if not os.path.exists("./Project"):
        os.makedirs("./Project")
    
    addOn = "/internal_links.txt"
    os.makedirs(os.path.dirname(currentPath + addOn), exist_ok=True)
    with open(currentPath + addOn, "w") as f:
        f.write("")
        f.close

    addOn = "/external_links.txt"
    os.makedirs(os.path.dirname(currentPath + addOn), exist_ok=True)
    with open(currentPath + addOn, "w") as f:
        f.write("")
        f.close

    addOn = "/error.txt"
    os.makedirs(os.path.dirname(currentPath + addOn), exist_ok=True)
    with open(currentPath + addOn, "w") as f:
        f.write("")
        f.close

    addOn = "/connection.txt"
    os.makedirs(os.path.dirname(currentPath + addOn), exist_ok=True)
    with open(currentPath + addOn, "w") as f:
        f.write("")
        f.close
    

#Should be able to pull double duty
def openProject(folder):
    err_Set = set()
    ext_Set = set()
    #Might need to break down into more sets
    int_Set = set()
    con_Set = set()

    previous_crawl_Test = False
    finished_Crawl_Test_pass = False
    all_Files_Found_Test_Pass = False
    

    starting_Number = 0

    if os.path.exists("./Project"):
        currentPath = "./Project/" + folder

        #Add Color coding ?
        stage = 0
        print("Checking for previous crawl")
        if os.path.exists(currentPath):
            print("Previous crawl found, checking integrity...")
            stage = 1
            previous_crawl_Test = True
            if os.path.exists(currentPath + "/internal_links.txt"):
                result = read_Int_File(currentPath, 0)
                int_Set = result[0]
                starting_Number =  result[1]
                print("stage " + str(stage) + ": Complete")
                stage = 2
                if os.path.exists(currentPath + "/external_links.txt"):
                    result = read_Ext_File(currentPath, starting_Number) 
                    ext_Set = result[0]
                    starting_Number =  result[1]
                    print("stage " + str(stage) + ": Complete")
                    stage = 3
                    if os.path.exists(currentPath + "/connection.txt"):
                        result = read_Con_File(currentPath)
                        con_Set = result[0]
                        #starting_Number =  result[1]
                        print("stage " + str(stage) + ": Complete")
                        stage = 4
                        if os.path.exists(currentPath + "/error.txt"):
                            #result = read_Err_File(currentPath)
                            #err_Set = result[0]
                            #starting_Number =  result[1]
                            print("stage " + str(stage) + ": Complete")
                            print("All stages are complete")
                            
                            all_Files_Found_Test_Pass = True

                            print("Checking if crawl completed...")
                            int_Set['test'] = -1
                            #print(len(con_Set))
                            #print(len(int_Set.keys())-1)
                            if len(con_Set) == len(int_Set.keys())-1:
                                print("This site has been crawled completely!")
                                finished_Crawl_Test_pass = True 
                            else:
                                percentage_of_mapped_Urls = len(con_Set) / len(int_Set)
                                #print("This crawl incomplete " + str(percentage_of_mapped_Urls) + " done resuming...")
                                print("This crawl is incomplete; the program will now resume...")
                        else:
                            print("stage " + str(stage) + ": Fail")
                    else:
                        print("stage " + str(stage) + ": Fail")
                else:
                    print("stage " + str(stage) + ": Fail")
            else:
                print("stage " + str(stage) + ": Fail")
        else:
            print("Previous crawl not found...")

    all_Sets = [previous_crawl_Test, all_Files_Found_Test_Pass, finished_Crawl_Test_pass, starting_Number ,err_Set, ext_Set, int_Set, con_Set]
    return  all_Sets
                    
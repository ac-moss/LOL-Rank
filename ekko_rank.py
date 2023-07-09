from urllib.request import Request,urlopen
from bs4 import BeautifulSoup



# Basic attempt using urllib
def get_rank_global(html):
    rank_index_start = html.find("number-medium solo-number")  
    while(html[rank_index_start] != '#' ):
        rank_index_start = rank_index_start +1 



    rank_index_end = rank_index_start
    while(html[rank_index_end] != '<' ):
        rank_index_end = rank_index_end +1 


    rank = html[rank_index_start:rank_index_end]
    rank.replace(" ","")
    print("Global rank is: " + rank)
    return rank



#cleaner version using BeautifulSoup
def get_rank_NA(html):

    #Feed raw html into BS to create new instance 
    soup = BeautifulSoup(html, "html.parser")

    #Find all mentions of "number-medium solo-number" this is the class that shows ranks for both global and NA
    ranks = soup.find_all('div', { "class": "number-medium solo-number"})

    #NA will always be second found in the html, convert this value to string and remove whitespace
    clean_rank = ranks[1].text.replace(" ","")
    clean_rank = clean_rank.replace("\n","")
    print("Na rank is: " + clean_rank)
    return clean_rank
    




def main():
    while(1):
        #Send request to webpage to get html, have to send request as website would allow non-user agents to access data
        req = Request(
            url = "https://www.leagueofgraphs.com/summoner/champions/ekko/na/Gh%C3%ADll%C3%ADe",
            headers={'User-Agent': 'Mozilla/5.0'}
        )

        #Read in HTML and create element 
        page = urlopen(req).read()
        html = page.decode("utf-8")


        global_rank = get_rank_global(html)
        NA_rank = get_rank_NA(html)

        sec = input('Press q to quit, or any other key to run again.\n')
        if sec == "q":
            break
if __name__ == "__main__":
    main()
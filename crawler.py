from bs4 import BeautifulSoup
import get_links
import requests
import get_tables
import check_new
linklist = get_links.fromURL(r"https://ec.europa.eu/info/strategy/priorities-2019-2024/european-green-deal/delivering-european-green-deal_en#documents")


print(len(linklist.get())) # Printing number of links
print(*linklist.get(), sep="\n") # Printing all links to the documents

for link in linklist.get():

    r  = requests.get(link)
    data = r.text

    soup = BeautifulSoup(data, "lxml")
    name = soup.find("p", {"class": "Rfrenceinstitutionnelle"}).text
    tables = soup.find_all('table')

    for idx, table in enumerate(tables):
        print("########: ", table)

        with open("tables_html/{}_{}.html".format(name, idx), 'w') as outfile:
            outfile.write(str(table))



    # #tables.get().to_csv("table_csv/test.csv", sep='\t', encoding='utf-8')
    # print(type(tables.get()))
    # for key, value in tables.get().items():
    #     for idx, table in enumerate(value):
        
    #         print("#####", type(table))
    #         table.to_csv("table_csv/{}_{}.csv".format(key, idx), sep=';', encoding='utf-8')

#check_new.check()

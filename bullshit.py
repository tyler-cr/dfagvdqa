from bs4 import BeautifulSoup
import requests

def generateListWithMaxAndMin(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    htmlList = []
    i = 0

    maxX = 0
    maxY = 0

    for tableRows in soup.find_all("tr"):
        
        htmlList.append([])

        for element in tableRows.find_all(class_="c0"):
            htmlList[i].append(element.text)

        try:
            curXCoord = int(htmlList[i][0])
            curYCoord = int(htmlList[i][2])

            if maxX < curXCoord: 
                maxX = curXCoord
            if maxY < curYCoord: 
                maxX = curYCoord
                
        except ValueError:
            pass

        i+=1


    htmlList = htmlList[1:]
    return [htmlList, maxX, maxY]

def generateOrganizedList(tripList):

    dataList = tripList[0]

    maxX = tripList[1]
    maxY = tripList[2]

    organizedList = [[None for _ in range(maxX)] for _ in range(maxY)]

    for data in dataList:
        organizedList[data[2]][data[0]] = data[1]

    return organizedList

def decipherCode(url):
    tripList = generateListWithMaxAndMin(url)
    test = generateOrganizedList(tripList)
    print(test)

decipherCode("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")

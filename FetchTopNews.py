#Importing Packages
import requests

def BBCNews():
    #BBC News API Key
    url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=PASTE_YOUR_API_KEY"

    #Fetching data in Json Format
    open = requests.get(url).json()

    #Getting all articles in a string format
    article = open["articles"]

    #Empty list which will contains news
    results =[]

    for a in article:
        results.append(a["title"])
    for i in range(len(results)):
        print(i+1, results[i]) #print news

    #To speak the news
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)

#main
if __name__ == "__main__":
    BBCNews() #Function Calling
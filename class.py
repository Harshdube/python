from threading import main_thread


class Anime(object):
    def __init__(self,name,author,genre,year,season) :
        self.name=name
        self.author=author
        self.genre=genre
        self.year=year
        self.season=season

    def printValue(self):
        print("name of the anime is ",self.name)
        print("name of the author is ",self.author)
        print("name of the genre is ",self.genre)
        print("name of the year is ",self.year)
        print("number of the season is ",self.season)

    def addseason(self):
        self.season=self.season+1
    
def main():
    demonslayer=Anime("demonslayer"," Koyoharu Gotouge","Adventure fiction, Dark fantasy, Martial Arts","2011",23)
    demonslayer.printValue()
    demonslayer.addseason()
    demonslayer.printValue()
        
main()

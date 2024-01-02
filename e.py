class Temps :
    def __init__(self,h=0,m=0,sec=0):
        self.__h = h
        self.__m = m
        self.__sec = sec

    def getHours(self):
        return self.__h
    
    def getMin(self) :
        return self.__m
    
    def getSec(self) :
        return self.__sec
    
    def affichetemps(self):
        print(self.__h,"H",self.__m,'min',self.__sec,"sec")

    def ajouterTemps(self,t1,t2):
        self.__sec= t1.__sec+ t2.__sec
        self.__m = t1.__m + t2.__m+ (int(self.__sec/60))
        self.__h = t1.__h + t2.__h + (int(self.__m/60))
        self.__m %= 60
        self.__sec %= 60

temps1 = Temps(2,58,40)
temp2= Temps(1,25,40)
temp3 = Temps()
temps1.affichetemps()
temp2.affichetemps()
temp3.ajouterTemps(temps1, temp2)
temp3.affichetemps()



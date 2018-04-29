
class Person(object):
    """description of class"""
    def __init__(self,inName,inAge):
        self.__name = inName
        self.__age = inAge

    def getInfo(self):
        #return "Name:{Name},Age:{Age}".format(Name = self.__name,Age = self.__age)
        return {"Name":self.__name,"Age":self.__age}

    def __str__(self):
        return "{className}({Info})".format( className = type(self),Info = self.getInfo())


if __name__ == "__main__":
    p = Person("laowan",10)
    print(p)

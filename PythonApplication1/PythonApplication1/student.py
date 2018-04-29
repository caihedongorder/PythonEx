import Person

class student(Person.Person):
    """description of class"""
    def __init__(self, inName, inAge, inNumber):
        self.__Number = inNumber
        return super(student, self).__init__(inName, inAge)
    
    def getInfo(self):
        info =  super(student, self).getInfo()
        info["Number"] = self.__Number
        return info

if __name__ == "__main__":
    s = student("xiaowang",10,1023443)
    print(s)



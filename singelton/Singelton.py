class singelclass:
    __instance = None
    def __init__(self, name):
        self.name = name
    def Instance(self, name):
        if self.__instance == None:
            self.__instance = singelclass(name= name)
        return self.__instance
    
ins1 = singelclass.Instance(name='class1')
# print(ins1.Instance().name)

ins2 = singelclass.Instance(name='class2')
print(ins2.Instance().name, ins1.Instance().name)

# print(type(ins1).__name__ )

class StringClass:
    def getString(self):
        self.str=input()
    def printString(self):
        print(self.str.upper())

processor = StringClass()
processor.getString()
processor.printString()
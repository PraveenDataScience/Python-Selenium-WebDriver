class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Configuration is : ",self.cpu,self.ram)

com=Computer("Ryzon",500)
com.config()

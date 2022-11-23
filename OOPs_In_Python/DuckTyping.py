class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditior:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell Checkig")
        print("Convention Check")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=MyEditior()

lap=Laptop()
lap.code(ide)
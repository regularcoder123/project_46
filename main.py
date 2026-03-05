class robot:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def introduction(self):
        print(f'''Robot Name: {self.name}
color: {self.color} ''')
        
robot1 = robot("Mark-42","Red")
robot1.introduction()
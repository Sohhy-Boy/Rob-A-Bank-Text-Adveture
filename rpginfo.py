class RPGInfo():
    author = "Soham Games Corp"
    
    def __init__(self, game_title):
        self.title = game_title
    
    def welcome(self):
        print("Welcome to " + self.title)

    @staticmethod
    def info():
        print("Credits to Mr BURDEN")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
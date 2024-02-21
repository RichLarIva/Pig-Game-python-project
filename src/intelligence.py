"""Class for the intelligence of the \"AI\""""

class Intelligence:
    intelligence_level = 0
    def __init__(self):
        ai_level = prompt("What difficulty do you want?\n1 or 2: ")
        if(ai_level == "1" or ai_level == "2"):
            self.intelligence_level = int(ai_level)

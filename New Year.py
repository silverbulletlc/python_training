class Year:
    def __init__(self, num, slogan):
        self.num = num
        self.slogan = slogan
        
    def speak(self):
        print("{} , the year of {}".format(self.slogan, self.num))
        
year_2022 = Year(num=2022, slogan="Fuck you")
year_2023 = Year(num=2023, slogan="Treat me friendly")
year_2022.speak()
year_2023.speak()
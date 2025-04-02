# 엉터리방터리 클래스 연습장

class Story:
    def __init__(self, sound, color):
        self.sound=sound
        self.color=color
    def say(self):
        return self.sound
    def outfit(self):
        return self.color
    def storyteller(self):
        return print(f"{self.outfit}{str(self)} {self.say}")

wolf=Story('Awoooool', 'gray')

wolf.storyteller()
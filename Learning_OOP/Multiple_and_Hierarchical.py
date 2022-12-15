
# Multiple Inheritance

class Cat:

    def meow(self):
        print("Meow!")


class Talker:

    def say(self, to_say):
        print(to_say)


class TalkingCat(Cat, Talker):
    pass


# Instance of talkingCat
salem = TalkingCat()

print("In this instance, TalkingCat inherits from Cat. TalkingCat says: ")
salem.meow()

print("Now, TalkingCat inherits from Talker. TalkingCat says: ")
salem.say("Hello!")

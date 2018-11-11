
#Leuphana University
#Module: 42027000 Technological Basics I
#Lecture: [7628] Tech Basics I, Stream B (lecture)
#Instructor: Helena Lingor
#Name: Crystal Palima Yip
#Matrikel: 3031775


#This is a direct game where you stumble upon an arrogant psychic and he grants you one wish. Feel free to check his predictions! :)


# Lists of possible answers from user
positive = ['Yes','y','Y','yes']
negative = ['No','n','no','N']

def greet():

#User encounters the psychic and gets a greeting from him
    print ("Who is that?! Please come forward and reveal your name!")
    name = raw_input("Who are you?! Tell me your name ")
    print ("Pleased to meet your acquiantance, " + name)
    country = raw_input("So where does you come from? ")
    print ("Interesting, a human.")
    print ("Seeing how far you've come, I'll grant you a piece of pleasure from my powers. I can read your future.")


    choice = raw_input("Would you like to receive a psychic reading? Yes/No? ")

#When user agrees to get a reading, they have the options to choose between career, love & health

#this line lets line 35 know what elements are included in 'pos'
    for pos in positive:

        if choice == pos:

            print ("Which aspects of your life would you like a reading on? Only one choice ")
            AspChoice = raw_input("Career/Love/Health ")

            if AspChoice == 'career':
                c = open("career.txt", "r") #opens prediction for 'career'
                c2 = open("money.TXT", "r")
                carRead = c.read()
                carImage = c2.read()
                print carImage
                print carRead
                print ("That's all for for your reading, hope you liked it. Farewell, human!")


            if AspChoice == 'love':
                l = open("love.txt")  #opens prediction for 'love'
                l2 = open("heart.TXT", "r")
                lovRead = l.read()
                lovImage = l2.read()
                print lovImage
                print lovRead
                print ("That's all for for your reading, hope you liked it. Farewell, human!")

            if AspChoice == 'health':
                h = open("health.txt")  #opens prediction for 'health'
                h2 = open("body.TXT", "r")
                healRead = h.read()
                healImage = h2.read()
                print healImage
                print healRead
                print ("That's all for for your reading, hope you liked it. Farewell, human!")


    for neg in negative: #this line lets line 70 know what elements are included in 'neg'
        if choice == neg:

            print("Alrighty then, I guess I don't need to waste my powers. Be gone!")




greet();


#References:
#2018 Horoscopes for Every Sign: Your 2018 Astrology Yearly Forecast by The AstroTwins, Ophira and Tali Edut. (2018).
#Astrostyle: Astrology and Daily, Weekly, Monthly Horoscopes by The AstroTwins from http://astrostyle.com/2018-horoscope/

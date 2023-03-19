import random
import os
# DEFINING CHARS

water = "\033[0;36m~\033[0m"
rocks = "\033[1;30m%\033[0m"
grass = "\033[1;32m#\033[0m"
house = "\u001b[33m[@]\033[0m"
# DEFINING CONFIG
steps = 75 # More steps = Bigger gen
digit = [1,2,3,4,5,6,7,8,9,0,10]
belief = 100
happiness = random.randint(87,101)
unbeliefamine = random.randint(20,100)
unbeliefalien = random.randint(55,100)
unbeliefplague = random.randint(0,45)
unbeliefriot = random.randint(0,5)
year = random.randint(130,3200)
prefix = ["Mink", "Monk", "Lanch", "Lexin", "Reg", "Temple", "Dream", "Fullab", "Side", "Dillin", "Gillin", "Saul", "Farwle", "Kotlin", "Yava", "K-", "Jinva", "Prelix", "Pogla", "Mogleg", "Bogleg", "Bruck", "Broos", "Kuhj"] #Prefixes for town names
suffix = ["land", "topia", "wirld", "tain", "-klog", "zania", "la", "troga", "landzia", "tropolis", "landia", "tropolia", "bolgia", "garia", "naria", "sharia", "flaria", "seria", "sarihaj", "licha", "world"] #Suffixes for prefixes
economy = prefix[random.randint(0,len(prefix)-1)]
economy = economy[0:3].upper()
mood = ["Excited for the future", "Happy but weary", "Excited due to a new religion spreading", "Happy because of the passing of a virus", "Upset due to the death of their leader", "Devestated due to the death of their king", "Greiving over the death of the queen's child.", "Mourning the death of the prince of the western region", "Starving and sad, there is a plague going around which attacks the cells of crops and feeds off them.", "Despising the new ruler who promises to destroy prosperity in the southern region.", "Happy because of a new ruler", "Going through a mass epidemic of glucopsi, a cell virus which degrades the muscle joints.", "Going through mass panic because of the new religion's leader, who is inciting underworld values subliminally.", "Trying to form a coup to overtake the north western prince, who was caught trying to assasinate a town mayor from the south western region.", "Happy at the election of the first leader who has come from the underprivaged south east region", "Happy at the death of the king who casted the country under 10 years of bad rule", "Happy at a new queen and king being elected", "Sad at a new queen being elected as she comes from an eletist north east region", "Happy at a new king being elected.", "Scared, they know they live in a command line", "Worried, they know a god is watching over them", "Afraid, they know they live in a terminal", "Terrified, they know of their whereabouts, they know that "+str(os.getlogin())+" is watching them inside a terminal", "Depressed because of a famine"]
faminemood = ["are Dying, from the famine caused by you", "are Depressed after being afflicted with a famine from above", "are Planning to escape their terminal window as they have become distrustful of you as a god", "Now have turned against rseligion after being poisened in the famine of "+str(year),"have stopped believing in you, in total "+str(unbeliefamine)+r"% of people stopped believing in you...", "are plotting against their local preist..."]
plaguemood = ["Now have turned against religion after being poisened in the plague of "+str(year),"have stopped believing in you, in total "+str(unbeliefplague)+r"% of people stopped believing in you...", "are dying from the virus you unleashed", "are wearing masks to prevent another virus, they are weary of you.", "are scared, they belive they upset you in some way...", "are sacrificing animals at an alter for you, they belive they made a mistake.", "are forgiving of you.", "are depressed and low.", "are practicing different relgions as "+str(unbeliefplague)+r"% of people stopped believing in you...", "are forming new governments..."]
metmood = ["Now have turned against religion after being injured in the meteor of "+str(year),"have stopped believing in you, in total "+str(unbeliefplague)+r"% of people stopped believing in you...", "are dying from the meteor you unleashed", "are wearing pointy cone hats to prevent another virus, they are weary of you.", "are scared, they belive they upset you in some way...", "are sacrificing veggies at an alter for you, they belive they made a mistake.", "are forgiving of you.", "are depressed and low.", "are practicing different relgions as "+str(unbeliefplague)+r"% of people stopped believing in you...", "are forming new governments..."]
riotmood = ["are unhappy with the government after the riots of "+str(year),"have stopped believing in you, in total "+str(unbeliefriot)+r"% of people stopped believing in you...", "are dying from the riots you unleashed", "are wearing riot sheilds made from birch bark to prevent death from riots, they are weary of you.", "are having mass suicide events", "are sacrificing leaves at an alter for you, they belive they made a mistake.", "are forming a new government", "are depressed and low.", "are practicing different religions as "+str(unbeliefriot)+r"% of people stopped believing in you...", "are forming new governments..."]
passive_alienmood = ["are delighted with the alien visit of "+str(year),"have increased their belief in you, in total "+str(unbeliefalien)+r"% of people increased their faith in you...", "are a bit rattled from the visit but excited and happy they were passive", "are wearing alien fashion, a new genre that was created with the alien craze of "+str(year), "are enjoying life", "are sacrificing alien goo at an alter for you, they belive they owe it to you.", "are forming a new government", "are happy and trying alien crystal drugs.", "are removing different religions as "+str(unbeliefalien)+r"% of people converted into believing in you...", "are forming new governments..."]
alienmood = ["are unhappy with the government after the alien incident of "+str(year),"have stopped believing in you, in total "+str(unbeliefalien)+r"% of people stopped believing in you...", "are dying from the aliens you unleashed", "are wearing alien sheilds made from physcadelic plant stems to prevent death from aliens, they are weary of you.", "are having mass suicide events", "are sacrificing alien babies at an alter for you, they belive they made a mistake.", "are forming a new anti-alien government", "are depressed and low.", "are practicing different religions as "+str(unbeliefalien)+r"% of people stopped believing in you...", "are forming new governments..."]
gravmood = ["are unhappy with the violation of physics, circa "+str(year),"have stopped believing in you, in total "+str(unbeliefalien)+r"% of people stopped believing in you...", "are dying from gravity not giving a fuck", "are crowding under trees as to not die.", "are having mass suicide events", "are sacrificing their shoes at an alter for you, they belive they made a mistake.", "are forming a new anti-gravity government", "are depressed and high.", "are practicing different religions as "+str(unbeliefalien)+r"% of people stopped believing in you...", "are forming new governments..."]
goodharvestmood = ["are excited with the harvest", "are well fed", "are excited to eat food", "are thriving now that their economy is up"]
economicboostmood = ["are excited with the economic boom", "have alot more money", "are excited to eat food properly", "are thriving now that their economy is up"]
economicdownturnmood = ["are depressed with the economic downturn", "have alot less money", "are sad that they cannot eat food properly", "are depressed now that their economy is down"]
map = []
name = str(str(prefix[random.randint(0,len(prefix)-1)])+str(suffix[random.randint(0,len(suffix)-1)]))
population = 0
for i in range(steps):
    chance = random.randint(0,3) # Random num generated to pick what to insert into the map array for each step
    if chance == 0:
        map.append(water*random.randint(20,50))
    if chance == 1:
        map.append(rocks*random.randint(0,5))
    if chance == 2:
        map.append(grass*random.randint(30,55))
    if chance == 3:
        amount = random.randint(0,3)
        map.append(house*amount)
        for i in range(amount):
            population += random.randint(1,6)
        

map = "".join(map)
print(map)
print("STATS:")
print("---------------")
print("NAME: "+name)
print("POPULATION: "+str(population))
print("YEAR: "+str(year))
print("BELIEF IN YOU: "+str(belief)+"%")
print("HAPINESS: "+str(happiness))
economy_status = random.randint(0,1)
economy_rate = random.random()
if economy_status == 0:
    print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"\033[0m")
if economy_status == 1:
        print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"\033[0m")
print("STATUS:\nThe citizens of "+name+" are "+str(mood[random.randint(0, len(mood)-1)]))
population = population
#try:
while True:
    print("\nMerciful Lord, you have a choice. What do you want to unleash upon these terminalites...\n1. Famine\n2. Plague\n3. Meteor\n4. Riots\n5. Alien attack\n6. Flip Gravity\n7. Mass Paronoia\n8. Good harvest\n9. Economic Recession")
    choice = input(">")
    choice = choice.strip()
    if choice != "break":
        choice = int(choice)
    if choice == 1:
        unbeliefamine = random.randint(20,100)
        map = map.replace("#","\u001b[33m#\033[0m")
        map = map.replace("~","\033[0;37m~\033[0m")
        print(map)
        deathcount = random.randint(0,population)
        population = population-deathcount
        sadness = random.randint(0,45)
        belief = belief - unbeliefamine
        happiness = happiness - sadness

        print("STATS:")
        print("---------------")
        print("NAME: "+name)
        print("POPULATION: "+str(population))
        print("\u001b[31m-"+str(deathcount)+" people died in the famine\033[0m")
        print("YEAR: "+str(year+random.randint(1,10)))
        print("BELIEF IN YOU: "+str(belief)+"%")
        print("\u001b[31m-"+str(unbeliefamine)+r"% belief"+"\033[0m")
        print("HAPINESS: "+str(happiness))
        print("\u001b[31m-"+str(sadness)+" hapiness\033[0m")
        economy_status = random.randint(0,1)
        economy_rate = random.random()
        if economy_status == 0:
            print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"%"+"\033[0m")
        if economy_status == 1:
            print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"%"+"\033[0m")
        print("STATUS:\nThe citizens of "+name+" "+str(faminemood[random.randint(0, len(faminemood)-1)]))
        
    if choice == 2:
        unbeliefplague = random.randint(0,45)
        map = map.replace("##","\033[0;33m#\033[0m\033[1;32m#\033[0m")
        map = map.replace("~","\033[0;35m~\033[0m")
        print(map)
        deathcount = random.randint(0,population)
        population = population-deathcount
        sadness = random.randint(0,54)
        happiness = happiness - sadness
        belief = belief - unbeliefplague
        print("STATS:")
        print("---------------")
        print("NAME: "+name)
        print("POPULATION: "+str(population))
        print("\u001b[31m-"+str(deathcount)+" people died as a result of the plague\033[0m")
        print("YEAR: "+str(year+random.randint(1,10)))
        print("BELIEF IN YOU: "+str(belief)+"%")
        print("\u001b[31m-"+str(unbeliefplague)+r"% belief"+"\033[0m")
        print("HAPINESS: "+str(happiness))
        print("\u001b[31m-"+str(sadness)+" hapiness\033[0m")
        economy_status = random.randint(0,1)
        economy_rate = random.random()
        if economy_status == 0:
            print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"%"+"\033[0m")
        if economy_status == 1:
            print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"%"+"\033[0m")
        print("STATUS:\nThe citizens of "+name+" "+str(faminemood[random.randint(0, len(faminemood)-1)]))
    if choice == 3:
        unbeliefplague = random.randint(0,45)
        map = map.replace("[@]","\033[0;31m{@}\033[0m")
        map = map.replace("~","\033[1;30m~\033[0m")
        map = map.replace("#", "\033[0;33m#\033[0m")
        print(map)
        deathcount = random.randint(0,population)
        sadness = random.randint(0,55)
        population = population-deathcount
        belief = belief - unbeliefplague
        happiness = happiness - sadness
        print("STATS:")
        print("---------------")
        print("NAME: "+name)
        print("POPULATION: "+str(population))
        print("\u001b[31m-"+str(deathcount)+" people died as a result of the meteor\033[0m")
        print("YEAR: "+str(year+random.randint(1,10)))
        print("BELIEF IN YOU: "+str(belief)+"%")
        print("\u001b[31m-"+str(unbeliefplague)+r"% belief"+"\033[0m")
        print("HAPINESS: "+str(happiness))
        print("\u001b[31m-"+str(sadness)+" hapiness\033[0m")
        economy_status = random.randint(0,1)
        economy_rate = random.random()
        if economy_status == 0:
            print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"%"+"\033[0m")
        if economy_status == 1:
            print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"%"+"\033[0m")
        print("STATUS:\nThe citizens of "+name+" "+str(metmood[random.randint(0, len(metmood)-1)]))
    if choice == 4 and population > 5:
        unbeliefriot = random.randint(0,5)
        map = map.replace("[@]","\033[0;31m{@}\033[0m")
        map = map.replace("#####", "####\033[0;33m#\033[0m")
        print(map)
        deathcount = random.randint(0,population)
        sadness = random.randint(0,75)
        population = population-deathcount
        belief = belief - unbeliefriot
        happiness = happiness - sadness
        print("STATS:")
        print("---------------")
        print("NAME: "+name)
        print("POPULATION: "+str(population))
        print("\u001b[31m-"+str(deathcount)+" people died as a result of the riots\033[0m")
        print("YEAR: "+str(year+random.randint(1,10)))
        print("BELIEF IN YOU: "+str(belief)+"%")
        print("\u001b[31m-"+str(unbeliefplague)+r"% belief"+"\033[0m")
        print("HAPINESS: "+str(happiness))
        print("\u001b[31m-"+str(sadness)+" hapiness\033[0m")
        economy_status = random.randint(0,1)
        economy_rate = random.random()
        if economy_status == 0:
            print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"%"+"\033[0m")
        if economy_status == 1:
            print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"%"+"\033[0m")
        print("STATUS:\nThe citizens of "+name+" "+str(riotmood[random.randint(0, len(riotmood)-1)]))
    if choice == 4 and population <= 5:
        print("\033[0;31m\nNot enough population to start riots\033[0m")
    if choice == 5:
        passive_or_mean = random.randint(0,10)
        if passive_or_mean != 5:
            unbeliefalien = random.randint(55,100)
            map = map.replace("[@]","\033[0;32m0-0\033[0m")
            map = map.replace("#", "\033[0;33m#\033[0m")
            print(map)
            deathcount = random.randint(0,population)
            sadness = random.randint(0,35)
            population = population-deathcount
            belief = belief - unbeliefalien
            happiness = happiness - sadness
            print("STATS:")
            print("---------------")
            print("NAME: "+name)
            print("POPULATION: "+str(population))
            print("\u001b[31m-"+str(deathcount)+" people died as a result of the aliens\033[0m")
            print("YEAR: "+str(year+random.randint(1,10)))
            print("BELIEF IN YOU: "+str(belief)+"%")
            print("\u001b[31m-"+str(unbeliefalien)+r"% belief"+"\033[0m")
            print("HAPINESS: "+str(happiness))
            print("\u001b[31m-"+str(sadness)+" hapiness\033[0m")
            economy_status = random.randint(0,1)
            economy_rate = random.random()
            if economy_status == 0:
                print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"%"+"\033[0m")
            if economy_status == 1:
                print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"%"+"\033[0m")
            print("STATUS:\nThe citizens of "+name+" "+str(alienmood[random.randint(0, len(alienmood)-1)]))
        if passive_or_mean == 5:
            unbeliefalien_passive = random.randint(0,40)
            belief = unbeliefalien_passive + belief
            increase_passive = random.randint(5,40)
            happiness = happiness + increase_passive
            map = map.replace("[@]","[@]\033[0;32m0-0\033[0m")
            print(map)
            deathcount = 0
            print("STATS:")
            print("---------------")
            print("NAME: "+name)
            print("POPULATION: "+str(population))
            print("\033[0;32mNo one died, the aliens were passive!")
            print("YEAR: "+str(year+random.randint(1,10)))
            print("BELIEF IN YOU: "+str(belief)+"%")
            print("\033[0;32m+"+str(unbeliefalien_passive)+r"% belief"+"\033[0m")
            print("HAPINESS: "+str(happiness))
            print("\033[0;32m+"+str(increase_passive)+" hapiness\033[0m")
            economy_status = random.randint(0,1)
            economy_rate = random.random()
            if economy_status == 0:
                print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"%"+"\033[0m")
            if economy_status == 1:
                print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"%"+"\033[0m")
            print("STATUS:\nThe citizens of "+name+" "+str(passive_alienmood[random.randint(0, len(passive_alienmood)-1)]))
    if choice == 6:
        unbeliefalien = random.randint(70,100)
        map = map.replace("[@]","]?[")
        map = map.replace("#", "+")
        map = map.replace("~", " ")
        print(map)
        deathcount = random.randint(0,population)
        sadness = random.randint(60,100)
        population = population-deathcount
        belief = belief - unbeliefalien
        happiness = happiness - sadness
        print("STATS:")
        print("---------------")
        print("NAME: "+name)
        print("POPULATION: "+str(population))
        print("\u001b[31m-"+str(deathcount)+" people died as a result of the flip\033[0m")
        print("YEAR: "+str(year+random.randint(1,10)))
        print("BELIEF IN YOU: "+str(belief)+"%")
        print("\u001b[31m-"+str(unbeliefalien)+r"% belief"+"\033[0m")
        print("HAPINESS: "+str(happiness))
        print("\u001b[31m-"+str(sadness)+" hapiness\033[0m")
        economy_status = random.randint(0,1)
        economy_rate = random.random()
        if economy_status == 0:
            print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"%"+"\033[0m")
        if economy_status == 1:
            print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"%"+"\033[0m")
        print("STATUS:\nThe citizens of "+name+" "+str(gravmood[random.randint(0, len(gravmood)-1)]))
    if choice == 7:
        unbeliefplague = random.randint(0,45)
        print(map)
        deathcount = random.randint(0,population)
        population = population-deathcount
        sadness = random.randint(0,23)
        happiness = happiness - sadness
        belief = belief - unbeliefplague
        print("STATS:")
        print("---------------")
        print("NAME: "+name)
        print("POPULATION: "+str(population))
        print("\u001b[31m-"+str(deathcount)+" people died as a result of the this mass panic\033[0m")
        print("YEAR: "+str(year+random.randint(1,10)))
        print("BELIEF IN YOU: "+str(belief)+"%")
        print("\u001b[31m-"+str(unbeliefplague)+r"% belief"+"\033[0m")
        print("HAPINESS: "+str(happiness))
        print("\u001b[31m-"+str(sadness)+" hapiness\033[0m")
        economy_status = random.randint(0,1)
        economy_rate = random.random()
        if economy_status == 0:
            print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"%"+"\033[0m")
        if economy_status == 1:
            print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"%"+"\033[0m")
        print("STATUS:\nAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    if choice == 8:
        beliefadd = random.randint(0,45)
        print(map)
        sadness = random.randint(0,23)
        happiness = happiness + sadness
        belief = belief + beliefadd
        print("STATS:")
        print("---------------")
        print("NAME: "+name)
        print("POPULATION: "+str(population))
        print("YEAR: "+str(year+random.randint(1,10)))
        print("BELIEF IN YOU: "+str(belief)+"%")
        print("\033[0;32m+"+str(unbeliefplague)+r"% belief"+"\033[0m")
        print("HAPINESS: "+str(happiness))
        print("\033[0;32m+"+str(sadness)+" hapiness\033[0m")
        economy_status = random.randint(0,1)
        economy_rate = random.random()
        print("ECONOMY: "+str(economy)+"\033[0;32m/\\ "+str(economy_rate)+"%"+"\033[0m")
        print("STATUS:\nThe citizens of "+name+" "+str(goodharvestmood[random.randint(0, len(goodharvestmood)-1)]))
    if choice == 9:
        unbeliefplague = random.randint(0,45)
        print(map)
        deathcount = random.randint(0,population)
        population = population-deathcount
        sadness = random.randint(0,23)
        happiness = happiness - sadness
        belief = belief - unbeliefplague
        print("STATS:")
        print("---------------")
        print("NAME: "+name)
        print("POPULATION: "+str(population))
        print("\u001b[31m-"+str(deathcount)+" people died as a result of the this economic downturn\033[0m")
        print("YEAR: "+str(year+random.randint(1,10)))
        print("BELIEF IN YOU: "+str(belief)+"%")
        print("\u001b[31m-"+str(unbeliefplague)+r"% belief"+"\033[0m")
        print("HAPINESS: "+str(happiness))
        print("\u001b[31m-"+str(sadness)+" hapiness\033[0m")
        economy_status = random.randint(0,1)
        economy_rate = random.random()
        print("ECONOMY: "+str(economy)+"\033[0;31m\\/ "+str(economy_rate)+"%"+"\033[0m")
        print("STATUS:\nThe citizens of "+name+" "+str(economicdownturnmood[random.randint(0, len(economicdownturnmood)-1)]))
    
    if choice != "break" and choice not in digit:
        print("ERROR, NOT A VALID CHOICE, TRY AGAIN")
    if choice == "break":
        exit()
        quit()

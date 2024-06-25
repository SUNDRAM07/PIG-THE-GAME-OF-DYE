import random

def play_game():
    while True:
        play_game=input("Do you want to play the game of PIG. roll the dice?(Y or N) ").lower()[0]
        if play_game=="y":
            print("Welcome to PIG the game of dice....")
            main()
        elif play_game=="n":
            quit()
        else:
            print("invalid input man")
            continue
            

def dice_roll():
    global randoms
    randoms=random.randrange(1,6)
    return randoms


def main():
    sum=0
    rounds=0
    while sum <= 50:
        hell=input("Press enter or quit by pressing q..").lower()
        if hell=="":
            dice_roll()
            if randoms == 1:
                print(randoms)
                print("fuck man The dice rolled: " + str(randoms) )
                print("Total sum = 0")
                sum = 0
                rounds+=1
            else:
                print("The dice rolled: " + str(randoms) )
                sum += randoms
                print ( "Total sum = " + str(sum))
                rounds+=1
                if sum == 50:
                    break
        elif hell=="q":
            play_game()
    print("YOU WON IN: " + str(rounds)+"rounds man!!! With a final score of : "+str(sum))
    play_game()
    


play_game()


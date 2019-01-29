def dice_roll(dice, choosen):
    if dice == 0:
        print(choosen)
    else:
        for i in range(1, 7):
            choosen.append(i)
            dice_roll(dice-1, choosen)
            choosen.pop()

if __name__ == "__main__":

    dice_roll(6, [])
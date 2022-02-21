from termcolor import *


def main():
    cn = colored("cn", 'blue', attrs=['reverse', 'blink'])
    rp = colored("rp", 'yellow', attrs=['reverse', 'blink'])

    cprint("Hello! what would you like to do?",'cyan')
    cprint("Create New List: " + cn, 'blue')
    cprint("Read previous List: " + rp, 'yellow')
    usr_input = input()
    item_list = []
    if usr_input.lower() == "cn":
        with open("itemList.txt", 'w'):
            pass
        listAmount = input("How many items do you have?")
        listAmount = int(listAmount)
        listCounter = 0
        while listCounter < listAmount:
            list_inp = input()
            item_list.insert(0, list_inp)
            listCounter += 1

        with open("itemList.txt", 'a', encoding="utf-8") as listFile:
            for items in range(len(item_list)):
                count = len(item_list) - 1
                count -= items
                listFile.write(item_list[count]+"\n")
                items += 1

    elif usr_input.lower() == "rp":
        with open("itemList.txt", "r") as lists:
            itemsInList = lists.readlines()
            newlist = [x[:-1] for x in itemsInList]
            for i in newlist:
                cprint(i, 'cyan')

    else:
        cprint("something went wrong", 'red')


if __name__ == "__main__":
    main()

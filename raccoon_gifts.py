import numpy as np
import random
import string

def randomTest(numGroups, nameLength):
    """
    The function is used to test the Raccoon_Gifts function against random size of family
    Family size is determined by the number of groups
    The function will generate a random family structre based on a given number of groups
    Each group represents a signle person or a couple
    For example: ['Alex'] is a group, and ['sam', 'jan'] is a couple and also a group
    So ON AVERAGE the number of family members will be numGroups + numGroups/2

    @param numGroups: number of groups to create the random family with
    @param namelength: length of the randmo names that will be assigned to the members

    @return fam: a list of a family. The structre of the family will be as follows:
    couples are put together in a list of size 2, and each signle person is put in a list of size 1

    @return mems: a list of a family members
    """
    if (nameLength <= 0 or numGroups <= 0):
        print("ERROR: please enter a number larger than 0")
        return 0, 0

    if (nameLength > 10):
        print("ERROR: maximum allowed random name length is 10")
        return 0, 0

    if (numGroups > np.power(26, 10)):
        print("ERROR: maximum allowed number of groups is 26^10")
        return 0, 0

    if (numGroups > np.power(26, nameLength)):
        print("ERROR: numGroups has to be less than 26^nameLength")
        return 0, 0

    # list to hold family members, singles and couples
    fam = []

     # set to hold names of all family members to esnure no duplicate names are created
    mems = set()


    for i in range(numGroups):
        # random choice of wether to add a single person or a couple. 0 for couple, 1 for single
        # On average half of the list will be couples and half will be singles
        # So total members should be around N + N/2
        x = np.random.randint(2)

        # generate two randmo names of length
        # a 4 character name has 26^4 possible permutations (more than 450k)
        firstMember = "".join(random.choices(string.ascii_lowercase, k=nameLength))
        secondMember = "".join(random.choices(string.ascii_lowercase, k=nameLength))

        # to prevent dublicate names
        valid = [firstMember not in mems and secondMember not in mems]

        # Add a couple to the family if the random result was 0 and no duplicates, otherwise add a signle person
        if (x == 0 and valid):
            mems.add(firstMember)
            mems.add(secondMember)
            fam.append([firstMember, secondMember])
        elif (x == 1 and valid):
            mems.add(firstMember)
            fam.append([firstMember])

    return fam, list(mems)


def create_family(couples, singles):
    """
    Create a family list given a specific number of couples and singlesself.
    The structer of the family is the same as described in the previous function

    @param couples: number of couples
    @param couples: number of singles

    @return fam: a list of a family. The structre of the family will be as follows:
    couples are put together in a list of size 2, and each signle person is put in a list of size 1

    @return mems: a list of a family members
    """

    #maximum size of family
    if (couples * 2 + singles > np.power(26, 4)):
        return "The size of the family has to be less than 26^4"

    # list to hold family members, singles and couples
    fam = []

    # set to hold names of all family members to esnure no duplicate names are created
    mems = set()

    #generate random names for the couples and add them to the
    #family list and members list
    for i in range(couples):
        firstMember = "".join(random.choices(string.ascii_lowercase, k=4))
        secondMember = "".join(random.choices(string.ascii_lowercase, k=4))
        valid = [firstMember not in mems and secondMember not in mems]
        if valid:
            mems.add(firstMember)
            mems.add(secondMember)
            fam.append([firstMember, secondMember])

    #generate random names for the singles and add them to the
    #family list and members list
    for i in range(singles):
        firstMember = "".join(random.choices(string.ascii_lowercase, k=4))
        valid = [firstMember not in mems]
        if valid:
            mems.add(firstMember)
            fam.append([firstMember])

    return fam, list(mems)


def pairs(family, members):
    """
    Function to find to who each member will give their gift.


    @param family: family structre . The structre of the family has to be as follows:
    couples are put together in a list of size 2, and each signle person is put in a list of size 1

    @para members: unique list of all family members (strings)

    @return pairs: a list of pairs in which the first member gives their gift to the second
    """

    # create dictionary of forbidden gifters (gift to oneself and gift to spouse)
    no = {}
    # 2n
    for m in members:
        #return the list which the member belongs to
        ind = [i for i, s in enumerate(family) if (str(m) in s)]
        no[m] = family[ind[0]]
        

    counter = len(members)
    loops = 0
    while (counter > 0):
        loops += 1
        noIllegal = True
        pairs = []

        givers, takers = members.copy(), members.copy()
        np.random.shuffle(givers)
        np.random.shuffle(takers)

        while (noIllegal and counter > 0):

            giver = givers.pop()
            taker = takers.pop()
            if (taker in no.get(giver)):
                noIllegal = False
            else:
                pairs.append([giver, taker])
            counter -= 1

        if (noIllegal):
            break
        else:
            # reset counter and restart the process
            counter = len(members)
    print('The program was restarted', loops, 'times until it found valid pairs')
    return pairs

def readIntInput(message):
    """
    Function that reads ONLY integer from the command line.


    @parameter message: the prompt to be displayed to the user

    @return num: the number that the user input
    """
    num = (input(message))
    if num.isdigit():
        return int(num)
    else:
        print('you ented an invalid option')
        readIntInput(message)



def raccoon_gifts():
    """
    Function that interacts with the user

    """
    print("Welcome to Raccoon Dinner. The easy way to find exchange pairs\n"
          "You can run random test of the program by inputing 0\n"
          "Or you can run the program for your family dinner by inputing 1\n")

    random_custom = readIntInput(
        'Input 0 to run program against random input, or 1 against customized input (Mr.Raccoon choose customized): ')

    if random_custom == 0:
        print("the random tests works by taking two parameters:\n"
              "First para: number of family groups. A signle person is a group, and a couple is a group\n"
              "Second para: length of each random name (so that we can assign names to family members) MAX=10\n"
              "The function then will generate a random number of couples and singles and give them random names\n"
              "Then it will find which pairs will exchange gifts")
        familyNum = readIntInput('Enter number of family groups: ')
        nameLength = readIntInput('Enter length of random name, NOTE: groups must be < 26^nameLength: ')
        f, m = randomTest(familyNum, nameLength)
        if (f == 0 or m == 0 or familyNum == 0 or nameLength == 0):
            print("program will terminate due to incorrect input")
            return "Program will terminate due to incorrect input."

        print("The program generated this random family which has", familyNum, "Groups with", len(m),
              " members in total\n", f)
        print("FINDING PAIRS...")
        p = pairs(f, m)
        print('The program suggest the following pairs, where the first member gives to the second', p)
    elif random_custom == 1:
        print("Custem input takes two parameters:\n"
              "Number of couples and number of singles\n"
              "The program will then generate random names for the family members\n"
              "Mr.Raccoon please assign those random names to your family members\n"
              "The program will give you a list of pairs (with the random names) so make sure to know who you assigned the names to")
        couples = readIntInput('How couples are there? ')
        singles = readIntInput('How many singles are there? ')
        s, n = create_family(couples, singles)
        print('The program generated those random names (couples are placed together)', s)
        print("Finding pairs...")
        p = pairs(s, n)
        print('The program suggest the following pairs, where the first member gives to the second', p)
    else:
        print('you must enter either 1 or 0')

    return "Thanks for using Raccoon Gifts"


raccoon_gifts()

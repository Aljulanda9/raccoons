# Project Title

A python program to be used by raccoons in their gift exchange dinner

## Getting Started

Clone the project:
```
git clone https://github.com/Aljulanda9/raccoons.git
```

## Prerequisites

Python3 

## Launching instructions

To launch the program, navigate to where the repository was cloned then:

```
python3 raccoons_gifts.py
```

The program will ask you if you want to run the program for a "random test" or "customized input". Choose customized input. Testing will be discussed later.

To simplify the interaction in the terminal: the user will not enter the names of the participants. 

Rather the user will tell the program how many singles and couples there are. 

The program will then generate random names for those signles and couples and displays them on the screen. 

The host of the dinner is responsiple of assigning those random names to the actual participants, because the program will return a list of pairs to give the gifts in terms of their random names.

The list of pairs that will be returned as the following structre:

For each pair in the returned list:
- first person gives their gift to the second person.

Ex: ['mas', ''kas'] mas will give a gift to kas

## Testing

For ease of use, the tests are bundeled with the program in one interface:

Start by launcing tha app:

```
python3 raccoons_gifts.py
```

The program will ask you if you want to do "random tests", choose it.

This test will ask you to input a "number of groups". This number will be used to create the 
random family structre.
The function will generate a random family structre based on a given number of groups
Each group represents a signle person or a couple.
For example: ['alex'] is a group, and ['sam', 'jan'] is a couple and also a group

So ON AVERAGE the number of family members will be numGroups + numGroups/2


The program will also ask you to choose the length for the random names that will be generated 
for the family members

## Example tests

Number of Groups = 1000

Name Length = 4

This test will generate around 1500 pairs of members to give gifts. Each member will have a name of length 4

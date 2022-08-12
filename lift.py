import random
time = 0
door_time = 0
environment = []
temp_env = []
people = []
chain = []
class rand_environment():
    """Class for creating a random set of people and requests"""
    def __init__(self, no_floors, no_people):
        self.no_floors = no_floors
        self.no_people = no_people
    def generate(self):
        """method for generating a random environment by appending to the environment lists"""
        for i in range (self.no_people):
            x = [random.randrange(1, self.no_floors), random.randrange(1, self.no_floors)]
            if x[0] == x[1]:
                x.pop(1)
                if x[0] == self.no_floors:
                    x.append(x[0]-1)
                else:
                    x.append(x[0]+1)
            people.append(x)
        for i in range (self.no_floors):
            environment.append([])
        chain = people
        for i in people:
            x = environment.pop(i[0])
            x.append(i[1])
            environment.insert(i[0],x)
        global temp_env
        temp_env = environment


class lift():
    """Class for the lift"""
    def __init__(self, current_floor, occupants):
        self.current_floor = current_floor
        self.occupants = occupants
    def move_lift(self, next_floor):
        self.next_floor = next_floor
        #global time
        global time
        time = time + abs(self.current_floor - next_floor) + door_time
        #maybe change to total wait time rather than/and time to completion
        self.current_floor = self.next_floor
        while len(environment[self.current_floor]) != 0:
            for i in environment[self.current_floor]:
                self.occupants.append(i)
                environment[self.current_floor].remove(i)
        while self.current_floor in self.occupants:
            self.occupants.remove(self.current_floor)
            #SOMETHING TO SAY THEY'VE BEEN DELIVERED
    def move_lift_mech(self, next_floor, going_up):
        self.next_floor = next_floor
        self.going_up = going_up
        global time
        time = time + abs(self.current_floor - next_floor) + door_time
        #maybe change to total wait time rather than/and time to completion
        self.current_floor = self.next_floor
        if len(environment[self.current_floor]) != 0:
            for i in environment[self.current_floor]:
                if self.going_up == True:
                    if i > self.current_floor:
                        self.occupants.append(i)
                        environment[self.current_floor].remove(i)
                if self.going_up == False:
                    if i < self.current_floor:
                        self.occupants.append(i)
                        environment[self.current_floor].remove(i)
        while self.current_floor in self.occupants:
            self.occupants.remove(self.current_floor)
            #SOMETHING TO SAY THEY'VE BEEN DELIVERED

def completion():
    x = 0
    global ppl_left
    for i in environment:
        x = x + len(i)
    ppl_left = len(lft.occupants) + x

def mechanical():
    going_up = True
    def go_up():
        global ppl_left
        while ppl_left > 0:
            for i in range (env.no_floors):
                lft.move_lift_mech(i,True)
            global going_up
            going_up = False
            completion()
            go_down()
    def go_down():
        global ppl_left
        while ppl_left > 0:
            for i in range (env.no_floors)[::-1]:
                lft.move_lift_mech(i,False)
            global going_up
            going_up = True
            completion()
            go_up()
    completion()
    go_up()

def execute(path):
    for i in path:
        lft.move_lift(i)
    print ("environment = ", environment )
    print ("path: ", path, "used" )
    print ("Time taken = ", time)


def my_method():
    branch_list  = []
    branch = []
    """go to the first list that contains an element"""
    for i in temp_env:
        if temp_env(i):

            #pathinder(i)
            if len (temp_env) == 1:
                branch.append(i[0])
            else:
                for x in temp_env(i):
                    branch.append(i[0])

tmp_occ = []
def pathfinder(x, tmp_occ):
    if len (x) == 1:
        tmp_occ.remove(x)
        branch.append(x)
        pathfinder(x, tmp_occ)
    while len(x) == 0:
        break
    else:
        for i in x:
            tmp_occ.append(i)
        branch.append(tmp_occ)
        for i in tmp_occ:
            pathfinder(i)
tmp = []


def pathfinder(tmp_occ):
    i = 0
    n = len(tmp_occ)
    while i < n:
        element = tmp_occ[i]
        p = add_people(element)
        tmp_occ.append(p)
        tmp_occ.remove(element)
        pathfinder(element)
    if check(element):
        n = n - 1
    else:
        i = i + 1

def add_people(x):
    y = temp_env[x]
    temp_env[x] = []
    return y

branch = []
def pathfinder(tmp_occ):
    for i in tmp_occ:
        tmp_occ.remove(i)
        x = add_people(i)
        tmp_occ.append(x)
        branch.append(i)
        branch.append(pathfinder(tmp_occ))


[1,2,3]
[1,[2,[3],3,[2]],2,[1,[3],3,[1]],3,[1,[2],2,[1]]]
#go to the first level with people on
#if there is 1, go to that number and continue
#if there is multiple: go through every option recursively
#
#function that takes a list as input and for each element in that list remove it, add the other people to the list and then input that list into itself
#
#
#
#
#
#
#[ [3,2] , [3,1] , [2,1] ]
#is there multiple people there?
#if no: append element to branch and move on
#if yes: look at all the
#go to the element in environment with index = last branch number






a = [1,[2,[3,4],5,[6,7]]]
branches = []
temp = []
def make_list(list):
    global a
    global temp
    global branches
    if len(a) != 0:
        if len(list) > 1 and type(list[1]) != int:
            if list[1] == []:
                list.pop(1)
                list.pop(0)
            if list != []:
                temp.append(list[0])
                make_list(list[1])
        if len(list) == 0:
            make_list(a)
        else:
            x = list.pop(0)
            temp.append(x)
            temp = [str(x) for x in temp]
            temp = "".join(temp)
            temp = int(temp)
            branches.append(temp)
            temp = []
            make_list(a)

#go though the elements of a list
#if there are any elements that are empty lists: delete the empty list and delete the element with index before the empty list
#
#
##
#
#i#f there are and numbers that have an empty bracket next to them, delete both the number and the empty bracket

#if there is a list as the element after
#
#
#
#
#
#
#
#if the second item of the list is an integer, then its the end of the branch
#add the first element on until the second element is an integer, then remove the first one and repeat
#
#go up to the first floor with people on it
#if there is 1 person there, pick them up and go to the floor that they want to go to
#if there are more than 1 person there, create a branch
#create a branch by copying the previous moves and inserting it as a list into the list of the same tree
#after creating a branch, continue with algorithm using the highest choice
#after completion of branch, insert it into the list of completed paths
#go back to last step before branch and use the second highest choice

#given a matrix, move every number in the matrix to the row of the same value
#sort the doubles so that the last element of the list is equal to the first of the next one

env = rand_environment(10,10)
rand_environment.generate(env)
lft = lift(0,[])
environment
lift.move_lift(lft,2)
#general algorithm is: Are you at the top/bottom floor? if yes: go in the other direction
#go up to the next floor. Is there someone there? If so, do they want to go in the same direction as the lift is currently going in?
#if yes: put them in the lift. keep going up/down and asking the previous questions.

#while going up: for each list in enviro: if the the number is greater than its index in enviro, then pick up the person

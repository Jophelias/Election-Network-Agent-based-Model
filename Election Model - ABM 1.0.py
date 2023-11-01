#For the state of Vermont

import networkx as nx
import random
#from _snap import *

#Used https://suburbanstats.org/population/how-many-people-live-in-vermont for all the demographic stats

A = nx.erdos_renyi_graph(0,0,directed=False)
#B = _snap.TNGraph.New()
#B = _snap.GenRndGnm(_snap.PNGraph, 625741,0)

white_male =int(293649)
white_female=int(302643)
multi_male=int(5244)
multi_female=int(5509)
hispanic_male=int(4626)
hispanic_female=int(4582)
asian_male=int(3481)
asian_female=int(4466)
black_male=int(3517)
black_female=int(2760)
other_male=int(1131+1103+287+81)
other_female=int(2207+2105+610+160)

n=0

print("Assigning Races")

while n < white_male:
    A.add_node(n, Race = 'White' , Gender = 'Male')
    n+=1
    #if n%1000:
        #print n
#print "White male done"

while n < white_female + white_male:
    A.add_node(n, Race = 'White', Gender = 'Female')
    n+=1
    #if n%1000:
        #print n
#print "white female done"

while n < multi_male + white_female + white_male:
    A.add_node(n, Race = 'Multi', Gender = 'Male')
    n+=1
    #if n%1000:
        #print n
#print "multi male done"

while n < multi_female + multi_male + white_male + white_female:
    A.add_node(n, Race = 'Multi', Gender = 'Female')
    n+=1
    #if n%1000:
        #print n

#print "multi female done"

while n < hispanic_male + multi_female + multi_male + white_male + white_female:
    A.add_node(n, Race = 'Hispanic', Gender = 'Male')
    n+=1
    #if n%1000:
        #print n

#print "hispanic male done"
while n < hispanic_female + hispanic_male + multi_female + multi_male + white_male + white_female:
    A.add_node(n, Race = 'Hispanic', Gender = 'Female')
    n+=1
    #if n%1000:
        #print n

#print "hispanic female done"
while n < asian_male + hispanic_female + hispanic_male + multi_female + multi_male + white_male + white_female:
    A.add_node(n, Race = 'Asian', Gender = 'Male')
    n+=1
    #if n%1000:
        #print n

#print "asian male done"

while n < asian_female + asian_male + hispanic_female + hispanic_male + multi_female + multi_male + white_male + white_female:
    A.add_node(n, Race = 'Asian', Gender = 'Female')
    n+=1
    #if n%1000:
        #print n

#print "asian female done"
while n < black_male + asian_female + asian_male + hispanic_female + hispanic_male + multi_female + multi_male + white_male + white_female:
    A.add_node(n, Race = 'Black', Gender = 'Male')
    n+=1
    #if n%1000:
        #print n

#print "black male done"
while n < black_female + black_male + asian_female + asian_male + hispanic_female + hispanic_male + multi_female + multi_male + white_male + white_female:
    A.add_node(n, Race = 'Black', Gender = 'Female')
    n+=1
    #if n%1000:
        #print n

#print "black female done"
while n < other_male + black_female + black_male + asian_female + asian_male + hispanic_female + hispanic_male + multi_female + multi_male + white_male + white_female:
    A.add_node(n, Race = 'Other', Gender = 'Male')
    n+=1
    #if n%1000:
        #print n

#print "other male done"
while n < other_female + other_male + black_female + black_male + asian_female + asian_male + hispanic_female + hispanic_male + multi_female + multi_male + white_male + white_female:
    A.add_node(n, Race = 'Other', Gender = 'Female')
    n+=1
    #if n%1000:
        #print n

#print "other female done"

# Now to set age groups

male_under18 = int(66010)
male_1829 = int(41640)
male_3049 = int(78723)
male_5064 = int(69608)
male_over65 = int(39188)

female_under18 = int(62634)
female_1829 = int(40637)
female_3049 = int(82213)
female_5064 = int(71850)
female_over65 = int(48089)

age_group = ["under 18", "18-29", "30-49", "50-64", "65+"]

B = A.nodes()
"""print (len(B.nodes()))
random_node = random.choice(B.nodes())
print("I picked", random_node)
B.remove_node(random_node)
print(len(B.nodes()))"""

print("Now to assigning Demographics")

count =0
while len(B) > 0:
    random_node = random.choice(B)
    count +=1
    #if count == 50000 or count == 100000 or count == 300000 or count == 600000 :
    #print ("The count is", count, "and B is this long", len(B), "And A is", len(A.nodes()))

    if A.node[random_node]['Gender'] == "Male" and male_under18 > 0 :
        A.node[random_node]['Age'] = "Under 18"
        male_under18 -=1
        B.remove(random_node)
        continue
    elif A.node[random_node]['Gender'] == "Male" and male_1829 > 0:
        A.node[random_node]['Age'] = "18-29"
        B.remove(random_node)
        male_1829 -= 1
        continue
    elif A.node[random_node]['Gender'] == "Male" and male_3049 > 0 :
        A.node[random_node]['Age'] = "30-49"
        B.remove(random_node)
        male_3049 -=1
        continue
    elif A.node[random_node]['Gender'] == "Male" and male_5064 > 0:
        A.node[random_node]['Age'] = "50-64"
        B.remove(random_node)
        male_5064 -= 1
        continue
    elif A.node[random_node]['Gender'] == "Male" and male_over65 > 0:
        A.node[random_node]['Age'] = "65+"
        B.remove(random_node)
        male_over65 -= 1
        continue

    #For Females

    elif A.node[random_node]['Gender'] == "Female" and female_under18 > 0 :
        A.node[random_node]['Age'] = "Under 18"
        B.remove(random_node)
        female_under18 -=1
        continue
    elif A.node[random_node]['Gender'] == "Female" and female_1829 > 0:
        A.node[random_node]['Age'] = "18-29"
        B.remove(random_node)
        female_1829 -= 1
        continue
    elif A.node[random_node]['Gender'] == "Female" and female_3049 > 0 :
        A.node[random_node]['Age'] = "30-49"
        B.remove(random_node)
        female_3049 -=1
        continue
    elif A.node[random_node]['Gender'] == "Female" and female_5064 > 0:
        A.node[random_node]['Age'] = "50-64"
        B.remove(random_node)
        female_5064 -= 1
        continue
    elif A.node[random_node]['Gender'] == "Female" and female_over65 > 0:
        A.node[random_node]['Age'] = "65+"
        B.remove(random_node)
        female_over65 -= 1
        continue
    else:
        random_age_choice = random.choice(age_group)
        A.node[random_node]['Age'] = random_age_choice
        B.remove(random_node)

#Now to generate the social network


nx.set_node_attributes(A, 'Connected', 0)
nx.set_node_attributes(A, 'Household Type', 'Default')

C = A.nodes()

singles = int(63112/10)
families_of_two = int(19759/10)
families_w_underage_children = int(76409/10)
families_w_children = int(81354/10)

print("Now to connecting the network, starting with singles and families with no children")

young_adult_male_nodes = []
young_adult_female_nodes =[]

for nodes in A.nodes():
    if A.node[nodes]['Age'] != 'Under 18' and A.node[nodes]['Gender'] == 'Male':
        young_adult_male_nodes.append(nodes)
    elif A.node[nodes]['Age'] != 'Under 18' and A.node[nodes]['Gender'] == 'Female':
        young_adult_female_nodes.append(nodes)


while singles > 0 or families_of_two > 0 :

    """print("This is how many young men there are", len(young_adult_male_nodes))
    print("This is how many young women there are", len(young_adult_female_nodes))
    print("single families", singles)
    print("families of two", families_of_two)"""

    random_male_node = random.choice(young_adult_male_nodes)
    another_female_node = random.choice(young_adult_female_nodes)

    #create couples w/ no kids - since nodes under the age of 18 can't be married, we have to filter for them

    A.add_edge(random_male_node, another_female_node)
    A.node[random_male_node]['Connected'] = 1
    A.node[another_female_node]['Connected'] = 1
    A.node[random_male_node]['Household Type'] = 'Couple'
    A.node[another_female_node]['Household Type'] = 'Couple'
    young_adult_male_nodes.remove(random_male_node)
    young_adult_female_nodes.remove(another_female_node)
    families_of_two -= 2

    random_male_node = random.choice(young_adult_male_nodes)
    another_female_node = random.choice(young_adult_female_nodes)

    A.node[random_male_node]['Household Type'] = 'Single'
    A.node[another_female_node]['Household Type'] = 'Single'
    A.node[random_male_node]['Connected'] = 1
    A.node[another_female_node]['Connected'] = 1
    young_adult_male_nodes.remove(random_male_node)
    young_adult_female_nodes.remove(another_female_node)
    singles -= 2

"""while families_w_underage_children !=0 or families_w_children != 0:
    random_one = random.choice(C)
    random_two = random.choice(C)
    random_three = random.choice(C)
    random_four = random.choice(C)"""

underage_nodes = []
young_adult_male_nodes = []
old_adult_male_nodes =[]
young_adult_female_nodes = []
old_adult_female_nodes =[]

print("Indexing, with families with children")

for nodes in A.nodes():
    if A.node[nodes]['Age'] == 'Under 18' and A.node[nodes]['Connected'] != 1:
        underage_nodes.append(nodes)
    elif (A.node[nodes]['Age'] == '18-29' or A.node[nodes]['Age'] == '30-49' ) and A.node[nodes]['Gender'] == 'Male' and A.node[nodes]['Connected'] != 1:
        young_adult_male_nodes.append(nodes)
    elif (A.node[nodes]['Age'] == '50-64' or A.node[nodes]['Age'] == '65+') and A.node[nodes]['Gender'] == 'Male' and A.node[nodes]['Connected'] != 1:
        old_adult_male_nodes.append(nodes)
    elif (A.node[nodes]['Age'] == '18-29' or A.node[nodes]['Age'] == '30-49' ) and A.node[nodes]['Gender'] == 'Female' and A.node[nodes]['Connected'] != 1:
        young_adult_female_nodes.append(nodes)
    elif (A.node[nodes]['Age'] == '50-64' or A.node[nodes]['Age'] == '65+') and A.node[nodes]['Gender'] == 'Female' and A.node[nodes]['Connected'] != 1:
        old_adult_female_nodes.append(nodes)

#young_adult_nodes = young_adult_male_nodes + young_adult_female_nodes
#families_w_underage_children = 76409
#families_w_children = 81354

"""male_under18 = 66010
male_1829 = 41640
male_3049 = 78723
male_5064 = 69608
male_over65 = 39188

female_under18 = 62634
female_1829 = 40637
female_3049 = 82213
female_5064 = 71850
female_over65 = 48089"""

#families_w_underage_children = 76409
#families_w_children = 81354

print("Now to connecting the network, with families with children")

while len(underage_nodes) > 3:
    # Triad young parents with underage children

    random_young_adult_male = random.choice(young_adult_male_nodes)
    random_young_adult_female = random.choice(young_adult_female_nodes)
    random_child = random.choice(underage_nodes)
    A.add_edges_from([(random_young_adult_female,random_young_adult_male),(random_young_adult_male,random_child),(random_child,random_young_adult_female)])

    A.node[random_young_adult_female]['Household Type'] = 'Family'
    A.node[random_young_adult_male]['Household Type'] = 'Family'
    A.node[random_child]['Household Type'] = 'Family'
    A.node[random_young_adult_female]['Connected'] = 1
    A.node[random_young_adult_male]['Connected'] = 1
    A.node[random_child]['Connected'] = 1

    young_adult_female_nodes.remove(random_young_adult_female)
    young_adult_male_nodes.remove(random_young_adult_male)
    underage_nodes.remove(random_child)

    #Clique young parents with 2 under age children

    #print("This is how many kids are left", len(underage_nodes))

    random_young_adult_male = random.choice(young_adult_male_nodes)
    random_young_adult_female = random.choice(young_adult_female_nodes)
    random_child = random.choice(underage_nodes)
    random_child_two = random.choice(underage_nodes)
    if random_child == random_child_two:
        random_child_two = random.choice(underage_nodes)
    A.add_edges_from([(random_young_adult_female,random_young_adult_male),(random_young_adult_male,random_child),(random_child,random_young_adult_female)])
    A.add_edges_from([(random_young_adult_female, random_child_two), (random_young_adult_male, random_child_two),(random_child, random_child_two)])
    
    A.node[random_young_adult_female]['Household Type'] = 'Family'
    A.node[random_young_adult_male]['Household Type'] = 'Family'
    A.node[random_child]['Household Type'] = 'Family'
    A.node[random_child_two]['Household Type'] = 'Family'
    A.node[random_young_adult_female]['Connected'] = 1
    A.node[random_young_adult_male]['Connected'] = 1
    A.node[random_child]['Connected'] = 1
    A.node[random_child_two]['Connected'] = 1

    young_adult_female_nodes.remove(random_young_adult_female)
    young_adult_male_nodes.remove(random_young_adult_male)
    underage_nodes.remove(random_child)
    underage_nodes.remove((random_child_two))

print("Now to connecting the network, starting with singles and families with older children")

young_adults = young_adult_male_nodes + young_adult_female_nodes

while len(young_adults) > 3 and len(old_adult_female_nodes) > 3 and len(old_adult_male_nodes) > 3:
    #Triad old parents and middle age children
    
    random_old_adult_male = random.choice(old_adult_male_nodes)
    random_old_adult_female = random.choice(old_adult_female_nodes)

    random_adult_child = random.choice(young_adults)

    A.add_edges_from([(random_old_adult_female,random_old_adult_male),(random_old_adult_male,random_adult_child),(random_adult_child,random_old_adult_female)])

    old_adult_female_nodes.remove(random_old_adult_female)
    old_adult_male_nodes.remove(random_old_adult_male)

    young_adults.remove(random_adult_child)

    #Clique old parents and 2 middle aged children

    random_old_adult_male = random.choice(old_adult_male_nodes)
    random_old_adult_female = random.choice(old_adult_female_nodes)

    #dice_roll = random.uniform(0,1)
    #dice_roll_two = random.uniform(0, 1)

    #Picking adult child #1

    random_adult_child = random.choice(young_adults)

    #Picking Adult child #2

    random_adult_child_two = random.choice(young_adults)

    if random_adult_child_two == random_adult_child:
        random_adult_child_two = random.choice(young_adults)

    A.add_edges_from([(random_old_adult_female,random_old_adult_male),(random_old_adult_male,random_adult_child),(random_adult_child,random_old_adult_female)])
    A.add_edges_from([(random_old_adult_female, random_adult_child_two), (random_old_adult_male, random_adult_child_two),(random_adult_child_two, random_adult_child)])

    old_adult_female_nodes.remove(random_old_adult_female)
    old_adult_male_nodes.remove(random_old_adult_male)

    young_adults.remove(random_adult_child)
    young_adults.remove(random_adult_child_two)

    #print("This is how many adult male kids are left", len(young_adults))
    #print("This is how many adult female kids are left", len(young_adult_female_nodes))

#some random friendships
n =0

while n < 100000:
        A.add_edge(random.choice(A.nodes()), random.choice(A.nodes()))
        n +=1




#Register the Voters:

print("Registering the voters")

nx.set_node_attributes(A, 'Registered', 'No')

for nodes in A.nodes():
    if A.node[nodes]['Age'] != 'Under 18':
        if random.uniform(0,1) < 0.657: #65.7% was registered to vote in 2014. We assume the same for 2016
            A.node[nodes]['Registered'] = 'Yes'

# Now the Vote
nx.set_node_attributes(A, 'Voted', 'No')
nx.set_node_attributes(A, 'Candidate', 'None')
nx.set_node_attributes(A, 'Time', 0)

# based on http://www.realclearpolitics.com/epolls/2016/president/vt/vermont_trump_vs_clinton-5912.html
#Clinton 50%, Trump 32.6, Independent 17.4

x = 0

print("Voting Time!!!")

for nodes in A.nodes():
    Clinton = 0
    Trump = 0
    Independent = 0
    if A.node[nodes]['Registered'] == 'Yes':
        if len(A.neighbors(nodes)) != 0:
            Neighbors = nx.all_neighbors(A,nodes)
            for n in Neighbors:
                if A.node[n]['Registered'] == 'Yes' and A.node[n]['Voted'] == 'Yes':
                    if A.node[n]['Candidate'] == 'Clinton':
                        Clinton += 1
                    elif A.node[n]['Candidate'] == 'Trump':
                        Trump += 1
                    elif A.node[n]['Candidate'] == 'Independent':
                        Independent += 1
        if Clinton == 0 and Trump == 0 and Independent == 0:
            dice_roll = random.uniform(0,1)
            if dice_roll <= 0.5:
               A.node[nodes]['Candidate'] = 'Clinton'
            if dice_roll > 0.5 and dice_roll <= 0.826:
               A.node[nodes]['Candidate'] = 'Trump'
            if dice_roll > 0.826:
               A.node[nodes]['Candidate'] = 'Independent'
        elif Clinton > Trump and Clinton > Independent:
            A.node[nodes]['Candidate'] = 'Clinton'
        elif Trump > Clinton and Trump > Independent:
            A.node[nodes]['Candidate'] = 'Trump'
        elif Independent > Clinton and Independent > Trump:
            A.node[nodes]['Candidate'] = 'Independent'
        A.node[nodes]['Time'] = x
        A.node[nodes]['Voted'] = 'Yes'
        x += 1

print ("Voting has been Cast. This number of people Voted in this election ", x)

print("Now, The counting begins")

#Counting the Vote

Clinton_vote = 0
Trump_vote = 0
Independent_vote = 0

for nodes in A.nodes():
    if A.node[nodes]['Voted'] == 'Yes':
        if A.node[nodes]['Candidate'] == 'Clinton':
            Clinton_vote += 1
        elif A.node[nodes]['Candidate'] == 'Trump':
            Trump_vote += 1
        elif A.node[nodes]['Candidate'] == 'Independent':
            Independent_vote += 1

print("The Tally has been completed --> Clinton:", Clinton_vote, " Trump: ", Trump_vote, " Independent: ", Independent_vote )
print("C: ", (float(Clinton_vote) / float(x)) * 100)
print(" T: ", (float(Trump_vote) / float(x)) * 100)
print(" I: ", (float(Independent_vote) / float(x)) * 100)
  
nx.write_gexf(A,"election_network3_final.gexf")



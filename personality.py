<<<<<<< HEAD
=======
import itertools
import time


>>>>>>> 884a953f971a7c9d29fb3cfbdd4c1d9f362bf8e8
class Personality:
    def __init__(self,
                 name="",
                 kindness=0,
                 naughtiness=0,
                 grace=0,
                 flamboyance=0,
                 shyness=0,
                 cheerfulness=0,
                 intelligence=0,
                 optimism=0,
                 selfishness=0,
                 courage=0):
        self.name = name
        self.kindness = kindness
        self.naughtiness = naughtiness
        self.grace = grace
        self.flamboyance = flamboyance
        self.shyness = shyness
        self.cheerfulness = cheerfulness
        self.intelligence = intelligence
        self.optimism = optimism
        self.selfishness = selfishness
        self.courage = courage

    def __str__(self):
        return 'Kindness = {0}, \n' \
               'Naughtiness = {1}, \n' \
               'Grace = {2}, \n' \
               'Flamboyance = {3}, \n' \
               'Shyness = {4}, \n' \
               'Cheerfulness = {5}, \n' \
               'Intelligence = {6}, \n' \
               'Optimism = {7}, \n' \
               'Selfishness = {8}, \n' \
<<<<<<< HEAD
               'Courage = {9}'.format(self.kindness, self.naughtiness, self.grace,
                                      self.flamboyance, self.shyness, self.cheerfulness,
                                      self.intelligence, self.optimism, self.selfishness,
                                      self.courage)
=======
               'Courage = {9}'.format(
            self.kindness, self.naughtiness, self.grace, self.flamboyance, self.shyness, self.cheerfulness,
            self.intelligence, self.optimism, self.selfishness, self.courage)
>>>>>>> 884a953f971a7c9d29fb3cfbdd4c1d9f362bf8e8
        # return self.name

    def to_string(self):
        return self.name


def personality_sum(a):
    total = a.kindness
    total += a.naughtiness
    total += a.grace
    total += a.flamboyance
    total += a.shyness
    total += a.cheerfulness
    total += a.intelligence
    total += a.optimism
    total += a.selfishness
    total += a.courage
    return total


def add_traits(a, b):
    c = Personality()
    c.kindness = max(a.kindness, b.kindness)
    c.naughtiness = max(a.naughtiness, b.naughtiness)
    c.grace = max(a.grace, b.grace)
    c.flamboyance = max(a.flamboyance, b.flamboyance)
    c.shyness = max(a.shyness, b.shyness)
    c.cheerfulness = max(a.cheerfulness, b.cheerfulness)
    c.intelligence = max(a.intelligence, b.intelligence)
    c.optimism = max(a.optimism, b.optimism)
    c.selfishness = max(a.selfishness, b.selfishness)
    c.courage = max(a.courage, b.courage)
    return c


def sum_after_subtracting_personality(pers_list, personality):
    if len(pers_list) <= 1:
        return 0
    if personality not in pers_list:
        print("personality not in list")
        return personality_sum(add_traits_list(pers_list))
    temp = []
    temp.extend(pers_list)
    temp.remove(personality)
    post_sum = personality_sum(add_traits_list(temp))
    return post_sum


def add_traits_list(pers_list):
    if len(pers_list) == 0:
        return []
    if len(pers_list) == 1:
        return pers_list[0]
    else:
        return add_traits(pers_list[0], add_traits_list(pers_list[1:]))


<<<<<<< HEAD
def personality_total(personality_list):
    result = []
    num_of_subsets = 1 << len(personality_list)
=======
def personality_total(personalities):
    result = []
    num_of_subsets = 1 << len(personalities)
>>>>>>> 884a953f971a7c9d29fb3cfbdd4c1d9f362bf8e8

    for i in range(num_of_subsets):
        subset = []
        mask = 1

<<<<<<< HEAD
        for k in range(len(personality_list)):
            if (mask & i) != 0:
                subset.append(personality_list[k])
=======
        for k in range(len(personalities)):
            if (mask & i) != 0:
                subset.append(personalities[k])
>>>>>>> 884a953f971a7c9d29fb3cfbdd4c1d9f362bf8e8
            mask = mask << 1
        result.append(subset)
    return result


MAX_TRAITS = 22000
personalities = []
standard = Personality(name="Standard")
friendly = Personality(name="Friendly", kindness=5, naughtiness=20)
tomboy = Personality(name="Tomboy", kindness=50, cheerfulness=100)
gentle = Personality(name="Gentle", kindness=100, grace=100)
pure = Personality(name="Pure", kindness=200, cheerfulness=300, optimism=500)
intelligent = Personality(name="Intelligent", grace=2000, shyness=500, intelligence=2500)
tsundere = Personality(name="Tsundere", naughtiness=1500, shyness=500, intelligence=800)
timid = Personality(name="Timid", kindness=500, shyness=1500, courage=1500)
sweet = Personality(name="Sweet", kindness=800, optimism=2000, selfishness=4000)
yandere = Personality(name="Yandere", naughtiness=1900, shyness=2300, intelligence=1000, selfishness=3000,
                      courage=400)
princess = Personality(name="Princess", grace=1000, flamboyance=2500, intelligence=1500, selfishness=4000)
bossy = Personality(name="Bossy", kindness=500, naughtiness=2000, grace=3000, intelligence=3500)
chunibyo = Personality(name="Chunibyo", naughtiness=1500, flamboyance=2000, cheerfulness=2000, optimism=2000,
                       selfishness=1500)
kuudere = Personality(name="Kuudere", kindness=2500, grace=2000, intelligence=2500, courage=2000)
personalities.extend((standard, friendly, tomboy, gentle, pure, intelligent, tsundere, timid, sweet, yandere,
                      princess, bossy, chunibyo, kuudere))


<<<<<<< HEAD
def personality_combinations(personality_list, number_of_personalities):
    all_subsets = personality_total(personality_list)
=======
def personality_combinations(personalities, number_of_personalities):
    all_subsets = personality_total(personalities)
>>>>>>> 884a953f971a7c9d29fb3cfbdd4c1d9f362bf8e8
    count = 0
    # first_personalities = [standard, friendly, tomboy]
    for subset in all_subsets:
        # total = 0
        # inList = False
        if len(subset) > 0:
            total = personality_sum(add_traits_list(subset))
            # numElements = 0
            # for i in subset:
            #     if i in first_personalities:
            #         numElements += 1
            # if(len(first_personalities) == numElements):
            #     inList = True
            if total <= 22000 and len(subset) == number_of_personalities:
                # print("Subset is: ", end=" ")
                # for a in subset:
                #     print(a.to_string(), end = " ")
                # print()
                is_valid = True
<<<<<<< HEAD
                for i in personality_list:
=======
                for i in personalities:
>>>>>>> 884a953f971a7c9d29fb3cfbdd4c1d9f362bf8e8
                    subset_sum = total
                    # sum_after_subtracting = 0

                    if i not in subset:
                        # print(f"sum before adding {total}" )
                        sum_after_adding = personality_sum(add_traits(i, add_traits_list(subset)))
                        # print(f"sumAfterAdding is {sumAfterAdding}")
                        # print(f"len of subset is {len(subset)}")

                        if subset_sum == sum_after_adding or sum_after_adding < 22000:
                            # print("\tsubset not included is")
                            # print("\t", end = "")
                            # for z in range(len(subset)):
                            #      print(subset[z].to_string(), end=" ")
                            # print()
                            # print(f"\tBecause by ADDING {i.to_string()} \
                            # to the subset whose total is {subsetSum}, you get {sumAfterAdding}")
                            is_valid = False
                            break
                    # else:
                    #     sumAfterSubtracting = sum_after_subtracting_personality(subset, i)
                    #     #print(f"subtracting subset length is {len(subset)}")
                    #     if(subsetSum == sumAfterSubtracting):
                    #         # print(f"\tlen of subset is {len(subset)}")
                    #         # print("\tsubset not included is")
                    #         # print("\t", end = "")
                    #         # for z in range(len(subset)):
                    #         #      print(subset[z].to_string(), end=" ")
                    #         # print()
                    #         # print(f"\tBecause by SUBTRACTING {i.to_string()} \
                    #         from the subset whose total is {subsetSum}, you get {sumAfterSubtracting}")
                    #         isValid = False
                    #         break
                # print()
                for personality in range(len(subset)):
                    # print(f"isValid is {isValid}")
                    # print(personality)
                    # print(len(subset))
                    if personality < len(subset) - 1 and is_valid:
                        print(subset[personality].to_string(), end=', ')
                    elif personality >= len(subset) - 1 and is_valid:
                        print(subset[personality].to_string())
                if is_valid:
                    count += 1
                    print(f"Total points: {total} \tTotal number of personalities: {len(subset)}")
                    print(f"Point distribution: \n{add_traits_list(subset)}")
    print(count)


personality_combinations(personalities, 12)
print(add_traits_list(personalities))

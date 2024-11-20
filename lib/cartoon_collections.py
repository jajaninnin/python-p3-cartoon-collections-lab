# import ipdb

def roll_call_dwarves(lst):
    num = 0
    for dwarf in lst:
        num += 1
        print(str(num) + ". " + dwarf)

def summon_captain_planet(lst):
    result = []
    for word in lst:
        new_word = word.capitalize() + "!"
        result.append(new_word)
    return result

def long_planeteer_calls(lst):
    for word in lst:
        if len(word) > 4:
            # ipdb.set_trace()
            return True
    return False
    

def find_the_cheese(lst):
    cheese = ['cheddar', 'gouda', 'camembert']
    # for word in lst:
    result = [word for word in cheese if word in lst]
    if len(result) > 0:
        return result[0]
    else:
        return None


# if __name__ == '__main__':
# #     listItems = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]
# #     # roll_call_dwarves(["Dopey", "Grumpy", "Bashful"])
#     # result = long_planeteer_calls(['axe', 'earth', 'wind', 'fire'])
#     find_the_cheese(["banana", "cheddar", "sock"])
#     ipdb.set_trace()
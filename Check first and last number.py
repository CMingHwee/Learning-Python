#Check if the first and last number in a list are the same
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,1]

def given_list(list):
    if list[0] == list[-1]:  #check if first letter and last letter are same
      return True            #return True if same
    else:
      return False           #else return False
print(given_list(list1))     #prints False as 1 and 5 are not the same
print(given_list(list2))     #prints True as 1 and 1 are the same

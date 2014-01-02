'''
Write a function to count the number of occurrences of each n-gram in a given input text (see http://en.wikipedia.org/wiki/N-gram for a definition).

ex. for n=2, "to be or not to be" yields
  "to be": 2
  "be or": 1
  "or not": 1
  "not to": 1
'''

#function returns list of list seperated by the value n EX: [1,2,3,4] -> [[1,2],[3,4]] if N was 2
def listOfList(x,N):
    return lambda x, N: [x[i;i+N] for i in range(0, len(x), N)]

def main():  
    N_value = int(raw_input("N value: "))# get value of N
    sentance = raw_input("Eneter text: ")# get sentance
    sentance_list = sentance.split()#splits sentance into words
    while sentance_list.length > 0:
        new_list = listOfList(sentance_list,N_value) # get list of list based on N value
        print new_list[0] + new_list.count(new_list[0]) #prints Ngrams
        del sentance_list[0] # deletes from the front of the list and repeats til the list if gone
        
if __name == "__main__":
    main()

# The print out will print per example "to be" with 2 and 1 since its using the same list. I havent figured out how to avoid this yet.

#sites used
# wiki.python.org
# stackoverflow.com
    
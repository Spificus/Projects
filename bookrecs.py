'''I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project
if I am found in violation of this policy.'''

rating_dict = {}
affinity_dict = {}
book_author_lyst = []

def dotprod(x,y):
    '''calculates the affinity score between two readers'''
    sum = 0
    for i in range(len(x)):
        sum += (x[i] * y[i])
    return sum

with open('booklist.txt') as bookfile:
    '''opens booklist.txt and reads it into a list of book author/book tuples'''
    for line in bookfile:
        tups = line.rstrip().split(',')
        book_author_lyst.append((tups[0],tups[1]))

with open('ratings.txt') as ratefile:
    '''opens ratings.txt and reads all the information into a dictionary
with readers as the keys and their scores as the values'''
    data = ratefile.readline()
    while data != "":
        data = data.lower().strip()
        ratings = ratefile.readline().rstrip().split()
        rating_dict[data] = list(map(int, ratings))
        data =ratefile.readline()

'''Creates a dictionary of people with dictionaries of the other people and their 
scores in relation to the original person using the dot product'''
for person in rating_dict:
                scores = {}
                for person2 in rating_dict:
                        if person != person2:
                                scores[person2] = dotprod(rating_dict[person], rating_dict[person2])
                affinity_dict[person] = scores

def friends(name, numfriends = 2):
    '''determines the 2 closest friends
     of a person based on similarities in ratings'''
    sortedfriends = sorted(affinity_dict[name], key=affinity_dict[name].get, reverse=True)
    return sorted(sortedfriends[0:numfriends])

def sortkey(authorbook):
    '''sorts recommends by author's last name'''
    author = authorbook[0].strip().split()
    return author[-1]

def recommend(name,nfriends = 2):
    '''recommends books to a person based on the scores of their 2 closest friends'''
    recommendedbooks = []
    topfriends = friends(name, nfriends)
    for friend in topfriends:
        for i in range(len(rating_dict[name])):
            if rating_dict[name][i] == 0 and rating_dict[friend][i] >= 3 and book_author_lyst[i] not in recommendedbooks:
                recommendedbooks.append(book_author_lyst[i])
    return sorted(recommendedbooks, key = sortkey)
          
def report():
    '''returns a single string with the full report'''
    fullreport = ''
    people = list(rating_dict.keys())
    for person in sorted(people):
        fullreport += f"{person} : {friends(person)} \n"
        for book in recommend(person):
            fullreport += f"\t{book}\n"
        fullreport += "\n"
    return fullreport

def main():
    """ Prints recommendations for all readers """ 
    with open('recommendations.txt', 'w') as rec_file:
        print(report(), file=rec_file) 
if __name__ == '__main__':
    main()


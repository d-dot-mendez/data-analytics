movies=["Coraline","Saw","Anastasia"]
length = len(movies)

#print(f"The movies includes the {length} movies." )
#print(f"The movies are: {movies}")

#When I used the sorted function, I noticed that it sorted my list alphabetically. 
#print(movies)
#print(sorted(movies))

#When i compare the two functions below, I noticed that once I placed .sort() after the list name
#The program understood that I wanted the list to be sorted each time I refer to it.
movies.sort()
print(movies)

#I noticed that the program added Mulan to the list of movies but that was after the second print. 
#Furthermore, It did not include the addition of Mulan in the sort.
movies.append("Mulan")
print(movies)
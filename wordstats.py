#
#   wordstats.py:
#
#     Starting code for Lab 6-4
#

# we'll learn more about reading from text files in HTT11...

FILENAME = 'words.txt'

fvar = open(FILENAME, 'r')  # open file for reading

bigline = fvar.read() # read ENTIRE file into single string

# what happens when you print such a big line?
# try it, by uncommenting next line

# print (bigline)

# the following print illustrates the printf-formatting approach in Python
# # this is the "old way", and not discussed in our book...

# [L6-4a] total number of characters, including newlines

print("Number of characters is: %d" % len(bigline))

# [L6-4b] total number of words in the file
#   hint: each word ends with a newline


# [L6-4c] average length of a word


# [L6-4d] count of 'e' in all words


# [L6-4e]

fvar.close()



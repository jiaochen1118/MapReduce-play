# MapReduce-play
This is a play programming about implement the idea of MapReduce, based on the material of Introduction to Data Science in Coursera.
##wordcount.py
count the word frequency occurs in the tons of documents.

##invert_index.py
Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears.Using

<source lang= "python">
python invert_index.py data/book.json
</source>
##friends_count.py and assymetric_friendship.py
Consider a simple social network dataset consisting of a set of key-value pairs (person, friend) representing a friend relationship between two people. Describe a MapReduce algorithm to count the number of friends for each person. And the friendship might not be symetric so that we need to rebuild the symetric relationship based on data.

##multiply.py
Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. Design a MapReduce algorithm to compute the matrix multiplication A x B

# Wordsearch Solver Python
First it asks for a text file which contains the wordsearch. Then it imports the data into arrays. The user inputs the word they want to find and it prints the wordsearch with the word highlighted, so you can clearly see its position. The algorithm to find the word goes through the wordsearch to find all of the first letters of the word and stores these positions in an array. Then it uses a depth-first algorithm (DFS) to go through each of the starting letters and the 8 possible directions to find the word.  
Make sure your Command Line directory is the folder containing the wordsearch text file.

## Built With

Python 3.6. Should work with 2.7 with little or no modifications.

## Breakdown of files/folders
* readme.md - This readme markdown file
* Example Wordsearch.txt - A text file containing an example wordsearch
* wordsearch_solver.py - This is the python script where all the fun happens :)

## License

You may download/use/distribute/modify/host/sell the code however you like. There are no restrictions.
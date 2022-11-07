#Text generation using Markov Chains
The program generates text using a probability of certain character existing after 5 preceding it.

Example:
./poor_mark.py --output output.txt --length 10 input_text.txt
generates a string of 10 characters and saves them to a file named "output.txt"

./poor_mark.py input_text.txt
displays a string of DEFAULT (10000) generated characters

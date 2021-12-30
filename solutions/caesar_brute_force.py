import os
import sys

RING_SIZE = 128

#open the file and read it's contents into a buffer
def load_buffer(file_name):
    size = os.path.getsize(file_name)
    buffer = ""
    with open(file_name, 'r') as f:
        buffer = f.read(size)
    return buffer

#BRUTE FORCE: get all possible solutions for a brute force analysis
#we know for the shift cipher there are 128 possible solutions
#and the key can range from 0 - 128 (due to modular arithmetic)
#let solution_set[i] = the buffer with possible solution i so len(solution_set) = 128
def get_possible_solutions(buffer):
    solution_set = []
    s_i = ""
    l = len(buffer)
    for i in range(0, RING_SIZE):
        for n in range(0, l):
            char = chr( (ord(buffer[n])  - i) % RING_SIZE  )
            s_i += char
        solution_set.append(s_i)
    return solution_set

#if the integer ASCII value of the first two bytes produces printable data
#i.e. ord(first byte) < 128 && ord(second byte) < 128, there is a good chance 
#both the brute force and analytical solutions to the shift cipher

#that is the correct answer, and we can remove anything else
#since the shift scipher used modular arithmetic, everything in the solution set should be printable
#and this should not change the length of the solution set
#this function could be useful in narrowing the solutions for a bitwise permutation, though
def narrow_down_solutions(solution_set):
    l = len(solution_set)
    for i in range(0, l):
        b0 = (solution_set[i])[0]
        b1 = (solution_set[i])[1]
        possible = (( ord(b0) and ord(b1) ) < 128 ) and ((ord(b0) and ord(b1)) >= 0)
        if not possible: 
            solution_set.remove(solution_set[i])
            i -= 1
    return solution_set

#the analytical solution for the shift cipher involves
#seeing which character appears most frequently in the text
#the most common letters in english plaintext are e, a, o , i
#note that this analytical solution only works because I'm familiary with my input text
#if trying to use an analytical solution on a regular document, you may want to note things like
#how the first letter of every sentence is capitalized, and how every sentence ends with a period
def analytical_solution(cipher_text):
    #frequent_symbols is a dictionary that tracks every symbol in the cipher_text and it's frequency
    #for i in cipher_text:
    #if we have not discovered this symbol, add it to the dictionary with value : 0
    #if we have discovered this symbol, update it's value
    symbol_frequency = {}
    found = False
    possible_key = -1
    for i in cipher_text:
        if i in symbol_frequency: symbol_frequency[i] += 1
        else: symbol_frequency[i] = 1
    print("cipher_text: ", cipher_text)
    print("symbol_frequency: ", symbol_frequency)
    #continue to pull the max symbol until you find 'e' - and you find the right key associated with it
    #i.e., cipher_text(presumed to be 'e') - possible key = 'e'
    while not found:
        possible_e = max(symbol_frequency, key = symbol_frequency.get)
        for i in range(128):
            #decrypt the possible e, with every possible key 0-127 
            #once we have the most frequent cipher text symbols
            #we can check if any of them match our guess for what the most frequent cipher text is " " most likely 
            char = chr( (ord(possible_e)  - i) % RING_SIZE  )
            if char == " ":
                possible_key = i
                found = True
        del symbol_frequency[possible_e]
    print(decrypt(cipher_text, possible_key))
    return possible_key
#PROBLEMS WITH ANALYTICAL SOLUTION: it could be that for a given plain text, the character we guess is the most
#frequent is not actually the most frequent, in this case a human would have to go through and change line 74
#to be equal to the next guess, if this one does not result in readable plaintext
#once we have a possible key, attempt to decrypt the ciphertext with it
def decrypt(cipher_text, key):
    plain_text = ""
    for i in cipher_text:
        char = chr( (ord(i) - key) % RING_SIZE  )
        plain_text += char
    return plain_text 


file_name = sys.argv[1]
buffer = load_buffer(file_name)
#allow the user to chose from either the brute force or 

brute_solution_set = get_possible_solutions(buffer)
key = analytical_solution(buffer)
print("the possible key given by analytical solution is: ", key)
#we now have a solution set with 128 possible solutions, the problem is now picking which one is valid



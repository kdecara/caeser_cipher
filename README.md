# Intro to the Caeser Cipher
The caesaer cipher is the one of the simplest encryption algorithms. While not at all used or secure (the brute force attempt is produces 128 possible options)
implementing it still serves a purpose in practicing programming skills and learning about cryptography.

# Encryption-Decryption
The shift cipher takes the plain text ASCII set and adds some cipher K to each character to create a new character. If (character + K) > 127 (127 is the max ASCII value) then values
will wrap around using modular arithmetic. so if a given character's ASCII value is 127 and the cipher is 5, ENC = (127 + 5) % 128 = 4 as It's new encrypted ASCII value
Decryption is the same as encryption, except the cipher is subtracted rather than added, so if we know K = 5 and ENC(c) = 5 then DEC(c) = (4 - 5) % 128 = 127

ENC(x) = y = (x + K) % 128

DEC(y) = x = (y - K) % 128

# Brute Force Solution
The brute force solution to caesaer cipher involves applying every possible key 0-127 and checking if the resulting decryption results in readable plain text.
For a future project, it would be interesting to see if this process could be automated, and the possible solution set can be solved automatically by a program which can 
tell which parts of the solution set produce readable text and which do not.

# Analytical Solution
The analytical solution to the shift cipher involves looking at which character appears most frequently in the cipher text, and guessing which character that is.
We know the most frequently used characters are " ", "e", "i", "a", and so on. In the analytical solution uploaded I guessed the most likely character was " " but I
did write the sample text myself, so I know I did not remove blankspaces, etc. Of course, a human must check whether decrypting the most frequent character to your guess
produces readable plain text. If not, it's a matter of simply changing your guess to the next most likely character.

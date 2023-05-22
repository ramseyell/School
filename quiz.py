#   start
score = 0
print("Welcome to the AP CSP review quiz! To select your answer, type A, B, C, or D.")
print("Lets begin!")


#   game
print("What is a group of two or more computer systems linked together called?")
print("A. Data")
print("B. Control structure")
print("C. Network")
print("D. Integrated circut")
answer = input().upper()
if answer == "C":
    score = score + 1

print("What is it called when you copy data (usually an entire file) from a main source to a peripheral device?")
print("A. Download")
print("B. Lossy compression")
print("C. Abstraction")
print("D. Cryptography")
answer = input().upper()
if answer == "A":
    score = score + 1

print("What is the process of representing a real-world object of phenomenon as a set of mathematical equations called?")
print("A. Algorithm")
print("B. Modeling")
print("C. Data aggregation")
print("D. Simulation")
answer = input().upper()
if answer == "B":
    score = score + 1

print("What do you call the art of protecting information by transforming it into an unreadable format called cipher text?")
print("A. Steganography")
print("B. Rasterisation")
print("C. Cryptography")
print("D. Selection")
answer = input().upper()
if answer == "C":
    score = score + 1

print("What is a machine that processes information under the control of a program called?")
print("A. Dossier")
print("B. Database")
print("C. Input devices")
print("D. Computer")
answer = input().upper()
if answer == "D":
    score = score + 1

print("What are data compression techniques in which some amount of data is lost in an attempt to eliminate redundant information called?")
print("A. Simple compression")
print("B. Lossless compression")
print("C. Reversable compression")
print("D. Lossy compression")
answer = input().upper()
if answer == "D":
    score = score + 1

print("What is a binary digit that represents a single unit of information?")
print("A. Bit")
print("B. Code")
print("C. ASCII")
print("D. Byte")
answer = input().upper()
if answer == "A":
    score = score + 1

print("What is the time it takes for one bit to travel from a sender to a receiver called?")
print("A. Bandlength")
print("B. Latency")
print("C. Bit rate")
print("D. Bandwidth")
answer = input().upper()
if answer == "B":
    score = score + 1

print("What are the set of rules governing the exchange or transmission of data between devices called?")
print("A. Moores law")
print("B. Protocol")
print("C. Communication laws")
print("D. HTTP")
answer = input().upper()
if answer == "B":
    score = score + 1

print("What is a computer that waits for and responds to requests for data called?")
print("A. Data abstraction")
print("B. Server")
print("C. Client")
print("D. Internet")
answer = input().upper()
if answer == "B":
    score = score + 1

#   end
print("Congratulations! You have finished the quiz. Your final score is:")
print(score, "out of 10.")
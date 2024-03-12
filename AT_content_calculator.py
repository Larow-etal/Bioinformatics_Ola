print("Hello, welcome to our laboratory")

name = input("Please may I know your name?\n")

print("My name is " + name)

question =  input("Do you wish to calculate the AT content of your DNA sequence?\n")

if question == "Yes":

 sequence = input("Please enter your DNA sequence below\n")

 A_count = sequence.count('A')

 T_count = sequence.count('T')

 length = len(sequence)
 
 AT_content = (A_count + T_count) / length
 
 print("The AT content of your DNA is: " + str(AT_content))

question =  input("Do you wish to derive the complement sequence of your DNA?\n")

if question == "Yes":

 replacement1 = sequence.replace('A', 'H')
 
 replacement2 = replacement1.replace('T', 'J')
 
 replacement3 = replacement2.replace('C', 'K')
 
 replacement4 = replacement3.replace('G', 'L')
 
 replacement5 = replacement4.replace('H', 'T')
 
 replacement6 = replacement5.replace('J', 'A')
 
 replacement7 = replacement6.replace('K', 'G')
 
 replacement8 = replacement7.replace('L', 'C')
 
 print("The complement sequence of your DNA is:\n" + replacement8)

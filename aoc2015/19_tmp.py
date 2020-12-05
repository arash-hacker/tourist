import re

replacements = []
medicine = ""
molecules = []

def calibrate():
    global medicine
    global molecules
    with open("19.txt") as f:
        had_blank = False
        for line in f:
            if not had_blank:
                if len(line)>100 :
                    had_blank = True
                    medicine = line.strip()
                    break
                else:
                    #Get replacements
                    line = line.strip()
                    rep = line.split(" ")
                    replacements.append((rep[0], rep[-1]))
            else:
                #Get medicine molecule
                medicine = line.strip()

    #Try all replacements
    for replacement in replacements:
        print("Checking %s => %s" % replacement)
        #Find instances of medicineing atom
        matches = [m.start() for m in re.finditer(replacement[0], medicine)]
        for match in matches:
            new_one = medicine[:match] + replacement[1] + \
            medicine[match + len(replacement[0]):]
            print("Replacing at %d: %s" % (match, new_one))
            if new_one not in molecules:
                molecules.append(new_one)

    print(len(molecules))

def synth():
    #All Rn and Ar match to (X) for X an element
    #Y matches to , within Rn/Ar constructs, to form (X,X)

    elements = sum(1 for c in medicine if c.isupper())
    rn_ar = len([m.start() for m in re.finditer("Rn|Ar", medicine)])
    y = len([m.start() for m in re.finditer("Y", medicine)])
    print(elements - rn_ar - 2*y - 1)

if __name__ == '__main__':
    print("Part 1:")
    calibrate()
    """
    for molecule in molecules:
        print(molecule)
    """
    print("Part 2:")
    synth()
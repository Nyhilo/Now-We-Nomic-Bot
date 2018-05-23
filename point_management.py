#

#load the playerlist, if it exists

def loadPlayerlist(filename):
    output = []
    # This one's a doozy. Mostly this is just checking the input file formatting
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Initialize the first user
            firstname = lines.pop(0).strip()
            output.append({"Name":firstname.strip()})
            output[0]["Items"] = {}

            index = 0
            lineNumber = 1    # The first name was line 1

            # Iterate through the rest of the lines.
            # New players will create a new entry in the output list
            # Additional items will be added to the items dictionary for the current index
            for line in lines:
                lineNumber += 1

                # Additional item
                if line.startswith("    ") or line.startswith("\t"):
                    item = line.strip().split(';')
                    if len(item) == 1:
                        print("No amount listed for " + item[0] + " on line " + lineNumber +
                            ". Defaulting to 1.")
                        output[index]["Items"][item[0]] = {}
                        output[index]["Items"][item[0]]["Amount"] = 0

                    if len(item) >= 2:
                        output[index]["Items"][item[0]] = {}
                        try:
                            output[index]["Items"][item[0]]["Amount"] = float(item[1])
                        except ValueError:  # item[1] not a number
                            print("Amount for " + item[0] + " on line " + lineNumber +
                                " listed as " + item[1] + ". Defaulting to 0.")
                            output[index]["Items"][item[0]]["Amount"] = 0

                    if len(item) > 2:   # Line contains additional details
                        output[index]["Items"][item[0]]["Notes"] = item[2]

                # Blank line
                elif line.strip() == "":
                    pass

                # Next player
                else:   # If the line is a new name
                    index += 1
                    output.append({"Name":line.strip()})
                    output[index]["Items"] = {}

        return output

    except FileNotFoundError:
        print("File: " + filename + " not found, creating file.")
        with open(filename, 'w+') as file:
            pass    # Just create the file, it's empty
        return []

# Format: [{Name:Username, Items:{Points:#, Item:{Amount:$, Notes:""}, etc...}}, {etc...}]
playerlist = loadPlayerlist("playerlist")



def init():
    print("Hello Points")

if __name__ == '__main__':
    print(playerlist[1]["Name"])

def read_db():
    with open("vars", "r") as file:
        # dataen er lagra på linje 4 og 6
        lines = [line.strip() for line in file.readlines()]
        try:
            expires, modified = lines[3], lines[5]
            if not expires or not modified:
                return False
            return expires, modified
        except IndexError:
            return False
    

def write_db(exp, mod):
    with open("vars", "r") as file:
        lines = file.readlines()
        lines[3], lines[5] = f"{exp}\n", f"{mod}\n"

    with open("vars", "w") as file:
        file.writelines(lines)
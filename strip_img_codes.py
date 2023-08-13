def getcodes(filename):
    codes = []
    with open(filename, 'r') as reader:
        for line in reader:
            if line[0:9] == "IMG Codes":
                l = line[10:].split()
                codes.append(l[0])
                if len(l) == 5:
                    codes.append(l[1])
                elif l[1] == "Female":
                    codes.append(l[2])
                elif l[2] == "Female":
                    codes.append(l[1])
                    codes.append(l[3])
    return codes

def makecss(codes):
    return "img[src*=\"pkmn/" + ".png\"],\nimg[src*=\"pkmn/".join(codes) + ".png\"]{\n\tborder: dashed;\n}"

if __name__ == "__main__":
    exclusives = getcodes("exclusives.txt")
    variants = getcodes("variants.txt")
    with open("exclusives_css.txt", 'w') as writer:
        writer.write(makecss(exclusives))
    with open("variants_css.txt", 'w') as writer:
        writer.write(makecss(variants))
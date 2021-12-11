import random
nucleobases = ["G","A","T","C"]
dna_file = open("dna.txt", "x")

for x in range(1000):
    base_pair = str.join(random.choice(nucleobases), random.choice(nucleobases))
    dna_file.write(base_pair)
    
dna_file.close()

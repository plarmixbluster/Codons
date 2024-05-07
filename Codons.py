from random import choice, choices

nucleobase = "AGCT"

start_codon = "ATG"
stop_codon = ("TAG", "TAA", "TGA")


def isPotentialGene(DNA: str):
    if (len(DNA) % 3) != 0:
        return False

    if not DNA.startswith(start_codon):
        return False

    for i in range(len(DNA) - 3):
        if i % 3 == 0:
            if DNA[i:i+3] in stop_codon:
                return False

    if DNA.endswith(stop_codon[0]):
        return True
    if DNA.endswith(stop_codon[1]):
        return True
    if DNA.endswith(stop_codon[2]):
        return True
    return False


# 0
def generateCodon(triplets: int):
    if triplets <= 0:
        raise ValueError("the minimum number of triplets is 1")
    codons = ""
    while triplets > 0:
        if (codon := "".join(choices(nucleobase, k=3))) not in stop_codon:
            codons += codon
            triplets -= 1
    return codons


def generateDNA(length: int):
    if length <= 6 or length % 3 != 0:
        raise ValueError("the length of the DNA must be greater than six and a multiple of six")
    return start_codon + generateCodon(int((length - 6) / 3)) + choice(stop_codon)


# 1
def isValidDNA(st: str):
    return set(st).issubset(nucleobase)


# 2
def complementWC(DNA: str):
    return ''.join([{'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[base] for base in DNA])


# 3
def palindromeWC(DNA: str):
    return DNA == complementWC(DNA)[::-1]


# 4
def isShift(s: str, t: str):
    return len(s) == len(t) and t in s + s


# 5
def find_PotentialGene(DNA: str, length: int):
    potential_genes = []
    for i in range(len(DNA)):
        if DNA[i:i+3] == start_codon:
            for j in range(i+3, len(DNA), 3):
                if DNA[j:j+3] in stop_codon:
                    gene = DNA[i:j+3]
                    if len(gene) >= length and len(gene) % 3 == 0:
                        potential_genes.append(gene)
                    break
    if not potential_genes:
        return None
    return potential_genes


# 6
def caesar_cipher(text: str, ROT: int, decipher=False):
    if ROT < 0:
        raise ValueError("the number of shifts must be greater than or equal to zero")
    encrypted_text = ""
    if decipher:
        ROT = -ROT
    for char in text:
        if char.isalpha():
            shifted = ord(char) + ROT
            if char.islower():
                if shifted > ord("z"):
                    shifted -= 26
                elif shifted < ord("a"):
                    shifted += 26
            elif char.isupper():
                if shifted > ord("Z"):
                    shifted -= 26
                elif shifted < ord("A"):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    if not encrypted_text:
        return None
    return encrypted_text

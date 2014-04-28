foo = "SSYYNNOOPPSSIISS"
foo = ''.join([foo[i] for i in range(len(foo)-1) if foo[i+1]!= foo[i]]+[foo[-1]])
# print foo

def remove_duplicate_letters(s):
    out = ''
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            out += s[i]
    # append last character
    out += s[-1]
    return out

print remove_duplicate_letters('hhhhho')


def reverseWords( s: str) -> str:
    splitted_sent = s.split()
    new_lis = []
    rev_str = ""
    for i in range(len(splitted_sent)):

        x = splitted_sent[i][::-1] # this is how to reverse the sentence letters
        new_lis.append(x)
        rev_str += x
        if i == len(splitted_sent) - 1:
            rev_str += ""
        else:
            rev_str += " "
    return rev_str
def main():
    sente = "My name is Liberty"
    print(reverseWords(sente))

main()
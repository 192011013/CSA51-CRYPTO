l1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
      'X', 'Y', 'Z']
ct = input("Enter the cipher text: ")
alphabet = ""
for i in ct:
    if i != " ":
        if i in l1:
            x = l1.index(i)
            print(x, end=",")
            new_index = int(((x - 1) / 1) % 26)
            print(new_index, end=",")
            alphabet = alphabet + l1[new_index]
            print(l1[new_index])

    print(alphabet)

def encryption(text,key):
    ciphertext = ""
    cycle = key*2-2

    for row in range(key):
        index = 0
        if row == 0:
            while index < len(text):
                ciphertext += text[index]
                index += cycle
        elif row == key - 1:
            index = row
            while index < len(text):
                ciphertext += text[index]
                index += cycle
        else:
            left_index = row
            right_index = cycle - row
            while left_index < len(text):
                ciphertext += text[left_index]

                if right_index < len(text):
                    ciphertext += text[right_index]

                left_index += cycle
                right_index += cycle

    print(ciphertext)

encryption("ali babanin bir ciftligi var ciftliginde inekleri var",4)

def send_string(string):

    char, string = string[0], string[1:]
    while char:

        if char == "\\":

            escape = ""
            char, string = string[0], string[1:]
            while char != "\\":
                escape += char
                char, string = string[0], string[1:]

            if escape:
                print(escape)
            else:
                print("\\")
        else:
            print(char)

        if string:
            char, string = string[0], string[1:]
        else:
            char = ""

if __name__ == "__main__":
    send_string("hello world")

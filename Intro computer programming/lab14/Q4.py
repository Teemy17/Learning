def rep_text():
    while True:
        try:
            file = input("Enter file name: ")
            with open(file, "r") as f:
                text = f.read()
            old_str = input("Enter string to replace: ")
            new_str = input("Enter new string: ")
            
            if old_str == new_str :
                raise ValueError("Old and new strings cannot be the same.")
            
            if old_str in text:
                text = text.replace(old_str, new_str)
            else:
                print("String not found.")
                continue
            with open(file, "w") as f:
                f.write(text)
            print("String replaced successfully.")
            break
        except FileNotFoundError:
            print("File not found.")

        except ValueError as e:
            print(e)
            break

rep_text()


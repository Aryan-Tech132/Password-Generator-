import string
import random
class PasswordGenerator:
    def __init__(self,length):
        self.length=length
    def generate_password(self):
        if self.length < 6:
            raise ValueError("password length should be at least 6 characters.")
        
        lowercase=string.ascii_lowercase
        uppercase=string.ascii_uppercase
        digits=string.digits
        symbols="!@$%&§*"
 
        password=[
             
             random.choice(lowercase),
             random.choice(uppercase),
             random.choice(digits),
             random.choice(symbols),
         ]

        all__characters = lowercase + uppercase + digits + symbols 

        password.extend(
            random.choice(all__characters)
            for _ in range(self.length-4)
        )

        random.shuffle(password)

        return "".join(password)
def main():
    print("=" * 50)
    print("        SECURE PASSWORD GENERATOR")
    print("="*50)

    try:
        length= int(input("Enter password length:"))

        generator= PasswordGenerator(length)
        password= generator .generate_password()

        print("\nGenerated Passwprd:")
        print("_"*50)
        print(password)
        print("_"*50)

    except ValueError as error :
        print(f"Error:{error}")

if __name__ == "__main__":
    main()
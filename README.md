# 🔐 Secure Password Generator (Python)

A simple and secure password generator built using Python. This project generates strong random passwords containing lowercase letters, uppercase letters, numbers, and special characters.

## 🚀 Features

- Generates secure random passwords
- User chooses the password length
- Includes at least:
  - ✅ One lowercase letter
  - ✅ One uppercase letter
  - ✅ One digit
  - ✅ One special character
- Minimum password length validation (6 characters)
- Simple command-line interface
- Built using Python's `random` and `string` modules

## 🛠️ Technologies Used

- Python 3
- random module
- string module
- Object-Oriented Programming (OOP)

## 📂 Project Structure

```
PasswordGenerator/
│── main.py
└── README.md
```

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/password-generator.git
```

2. Navigate to the project folder

```bash
cd password-generator
```

3. Run the program

```bash
python main.py
```

## 💻 Example Output

```
==================================================
        SECURE PASSWORD GENERATOR
==================================================
Enter password length: 12

Generated Password:
__________________________________________________
A7@mK2#pqL8!
__________________________________________________
```

## 📖 How It Works

1. The user enters the desired password length.
2. The program checks that the length is at least 6 characters.
3. It guarantees the password contains:
   - One lowercase letter
   - One uppercase letter
   - One number
   - One special character
4. The remaining characters are selected randomly.
5. The password is shuffled to increase randomness.
6. The final secure password is displayed.

## 📚 Key Concepts Used

- Classes and Objects
- Constructors (`__init__`)
- Functions
- Exception Handling (`try-except`)
- Random Module
- String Module
- Lists
- Loops
- User Input
- String Manipulation

## 🎯 Future Improvements

- Copy password directly to clipboard
- Password strength indicator
- Custom special characters
- Option to include/exclude symbols
- Save generated passwords to a file
- GUI version using Tkinter

## 👨‍💻 Author

**Aryan Kumar**

---

⭐ If you found this project helpful, consider giving it a Star on GitHub!

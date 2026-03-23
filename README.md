# Python-Email-Validation

Email validation in Python using two approaches: **manual validation and regular expressions**.

This project demonstrates how to check whether an email address is valid using two different techniques in Python. It is designed for beginners who want to understand **string validation logic and pattern matching**.

---

## Project Structure

```
Python-Email-Validation
│
├── README.md
└── src
    ├── EmailValidation.py
    └── using_regex.py
```

---

## EmailValidation.py

- Validates email using **manual conditions**
- Uses **loops, string methods, and logical checks**
- Helps understand the **internal logic of email validation**

---

## using_regex.py

- Validates email using **Regular Expressions (Regex)**
- Uses Python’s built-in **`re` module**
- Demonstrates a **shorter and more powerful validation approach**

---

## Rules for a Valid Email

The program checks whether the email follows these basic rules:

1. The email must contain **at least 6 characters**
2. The email must **start with a letter**
3. The email must contain **exactly one `@` symbol**
4. The email must contain a **`.` after the `@`**
5. The domain extension must be **at least 2 characters** (like `.com`, `.in`)
6. The email must **not contain spaces**

---

## Allowed Characters

```
Letters (A-Z, a-z)
Numbers (0-9)
Dot (.)
Underscore (_)
Hyphen (-)
```


# Bank Account System using Python OOP | Simple Project

This is a beginner-friendly Python project demonstrating **Object-Oriented Programming (OOP)** concepts like:
- Encapsulation
- Inheritance
- Polymorphism
- Classes and Objects

##  Features
- Create Bank Account (Savings / Current)
- Deposit money
- Withdraw money
- Check balance
- Calculate interest

##  OOP Concepts Used
| Concept | Usage |
|--------|-------|
| Encapsulation | `__balance` made private |
| Inheritance | `SavingsAccount` & `CurrentAccount` inherit `BankAccount` |
| Polymorphism | `calculate_interest()` overridden |
| Class & Object | Objects created: `acc` |

##  Code Structure
BankAccount (Parent Class)
│
├── SavingsAccount (Child Class) → 5% interest
└── CurrentAccount (Child Class) → 2% interest

## ▶ How to Run
```bash
python bank_account.py

🖥 Sample Output
---- Create Bank Account ----
Enter Name: Akash
Enter Starting Balance: 10000
1. Savings Account
2. Current Account
Enter 1 or 2: 1

---- Account Created Successfully ----
Account Holder: Akash
Balance: 10000.0

Enter Deposit Amount: 2000
Updated Balance: 12000.0

Enter Withdraw Amount: 5000
Updated Balance: 7000.0

Interest Earned: 350.0

## **🚀 Future Enhancements**
- Add login with PIN
- Add database storage
- Create menu-driven system
GUI using Tkinter or web interface using Flask/Django

💡 Learning Outcome

This project helped me:

Understand OOP practically instead of just theory

Apply Encapsulation, Inheritance & Polymorphism in real example

Gain confidence in object-oriented design

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to improve.

⭐ Support

Give this repository a star  to support and motivate!

🎉 Thank You for Reading!

Excited to share more Python & OOP projects to the community 🚀

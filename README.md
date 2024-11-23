---

# **LearnEdge**

A Python program that reads questions from a CSV file and presents them in a computer-based test (CBT) format. Designed with a user-friendly interface, it supports multiple-choice questions and tracks accuracy for learning purposes.

---

## **Features**

- Reads questions dynamically from a user-selected CSV file.
- Supports multiple-choice question formats (A, B, C, D).
- Displays the correct answer after every question.
- Tracks accuracy at the end of the quiz.
- Built with a graphical user interface (GUI) using Tkinter.

---

## **Installation**

### **Prerequisites**
- Python 3.x installed on your system.
- Required Python packages: `pandas` and `tkinter` (pre-installed with Python).

### **Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/learnedge.git
   ```
2. Navigate to the project directory:
   ```bash
   cd learnedge
   ```
3. Install required dependencies:
   ```bash
   pip install pandas
   ```
4. Prepare the images used for the UI:
   - Ensure the following files are present in an `images` directory:
     - `card_front.png`
     - `card_back.png`
     - `a.png`, `b.png`, `c.png`, `d.png`
     - `next.png`

5. Run the application:
   ```bash
   python main.py
   ```

---

## **Usage**

1. On launching the program, select a CSV file with the following structure:
   | Question   | Option A | Option B | Option C | Option D | Correct Option |
   |------------|----------|----------|----------|----------|----------------|
   | Example Q1 | Answer A | Answer B | Answer C | Answer D | A              |

   - Column names should match exactly as above.

2. Use the GUI buttons to select answers.
3. Once you complete all questions, the program displays your accuracy.

---

## **Technologies Used**

- **Python**: Core programming language.
- **Tkinter**: For building the graphical interface.
- **Pandas**: For handling CSV file operations.

---

## **Contributing**

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git push origin feature-name
   ```
4. Open a pull request for review.

---

## **Acknowledgments**

- Inspired by educational CBT systems.
- Special thanks to the Python community for the resources and tools.

---

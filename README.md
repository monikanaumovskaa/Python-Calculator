# Python-Calculator
Overview
This Python application leverages the tkinter library to build a simple graphical user interface (GUI) calculator. It allows users to perform basic arithmetic operations—addition, subtraction, multiplication, and division—by inputting two numbers and selecting an operator.

Features:
User-Friendly GUI: A clean and interactive interface built with tkinter.
Basic Arithmetic Operations: Supports addition (+), subtraction (-), multiplication (*), and division (/).
Result Display: Shows the result of the calculation in a label after pressing the "Calculate" button.
How It Works:
The calculator accepts three inputs:

First Number: The first operand for the calculation.
Operator: The operation to be performed (+, -, *, /).
Second Number: The second operand for the calculation.
After the user enters the numbers and operator, they can click the "Calculate" button to perform the operation and see the result displayed in a label.

Installation & Usage:
Clone the Repository:

Clone the project to your local machine:
bash
Copy code
git clone https://github.com/RosanaBlazheska/python-project--calculator.git
cd python-project--calculator
Run the Application:

Execute the Python script:
bash
Copy code
python calculator.py
Using the Calculator:

The GUI will display three input fields: one for the first number, one for the operator, and one for the second number.
After entering the numbers and operator, click the "Calculate" button to see the result below in a label.
Code Breakdown:
Entry Fields (entry1, entry2, entry3): These fields collect the first number, the operator, and the second number respectively.
Button (button): When clicked, it calls the calculate function, which performs the selected arithmetic operation.
Label (label): Displays the result of the calculation or an error message if the input is invalid.
Main Logic:
The core of the program is the calculate function:

Retrieves values from the entry fields.
Determines which arithmetic operation to perform based on the operator.
Calculates the result and updates the label to show the output.
Layout:
The window is sized at 600x100 pixels with appropriate padding for spacing. The layout includes:

Three horizontally aligned input fields (for numbers and operator).
A button to trigger the calculation.
A label to display the result.
Notes:
Ensure that valid data is entered: the first and third fields must be numeric, and the second field should contain a valid operator (+, -, *, /).
If any input is invalid, the program will display "Error" in the result label.
Contributions:
Feel free to contribute by submitting issues or pull requests to improve the project.

License:
This project is open-source and licensed under the MIT License.

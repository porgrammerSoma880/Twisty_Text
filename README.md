# Twisty_Type

Welcome to the **Twisty_Type**! This Python program takes a sentence as input and shuffles the words to produce a fun, twisted version of the text. It's simple, interactive, and perfect for generating random, quirky phrases!

---



## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [How to Run](#how-to-run)
4. [Example Usage](#example-usage)
5. [Code Explanation](#code-explanation)
6. [Contributions](#contributions)
7. [Future Enhancements](#future-enhancements-optional)
8. [Legal Notice](#legal-notice)
9. [License](#license)
10. [Author](#author)










## Repository Structure
text
Copy
Edit
├── twisty_type_project.py
├── README.md
├── LICENSE















## Features

- **Interactive User Input**: Enter a sentence and see it twisted instantly.
- **Validation**: Ensures the input has more than one word to shuffle.
- **Randomization**: Uses Python's `random` module to shuffle words unpredictably.
- **Error Handling**: Guides the user if the input is invalid or insufficient.









---

## Requirements

- Python 3.7 or higher

---









## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/porgrammerSoma880/Twisty_Typet.git
   cd Twisty_Type
   ```

2. Run the script using Python:
   ```bash
   python twisty_type_project.py
   ```

3. Follow the on-screen instructions. Type a sentence with more than one word to see its twisted version. Type `exit` to quit the program.

---









## Example Usage

```text Welcome to the Twisty_Type!
Type 'exit' to quit the program.

Enter text to get a fun, twisted version (text must include more than one word!): 
Type 'exit' to quit the program.

Enter text to get a fun, twisted version (text must include more than one word!): Hello World from Python
Normal text: Hello World from Python

Twisted version: Python Hello from World

Enter text to get a fun, twisted version (text must include more than one word!): exit
Goodbye!
```










---

## Code Explanation

### Core Functionality

- **`twisted_text_generate(text: str) -> Optional[str]`**
  - Takes a string input.
  - Splits the input into words.
  - Validates that the input contains more than one word.
  - Shuffles the words until the order changes.
  - Joins the shuffled words into a new sentence and returns it.

- **`main()`**
  - Handles user interaction.
  - Continuously prompts the user for input and processes it using `twisted_text_generate`.
  - Exits when the user types `exit`.









### Libraries Used

- `random`: For shuffling the words.
- `typing`: For type hinting (`List` and `Optional`).

---






## Contributions

Contributions are welcome! If you have ideas to improve this program, feel free to create a pull request or open an issue.

---
1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Submit a pull request with a detailed description of your changes

For significant changes, please open an issue first to discuss your idea.




### How to Contribute
1. Fork the repo  
2. Create a branch: `git checkout -b feature/fooBar`  
3. Commit your changes: `git commit -m 'Add some fooBar'`  
4. Push to the branch: `git push origin feature/fooBar`  
5. Open a Pull Request  














## Future Enhancements (Optional)

- **Multilingual Support**: Extend support for non-English text.
- **Graphical User Interface (GUI)**: Create a simple GUI for non-technical users.

---







## Legal Notice

### Disclaimer
This program was developed for educational and entertainment purposes only. The developer assumes no responsibility for any misuse or issues arising from the use of this program. By using this program, you agree to the following:

## License

This project is open-source and available under the [MIT License](LICENSE).

---





Legal Notice
Disclaimer
This program is provided “as is” for educational and entertainment purposes only. The author assumes no liability for misuse or damages arising from its use.














## Author

Developed with ❤️ by **porgrammerSoma880**.  
For inquiries or feedback, feel free to reach out via GitHub.

---










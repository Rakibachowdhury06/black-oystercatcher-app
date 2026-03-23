"""
CST8002 - Programming Language Research Project
Practical Project Part 3 - Project Review 2
Professor: Stanley Pieda
Due Date: March 29, 2026
Student: Rakiba Chowdhury
Section: 020

This is the main entry point for the Black Oystercatcher data
management program. It creates the presentation layer Menu object
and starts the interactive menu loop.

Dataset Source:
Parks Canada. (2017). Black Oystercatcher Population - Pacific Rim.
Available at: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02
License: Open Government Licence - Canada

References:
[1] Python Software Foundation. (2024). Modules. docs.python.org [Online]. 
Available: https://docs.python.org/3/tutorial/modules.html [Accessed: Feb. 15, 2026].
[2] Python Software Foundation. (2024). Sorting HOW TO. docs.python.org [Online].
Available: https://docs.python.org/3/howto/sorting.html [Accessed: Mar. 20, 2026].
"""
from presentation.menu import Menu


def main():
    """
    Main function that starts the program.

    Creates a Menu instance (presentation layer) and runs the interactive
    menu loop for the user.
    """
    app = Menu()
    app.run()


if __name__ == "__main__":
    main()
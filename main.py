"""
CST8002 - Programming Language Research Project
Practical Project Part 4 - Project Release
Professor: Stanley Pieda
Due Date: April 12, 2026
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
[3] Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. matplotlib.org [Online].
Available: https://matplotlib.org/stable/index.html [Accessed: Apr. 5, 2026].

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
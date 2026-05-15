"""
Author: Rakiba Chowdhury

This is the main entry point for the Black Oystercatcher data
management program. It creates the presentation layer Menu object
and starts the interactive menu loop.

References:
[1] Python Software Foundation. (2024). Modules. docs.python.org [Online]. 
Available: https://docs.python.org/3/tutorial/modules.html [Accessed: Feb. 15, 2026].
[2] Python Software Foundation. (2024). Sorting HOW TO. docs.python.org [Online].
Available: https://docs.python.org/3/howto/sorting.html [Accessed: Mar. 20, 2026].
[3] Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. matplotlib.org [Online].
Available: https://matplotlib.org/stable/index.html [Accessed: Apr. 5, 2026].
[4] Parks Canada. (2017, Oct. 1). Black Oystercatcher Population – Pacific Rim. open.canada.ca 
[Online]. Available: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02 
[Accessed: Apr. 12, 2026].
[5] Government of Canada. (2025). Open Government Licence – Canada. open.canada.ca [Online]. 
Available: https://open.canada.ca/en/open-government-licence-canada [Accessed: Apr. 12, 2026].
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
"""
This module prints a five-pointed star (pentagram) to the command line.
"""

def print_pentagram():
    """
    Prints an ASCII representation of a five-pointed star.
    """
    # A simple ASCII art pentagram
    pentagram = [
        "       *       ",
        "      * *      ",
        "     *   *     ",
        " * * * * * * * ",
        "  *         *  ",
        "   *       *   ",
        "  *   * *   *  ",
        " *   *   *   * ",
        "*   *     *   *"
    ]
    
    for line in pentagram:
        print(line)

if __name__ == "__main__":
    print_pentagram()

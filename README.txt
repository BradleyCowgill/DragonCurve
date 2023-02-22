# Dragon Curve Fractal Generator

This Python program generates and displays the nth iteration of the dragon curve fractal. The algorithm used is constructive on previous iterations, so while there may be faster ways to achieve the same final result, this program provides a unique and interesting method to create the fractal.

## What is the Dragon Curve?

The Dragon Curve is a mathematical fractal that is created from the simple act of repeatedly folding a piece of paper in half over itself. Each time the paper is folded in half (each iteration), the paper can be unraveled to see "peaks" and "valleys". From such a simple premise emerges a beautiful and seemingly chaotic pattern. This pattern is easiest to visualize when the fold crease angles are set to 90 degrees.

Please see Brady Haran and Rob Eastaway's video below to learn more about the Dragon Curve:

https://youtu.be/wCyC-K_PnRY 

## Getting Started

To run the program, simply clone the repository and run the code in Python. The following libraries are not included with Python and will need to be installed and imported when trying to run DragonCurve.py:

 - Numpy
 - Matplotlib

Alternatively, the DragonCurve.exe can be ran with no dependencies.

## Usage

Upon running the program, the user will be prompted to input an integer value for the desired iteration number. The program will then generate the fractal based on this input and display the resulting plot. The console will also output the peak and valley pattern in text format to the console window. When finished looking at the visualizations, the user can close the matplotlib window and press enter within the console window to end the program.

Note that for very large iteration numbers (greater than 18), processing times may be considerable on some computers due to the exponential nature of the fractal.

This program was coded with Python 3.11 (64-bit) and may have compatibility issues with older versions.

## Contributing

Contributions are welcome and encouraged. Please feel free to submit a pull request if you have suggestions for improving the code. Any questions can be sent to bradleyjcowgill@gmail.com
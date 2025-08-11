# Hacker Text
This simple Python sprogram simulates a hacker effect by cycling through a set of characters until it finds the correct one for each position in a target string. It's a fun way to display text as if it's being brought into existence by itself.

### How to use
1. Save the code
2. Open a terminal
3. Run the script
(pretty self explanatory)

## How to customise
to display a target message, simply change the string in line 8 (the variable 'target')

### Adjust animation speed
The speed of the animation is controlled by the 'time.sleep()' function on line 14. The number inside the function is the delay in seconds between each character. A Smaller number means faster animation.

#### To make animation faster you can change it to
time.sleep(0.0001)

#### To make animation slower, you can change it to
time.sleep(0.01)

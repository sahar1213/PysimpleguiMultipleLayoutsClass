# About this repository
## Multiple layouts on the same window?
Ever wanted to have a window that switches between multiple layouts, but couldn't find a way to apply this in pysimplegui? This class is a quick framework I made for this purpose.

# Guide to use
## How do I use this to create a window?
First, copy the class from the python file.

To create a window, the class takes 2 parameters:

```python
window = Window("Name Of The Program", [
  Layout1, 
  Layout2,
  Layout3
], UpperLayout, LowerLayout)
```

The name of the program, and layouts for each *'page'* of the window, which you can switch between. (you can enter as many layouts as you'd like)

UpperLayout and LowerLayout are optional, they stay displayed no matter which page you switch to, above the columns and below respectively. (look in the example file for an example of how this can be used)

## How do I use the window object created from this class?
There are some functions embedded in the class:

```python
event, values = window.read()
```
.read() - Reads the window like normal.

```python
window.e(Key).update(Properties)
```
.e(Key) - replaces the normal window[]. (same as the window.element() function used in the class)


```python
window.topage(int)
```
.topage(int) Switches to the page entered. (starts from 0)

```python
CurrentPage = window.page()
```
.page() - Outputs the current visible page. (starts from 0)

```python
window.close()
```
.close() - Closes the window.

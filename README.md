# Multiple layouts on the same window?
Ever wanted to have a window that switches between multiple layouts, but couldn't find a way to apply this in pysimplegui? This class is a quick framework I made for this purpose.

There is an example file to get a taste of what it does.

# How do I use this to create a window?
To create a window, the function takes 2 parameters:

```python
window = Window("Name Of The Program", [
  [LAYOUT1], 
  [LAYOUT2],
  [LAYOUT3]
])
```

The name of the program, and layouts for each *'page'* of the window, which you can switch between. (you can enter as many layouts as you'd like)

# How do I use the window object created from this class?
There are some functions embedded in the class:

```python
event, values = window.read()
```
.read() - Reads the window like normal.

```python
window.e(KEY).update(PROPERTIES)
```
.e(KEY) - replaces the normal window[]. (same as the window.element() function used in the class)

```python
window.topage(INT)
```
.topage(INT) Switches to the page entered. (starts from 0)

```python
CurrentPage = window.page()
```
.page() - Outputs the current visible page. (starts from 0)

```python
window.close()
```
.close() - Closes the window.

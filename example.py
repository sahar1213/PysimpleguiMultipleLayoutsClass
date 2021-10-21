import PySimpleGUI as sg

class Window:
  def __init__(self, Name, Layouts, UpperLayouts=[], LowerLayouts=[]): # (upper and lower layouts are always shown on-screen)
    columns = [] # a list for the columns

    for i in range(len(Layouts)): # loop over the layouts from parameters
      print("c" + str(i))
      if i == 0: # if its the first button, add it to the columns and make it visible
        columns.append(sg.Column(Layouts[i], visible=True, key="c" + str(i)))
      else: # if its not the first button, add it to the columns and make it invisible
        columns.append(sg.Column(Layouts[i], visible=False, key="c" + str(i)))
    
    layout = [UpperLayouts, columns, LowerLayouts] # add the columns to a layout

    window = sg.Window(Name, layout) # make a window with the layout

    def GetPage(): # function to get the current visible page
      for i in range(len(Layouts)): # loop over the layouts
        if window["c" + str(i)].visible: # check if column is visible
          return i #if visible return i
        
    def SwitchPage(Page):
      for i in range(len(Layouts)): # loop over the layouts
        if i == Page: # if its the wanted page, make it visible
          window["c" + str(i)].update(visible=True)
          print("y" + str(i))
        else: # if it isnt the wanted page, make it invisible
          window["c" + str(i)].update(visible=False)
          print("n" + str(i))

    # add functions to self
    self.read = window.read
    self.e = window.Element # window.e(KEY).Update(CHANGE PROPERTIES HERE)
    self.topage = SwitchPage
    self.page = GetPage
    self.close = window.close

# Example of a program using this class

window = Window("Example Program", [
  [
    [sg.Text('This is layout 1 - It is all Checkboxes')],
    *[[sg.CB(f'Checkbox {i}')] for i in range(5)],
  ],
  
  [
    [sg.Text('This is layout 2')],
    [sg.Input(key='-IN-')],
    [sg.Input(key='-IN2-')],
  ],

  [
    [sg.Text('This is layout 3 - It is all Radio Buttons')],
    *[[sg.Radio(f'Radio {i}', 1)] for i in range(8)],
  ]
], [], [
      sg.Button('1'),
      sg.Button('2'),
      sg.Button('3'),
      sg.Button('Exit')
])

while True:
    event, values = window.read() # read window
    
    if event == "Exit" or event == None: # stop program if user clicks exit or exits the program
      break
    else:
      try:
        layout = int(event) # try converting event to int (errors if its not int)
      except:
        print()
      
      if layout: # if its int
        window.topage(layout - 1) # switch to page on button

window.close()
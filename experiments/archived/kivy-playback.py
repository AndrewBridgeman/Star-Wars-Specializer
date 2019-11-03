# Program to learn how to make checkbox
# and adding callback in kivy

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# The :class:`Widget` class is the base class
# required for creating Widgets.
from kivy.uix.widget import Widget

# The Label widget is for rendering text.
from kivy.uix.label import Label

# To use the checkbox must import it from this module
from kivy.uix.checkbox import CheckBox

# The GridLayout arranges children in a matrix.
# imports the GridLayout class for use in the app.
from kivy.uix.gridlayout import GridLayout


# Container class for the app's widgets
class check_box(GridLayout):

    def __init__(self, **kwargs):
        # super function can be used to gain access
        # to inherited methods from a parent or sibling class
        # that has been overwritten in a class object.
        super(check_box, self).__init__(**kwargs)

        # 2 columns in grid layout
        self.cols = 2

        # Add checkbox, Label and Widget
        self.add_widget(Label(text='Male'))
        self.active = CheckBox(active=True)
        self.add_widget(self.active)

        # Adding label to scrren
        self.lbl_active = Label(text='Checkbox is on')
        self.add_widget(self.lbl_active)

        # Attach a callback
        self.active.bind(active=self.on_checkbox_Active)

        # Callback for the checkbox

    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active.text = "Checkbox is ON"
            print("Checkbox Checked")
        else:
            self.lbl_active.text = "Checkbox is OFF"
            print("Checkbox unchecked")

        # App derived from App class


class CheckBoxApp(App):
    def build(self):
        # build is a method of Kivy's App class used
        # to place widgets onto the GUI.
        return check_box()

    # Run the app


if __name__ == '__main__':
    CheckBoxApp().run() 
"""What this program does:
Creates a GUI application with tkinter
with an embedded 3d graph
that gets updated dynamically by the GUI buttons.
Arrows can be added to and removed from the graph.
Each step and exceptions are printed in console.
"""
from tkinter import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import randrange, choice
#hi how are u?
#hello
# can we put the figure on tkinter?
#wait.

class AppWindow(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.winfo_toplevel().title("Embedded 3D Graph in Tkinter GUI")
        self.master.protocol('WM_DELETE_WINDOW', self.close_app)

        # Control buttons
        self.navbar = Frame(self)
        self.navbar.pack(side=TOP)
        self.add_button = Button(self.navbar, text='Add Random Arrow', command=self.add_arrow)
        self.add_button.pack(side=LEFT)
        self.add_button = Button(self.navbar, text='Remove Random Arrow', command=self.remove_arrow)
        self.add_button.pack(side=LEFT)
        self.quit_button = Button(self.navbar, text='QUIT', command=self.close_app)
        self.quit_button.pack(side=LEFT)

        # Embedded matplotlib graph on the canvas
        self.graph = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.graph, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=1)
        self.ax = self.graph.add_subplot(111, projection='3d')
        self.ax.set_xlim([-9, 9])
        self.ax.set_ylim([-9, 9])
        self.ax.set_zlim([-9, 9])
        self.qarrow, self.qlabel = [], []  # placeholders for quiver arrows and labels
        self.colors = ['red', 'blue', 'purple', 'green', 'pink', 'gray', 'black']
        print("Graph is fully initialized.")

    def add_arrow(self):
        """Create a random quiver arrow"""
        rolls = [randrange(-9, 9) for _ in range(3)]
        color = choice(self.colors)
        self.qarrow.append(self.ax.quiver(0, 0, 0, *rolls, color=color))
        self.qlabel.append(self.ax.text(*rolls, str(len(self.qlabel)), fontsize=8, color=color))
        print("Creating a random arrow.")
        self.canvas.draw()

    def remove_arrow(self):
        """Remove a random quiver arrow from plot"""
        try:
            roll = randrange(0, len(self.qarrow))
            self.qarrow[roll].remove()
            self.qlabel[roll].remove()
            print("Removing a random arrow.")
            self.canvas.draw()
        except Exception as e:
            print("Remove failed, " + str(e))

    def close_app(self):
        """Safely close the program."""
        print("Quitting the program.")
        self.quit()
        self.master.destroy()

if __name__ == '__main__':
    root = Tk()
    AppWindow(root).pack()
    root.mainloop()
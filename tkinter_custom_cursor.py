"""Demonstration of Cursor Shapes in Tkinter
Custom Cursors downloaded from:
http://www.cursors-4u.com/cursor/2017/03/14/starfruit.html
http://www.cursors-4u.com/cursor/2014/03/05/minecraft-diamond-sword.html
The .cur files must be in the same directory as where the script is run.
.cur works only on Windows. Other operating units require different format.
"""
import tkinter as tk
from random import choice

class CursorDemo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.winfo_toplevel().title("Cursor Shapes Demo")
        self.pack()
        cursors = sorted("arrow man based_arrow_down middlebutton based_arrow_up mouse boat pencil bogosity pirate bottom_left_corner plus bottom_right_corner question_arrow bottom_side right_ptr bottom_tee right_side box_spiral right_tee center_ptr rightbutton circle rtl_logo clock sailboat coffee_mug sb_down_arrow cross sb_h_double_arrow cross_reverse sb_left_arrow crosshair sb_right_arrow diamond_cross sb_up_arrow dot sb_v_double_arrow dotbox shuttle double_arrow sizing draft_large spider draft_small spraycan draped_box star exchange target fleur tcross gobbler top_left_arrow gumby top_left_corner hand1 top_right_corner hand2 top_side heart top_tee icon trek iron_cross ul_angle left_ptr umbrella left_side ur_angle left_tee watch leftbutton xterm ll_angle X_cursor lr_angle".split())
        colors = sorted(["snow", "linen", "papaya whip", "mint cream", "azure", "lavender", "beige", "pink", "plum", "honeydew", "light steel blue", "light blue", "pale turquoise", "pale green", "tan", "thistle", "cornflower blue", "cyan", "aquamarine", "gold", "light goldenrod", "sandy brown", "salmon", "wheat", "tomato", "azure"])
        for i, cursor in enumerate(cursors):
            tk.Label(self, cursor=cursor, text=cursor, bg=choice(colors), relief=tk.RAISED, width=15, padx=15, pady=15).grid(row=(i//8), column=(i%8))
        tk.Label(self, cursor='none', text='No Cursor', bg=choice(colors), relief=tk.RAISED, padx=15, pady=15).grid(row=(len(cursors)//8+1), columnspan=8, sticky="ew")
        # This is where the custom cursor files are used
        try:
            tk.Label(self, cursor='@nat1059.cur', text='Starfruit (totally custom, downloaded from http://www.cursors-4u.com)', relief=tk.RAISED, padx=15, pady=15).grid(row=(len(cursors)//8+2), columnspan=8, sticky="ew")
            tk.Label(self, cursor='@gam1537x.cur', text='Diamond Sword (totally custom, downloaded from http://www.cursors-4u.com)', relief=tk.RAISED, padx=15, pady=15).grid(row=(len(cursors)//8+3), columnspan=8, sticky="ew")
        except tk.TclError:
            print("The cursor file was not found")

root = tk.Tk()
app = CursorDemo(master=root)
app.mainloop()

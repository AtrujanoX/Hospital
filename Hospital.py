from tkinter import *
from PIL import ImageTk, Image

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel(root)
    init(root, top)
    root.mainloop()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


w = None


class New_Toplevel:

    def __init__(self, top=None):
        top.geometry("480x320+0+0")
        top.title("Hospital")


        self.menuPrincipal(top)

    def clear(self, top):
        for wi in top.winfo_children():
            wi.destroy()

    def menuPrincipal(self,top):
        self.clear(top)
        self._img01 = ImageTk.PhotoImage(Image.open("images/menu_01.png"))
        self._img02 = ImageTk.PhotoImage(Image.open("images/menu_02.png"))
        self._img03 = ImageTk.PhotoImage(Image.open("images/menu_03.png"))
        self._img04 = ImageTk.PhotoImage(Image.open("images/menu_04.png"))
        self._img05 = ImageTk.PhotoImage(Image.open("images/menu_05.png"))
        self._img06 = ImageTk.PhotoImage(Image.open("images/menu_06.png"))
        self._img07 = ImageTk.PhotoImage(Image.open("images/menu_07.png"))
        self._img08 = ImageTk.PhotoImage(Image.open("images/p_08.png"))
        self._img09 = ImageTk.PhotoImage(Image.open("images/p_09.png"))
        self._img10 = ImageTk.PhotoImage(Image.open("images/p_10.png"))
        self._img11 = ImageTk.PhotoImage(Image.open("images/p_11.png"))
        self._img12 = ImageTk.PhotoImage(Image.open("images/p_12.png"))
        self._img13 = ImageTk.PhotoImage(Image.open("images/p_13.png"))
        self._img14 = ImageTk.PhotoImage(Image.open("images/p_14.png"))
        self._img15 = ImageTk.PhotoImage(Image.open("images/spacer08.png"))
        self._img16 = ImageTk.PhotoImage(Image.open("images/bot_01.png"))
        self._img17 = ImageTk.PhotoImage(Image.open("images/bot_02.png"))
        self._img18 = ImageTk.PhotoImage(Image.open("images/bot_03.png"))

        # Header
        self.img01 = Label(top, image=self._img01, borderwidth=0)
        # CoreButtons
        self.img02 = Button(top, image=self._img02, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.menuCocina(top))
        self.img03 = Label(top, image=self._img03, borderwidth=0)
        self.img04 = Button(top, image=self._img04, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.menuMedicamentos(top))
        self.img05 = Label(top, image=self._img05, borderwidth=0)
        self.img06 = Button(top, image=self._img06, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.menuCunero(top))

        self.img07 = Label(top, image=self._img07, borderwidth=0)

        self.img08 = Button(top, image=self._img08, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.menuTelevision(top))
        self.img09 = Label(top, image=self._img09, borderwidth=0)
        self.img10 = Button(top, image=self._img10, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.menuTelefono(top))
        self.img11 = Label(top, image=self._img11, borderwidth=0)
        self.img12 = Button(top, image=self._img12, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.menuPeliculas(top))
        self.img13 = Label(top, image=self._img13, borderwidth=0)
        self.img14 = Button(top, image=self._img14, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.lampara(top))

        self.img15 = Label(top, image=self._img15, borderwidth=0)  # ,compound=CENTER,text="asd")

        self.img16 = Button(top, image=self._img16, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.llamarEnfermera(top))
        self.img17 = Label(top, image=self._img17, borderwidth=0)
        self.img18 = Button(top, image=self._img18, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.alerta(top))

        self.img01.place(x=0, y=0)

        self.img02.place(x=0, y=7)
        self.img03.place(x=154, y=7)
        self.img04.place(x=166, y=7)
        self.img05.place(x=313, y=7)
        self.img06.place(x=324, y=7)

        self.img07.place(x=0, y=66)

        self.img08.place(x=0, y=99)
        self.img09.place(x=114, y=99)
        self.img10.place(x=130, y=99)
        self.img11.place(x=235, y=99)
        self.img12.place(x=249, y=99)
        self.img13.place(x=354, y=99)
        self.img14.place(x=367, y=99)

        self.img15.place(x=0, y=154)

        self.img16.place(x=0, y=191)
        self.img17.place(x=130, y=191)
        self.img18.place(x=354, y=191)

    def menuCocina(self, top):
        self.clear(top)

        self._img02 = ImageTk.PhotoImage(Image.open("images/com_02.png"))
        self._img03 = ImageTk.PhotoImage(Image.open("images/com_03.png"))
        self._img04 = ImageTk.PhotoImage(Image.open("images/com_04.png"))
        self._img05 = ImageTk.PhotoImage(Image.open("images/com_05.png"))
        self._img06 = ImageTk.PhotoImage(Image.open("images/com_06.png"))

        self.img02 = Label(top, image=self._img02, borderwidth=0) # espaciadorV
        self.img03 = Button(top, image=self._img03, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0", command=lambda: self.menuPrincipal(top))
        self.img04 = Label(top, image=self._img04, borderwidth=0) # espaciadorH
        self.img05 = Label(top, image=self._img05, borderwidth=0) # info
        self.img06 = Label(top, image=self._img06, borderwidth=0) # espaciadorH

        self.img02.place(x=0, y=7)
        self.img03.place(x=7, y=7)
        self.img04.place(x=154, y=7)
        self.img05.place(x=0, y=66)
        self.img06.place(x=0, y=78)

        self.menuComun(top)


    def menuMedicamentos(self, top):
        self.clear(top)

        self._img02 = ImageTk.PhotoImage(Image.open("images/med_02.png"))
        self._img03 = ImageTk.PhotoImage(Image.open("images/med_03.png"))
        self._img04 = ImageTk.PhotoImage(Image.open("images/med_04.png"))
        self._img05 = ImageTk.PhotoImage(Image.open("images/med_05.png"))
        self._img06 = ImageTk.PhotoImage(Image.open("images/med_06.png"))

        self.img02 = Label(top, image=self._img02, borderwidth=0) # espaciadorV
        self.img03 = Button(top, image=self._img03, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.menuPrincipal(top))
        self.img04 = Label(top, image=self._img04, borderwidth=0) # espaciadorH
        self.img05 = Label(top, image=self._img05, borderwidth=0) # info
        self.img06 = Label(top, image=self._img06, borderwidth=0) # espaciadorH

        self.img02.place(x=0, y=7)
        self.img03.place(x=7, y=7)
        self.img04.place(x=154, y=7)
        self.img05.place(x=0, y=66)
        self.img06.place(x=0, y=78)

        self.menuComun(top)


    def menuCunero(self, top):
        self.clear(top)

        self._img02 = ImageTk.PhotoImage(Image.open("images/cun_02.png"))
        self._img03 = ImageTk.PhotoImage(Image.open("images/cun_03.png"))
        self._img04 = ImageTk.PhotoImage(Image.open("images/cun_04.png"))
        self._img05 = ImageTk.PhotoImage(Image.open("images/cun_05.png"))
        self._img06 = ImageTk.PhotoImage(Image.open("images/cun_06.png"))

        self.img02 = Label(top, image=self._img02, borderwidth=0)  # espaciadorV
        self.img03 = Button(top, image=self._img03, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.menuPrincipal(top))
        self.img04 = Label(top, image=self._img04, borderwidth=0)  # espaciadorH
        self.img05 = Label(top, image=self._img05, borderwidth=0)  # info
        self.img06 = Label(top, image=self._img06, borderwidth=0)  # espaciadorH

        self.img02.place(x=0, y=7)
        self.img03.place(x=7, y=7)
        self.img04.place(x=154, y=7)
        self.img05.place(x=0, y=66)
        self.img06.place(x=0, y=78)

        self.menuComun(top)

    def menuComun(self,top):
        self.img01 = Label(top, image=self._img01, borderwidth=0)
        self._img07 = ImageTk.PhotoImage(Image.open("images/com_07.png"))
        self._img16 = ImageTk.PhotoImage(Image.open("images/bot_01.png"))
        self._img17 = ImageTk.PhotoImage(Image.open("images/bot_02.png"))
        self._img18 = ImageTk.PhotoImage(Image.open("images/bot_03.png"))
        self.img07 = Label(top, image=self._img07, borderwidth=0)
        self.img16 = Button(top, image=self._img16, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.llamarEnfermera(top))
        self.img17 = Label(top, image=self._img17, borderwidth=0)
        self.img18 = Button(top, image=self._img18, borderwidth=0, highlightthickness=0, activebackground="#A0A0A0",
                            command=lambda: self.alerta(top))
        self.img01.place(x=0, y=0)
        self.img07.place(x=0, y=186)
        self.img16.place(x=0, y=191)
        self.img17.place(x=130, y=191)
        self.img18.place(x=354, y=191)



    def menuTelevision(self, top):
        return

    def menuTelefono(self, top):
        return

    def menuPeliculas(self, top):
        return

    def lampara(self,top):
        return

    def llamarEnfermera(self, top):
        return

    def alerta(self, top):
        return



if __name__ == '__main__':
    vp_start_gui()

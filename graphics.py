from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Mazer")
        self.__canvas = Canvas(self.__root,
                               background="cyan",
                               width=self.width,
                               height=self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True

        while self.__is_running:
            self.redraw()
        print("Closing window.")

    def close(self):
        self.__is_running = False

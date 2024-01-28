from tkinter import Tk, BOTH, Canvas


class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str = "black"):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2
        )
        canvas.pack(fill=BOTH, expand=1)


class Window:

    def __init__(self, width: float, height: float):
        self.__root = Tk()
        self.__root.title("Mazer")
        self.__canvas = Canvas(self.__root,
                               background="cyan",
                               width=width,
                               height=height)
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

    def draw_line(self, line: Line, fill_color: str = "black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__is_running = False

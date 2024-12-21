#COPYRIGHT (C) Haoriwa 2022-2024 All rights reserved.
# license under the MIT license.
#see LICENSE.txt for more info.
import tkinter as tk
import sys
from time import *
from ctypes import windll

class TiDraw:
    
    def __init__(self, width=400, height=400, bg="white"):
        self.width = width
        self.height = height
        self.bg = bg
        self.color = "black"
        self.pen_style = (1, "solid")
        self.root = tk.Tk()
        self.root.title("ESTT")
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg=self.bg)
        self.canvas.pack()

    def set_color(self, r, g, b):
        """设置绘图颜色，参数为RGB值 (0-255)"""
        self.color = f"#{r:02x}{g:02x}{b:02x}"

    def set_window(self, width, height, title="ESTT"):
        """设置窗口宽度、高度和标题"""
        self.width = width
        self.height = height
        self.root.title(title)
        self.canvas.config(width=self.width, height=self.height)

    def set_pen(self, thickness=1, style="solid"):
        """设置画笔样式，参数为厚度(thickness)和线条样式(style)"""
        if isinstance(thickness, str):
            thickness_map = {"thin": 1, "medium": 2, "thick": 4}
            thickness = thickness_map.get(thickness, 1)
        self.pen_style = (thickness, style)

    def draw_line(self, x1, y1, x2, y2):
        """绘制一条从(x1, y1)到(x2, y2)的直线"""
        dash = None
        if self.pen_style[1] == "dashed":
            dash = (5, 5)
        elif self.pen_style[1] == "dotted":
            dash = (2, 2)
        self.canvas.create_line(x1, y1, x2, y2, fill=self.color, width=self.pen_style[0], dash=dash)

    def draw_rect(self, x, y, width, height):
        """绘制矩形，左上角为(x, y)，宽度为width，高度为height"""
        self.canvas.create_rectangle(x, y, x + width, y + height, outline=self.color, width=self.pen_style[0])

    def fill_rect(self, x, y, width, height):
        """填充矩形，左上角为(x, y)，宽度为width，高度为height"""
        self.canvas.create_rectangle(x, y, x + width, y + height, fill=self.color, outline=self.color)

    def draw_circle(self, x, y, radius):
        """绘制圆形，圆心为(x, y)，半径为radius"""
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=self.color, width=self.pen_style[0])

    def fill_circle(self, x, y, radius):
        """填充圆形，圆心为(x, y)，半径为radius"""
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=self.color, outline=self.color)

    def draw_arc(self, x, y, width, height, start, extent):
        """绘制圆弧，指定位置(x, y)，宽度，高度，起始角度和角度范围"""
        self.canvas.create_arc(x, y, x + width, y + height, start=start, extent=extent, outline=self.color, style=tk.ARC, width=self.pen_style[0])

    def fill_arc(self, x, y, width, height, start, extent):
        """填充圆弧，指定位置(x, y)，宽度，高度，起始角度和角度范围"""
        self.canvas.create_arc(x, y, x + width, y + height, start=start, extent=extent, fill=self.color, outline=self.color)

    def draw_poly(self, points):
        """绘制多边形，points为点的列表 [(x1, y1), (x2, y2), ...]"""
        transformed_points = []
        for x, y in points:
            transformed_points.append(x)
            transformed_points.append(y)
        self.canvas.create_polygon(transformed_points, outline=self.color, fill="", width=self.pen_style[0])

    def fill_poly(self, points):
        """填充多边形，points为点的列表 [(x1, y1), (x2, y2), ...]"""
        transformed_points = []
        for x, y in points:
            transformed_points.append(x)
            transformed_points.append(y)
        self.canvas.create_polygon(transformed_points, fill=self.color, outline=self.color)

    def plot_xy(self, x, y):
        """绘制单个像素点(x, y)"""
        self.canvas.create_line(x, y, x + 1, y, fill=self.color)

    def draw_text(self, x, y, text):
        """在指定位置(x, y)显示文本"""
        self.canvas.create_text(x, y, text=text, fill=self.color)

    def clear(self):
        """清空画布"""
        self.canvas.delete("all")

    def run(self):
        """运行主循环"""
        self.root.mainloop()
# 全局默认实例
__app = TiDraw()

def set_color(r, g, b):
    __app.set_color(r, g, b)

def set_window(width, height, title="ESTT"):
    __app.set_window(width, height, title)

def set_pen(thickness=1, style="solid"):
    __app.set_pen(thickness, style)

def draw_line(x1, y1, x2, y2):
    __app.draw_line(x1, y1, x2, y2)

def draw_rect(x, y, width, height):
    __app.draw_rect(x, y, width, height)

def fill_rect(x, y, width, height):
    __app.fill_rect(x, y, width, height)

def draw_circle(x, y, radius):
    __app.draw_circle(x, y, radius)

def fill_circle(x, y, radius):
    __app.fill_circle(x, y, radius)

def draw_arc(x, y, width, height, start, extent):
    __app.draw_arc(x, y, width, height, start, extent)

def fill_arc(x, y, width, height, start, extent):
    __app.fill_arc(x, y, width, height, start, extent)

def draw_poly(points):
    __app.draw_poly(points)

def fill_poly(points):
    __app.fill_poly(points)

def plot_xy(x, y):
    __app.plot_xy(x, y)

def draw_text(x, y, text):
    __app.draw_text(x, y, text)

def clear():
    __app.clear()

def run():
    __app.run()
# 如果直接运行脚本
if __name__ == "__main__":
    if len(sys.argv) > 1:  # 支持从文件加载绘图脚本
        script = sys.argv[1]
        exec(open(script).read(), globals())
        run()
    else:
        # 示例代码
        set_window(600, 550, "ESTT")

        set_color(255, 0, 0)
        set_pen(3, "dashed")
        draw_line(50, 50, 200, 200)

        set_pen("medium", "solid")
        draw_rect(100, 100, 150, 100)
        fill_rect(300, 50, 100, 100)

        set_pen("thick", "dotted")
        draw_circle(300, 200, 50)
        fill_circle(500, 200, 50)

        draw_poly([(400, 300), (450, 350), (350, 350)])
        fill_poly([(200, 300), (250, 350), (150, 350)])

        plot_xy(100, 100)
        draw_text(150, 50, "Hello, EasyTurtle!")
        set_color(0, 255, 0)
        set_pen(2, "solid")
        draw_arc(50, 250, 100, 100, 0, 180)

        set_color(0, 0, 255)
        set_pen(1, "dotted")
        draw_poly([(200, 250), (250, 300), (200, 350), (150, 300)])

        set_color(255, 255, 0)
        set_pen(3, "solid")
        fill_rect(350, 250, 50, 50)

        set_color(255, 0, 255)
        set_pen(2, "dashed")
        draw_circle(400, 300, 25)

        set_color(0, 255, 255)
        set_pen(1, "solid")
        draw_text(450, 250, "Graphics Example")

        set_color(128, 128, 128)
        set_pen(2, "solid")
        fill_poly([(500, 250), (550, 300), (500, 350), (450, 300)])
        clear()
        set_color(255, 0, 0)
        set_pen(3, "dashed")
        draw_line(50, 50, 200, 200)

        set_pen("medium", "solid")
        draw_rect(100, 100, 150, 100)
        fill_rect(300, 50, 100, 100)

        set_pen("thick", "dotted")
        draw_circle(300, 200, 50)
        fill_circle(500, 200, 50)

        draw_poly([(400, 300), (450, 350), (350, 350)])
        fill_poly([(200, 300), (250, 350), (150, 350)])

        plot_xy(100, 100)
        draw_text(150, 50, "Hello, EasyTurtle!")
        set_color(0, 255, 0)
        set_pen(2, "solid")
        draw_arc(50, 250, 100, 100, 0, 180)

        set_color(0, 0, 255)
        set_pen(1, "dotted")
        draw_poly([(200, 250), (250, 300), (200, 350), (150, 300)])

        set_color(255, 255, 0)
        set_pen(3, "solid")
        fill_rect(350, 250, 50, 50)

        set_color(255, 0, 255)
        set_pen(2, "dashed")
        draw_circle(400, 300, 25)

        set_color(0, 255, 255)
        set_pen(1, "solid")
        draw_text(450, 250, "Graphics Example")

        set_color(128, 128, 128)
        set_pen(2, "solid")
        fill_poly([(500, 250), (550, 300), (500, 350), (450, 300)])

        set_color(255, 0, 0)
        set_pen(1, "solid")
        draw_text(100, 300, "Beautiful Graphics")

        set_color(0, 255, 0)
        set_pen(2, "dashed")
        draw_line(100, 350, 200, 400)

        set_color(0, 0, 255)
        set_pen(3, "solid")
        draw_circle(300, 400, 50)

        set_color(255, 255, 0)
        set_pen(1, "dotted")
        draw_poly([(400, 400), (450, 450), (350, 450)])

        set_color(255, 0, 255)
        set_pen(2, "solid")
        fill_rect(500, 400, 50, 50)

        set_color(0, 255, 255)
        set_pen(1, "solid")
        draw_text(550, 400, "More Graphics")

        set_color(128, 128, 128)
        set_pen(2, "dashed")
        fill_poly([(100, 450), (150, 500), (100, 550), (50, 500)])

        set_color(255, 0, 0)
        set_pen(3, "solid")
        draw_arc(200, 450, 100, 100, 0, 180)

        set_color(0, 255, 0)
        set_pen(1, "solid")
        draw_poly([(300, 450), (350, 500), (300, 550), (250, 500)])

        set_color(0, 0, 255)
        set_pen(2, "dotted")
        fill_rect(400, 450, 50, 50)

        set_color(255, 255, 0)
        set_pen(1, "solid")
        draw_text(450, 450, "Even More Graphics")

        set_color(255, 0, 255)
        set_pen(2, "dashed")
        draw_circle(500, 500, 25)

        set_color(0, 255, 255)
        set_pen(1, "solid")
        draw_text(550, 500, "The End")
        run()
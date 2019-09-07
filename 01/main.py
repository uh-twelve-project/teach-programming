#!/usr/bin/env python3

from turtle import *
from math import *

from cmd import Cmd


class cmd(Cmd):
    intro = '''Bienvenido a la primera clase de programación!
Escribe help o ? para obtener la lista de comandos que puedes escribir.
'''
    prompt = '(cmd) '

    def __init__(self):
        super(cmd, self).__init__()
        self.trtl = Turtle()
        self.screen = Screen()
        self.screen.setworldcoordinates(0, 0, 500, 500)

    def do_set(self, line):
        """\
Configurar los valores de ángulo y velocidad.
La sintaxis es:
    set <ángulo> <fuerza>"""
        a, f = map(float, line.split())
        self.angle = a
        self.force = f
        self._redraw()

    def _redraw(self):
        self.trtl.clear()

        t = 0
        xk, yk = 0, 0
        v, a = self.force, radians(self.angle)

        self.trtl.speed('fastest')
        self.trtl.penup()
        self.trtl.goto((0, 0))
        self.trtl.pendown()
        self.trtl.speed('normal')

        while yk >= 0:
            xk = v * t * cos(a)
            yk = v * t * sin(a) - 1/2 * 9.8 * t**2
            self.trtl.goto((xk, yk))
            print(self.trtl.pos())
            t += 0.1

    def do_EOF(self, line):
        print('^D')
        return True


def main():
    cmd().cmdloop()


if __name__ == "__main__":
    main()

#Cristopher jose Rodolfo Barrios Solis
#SR3
import struct
from obj import Obj
import random
from collections import namedtuple

def char(c):
		return struct.pack('=c', c.encode('ascii'))

def word(c):
	return struct.pack('=h', c)

def dword(c):
	return struct.pack('=l', c)

def normalizeColorArray(colors_array):
    return [round(i*255) for i in colors_array]

def color(r,g,b):
	return bytes([b, g, r])

class Render(object):
    def __init__(self):
        self.framebuffer = []
        self.width = 400
        self.height = 500
        self.viewport_x = 0
        self.viewport_y = 0
        self.viewport_width = 1200
        self.viewport_height = 1200
        self.glClear()

    def glInit(self):
        return "Generando...\n"

    def glClear(self):
        BLACK = color(0,0,0)
        self.framebuffer = [
            [BLACK for x in range(self.width)] for y in range(self.height)
        ]
    def glCreateWindow(self, width, height):
        self.height = height
        self.width = width

    def glClearColor(self, r=1, g=1, b=1):

        normalized = normalizeColorArray([r,g,b])
        clearColor = color(normalized[0], normalized[1], normalized[2])

        self.framebuffer = [
            [clearColor for x in range(self.width)] for y in range(self.height)
        ]

    def glColor(self, r=0, g=0, b=0):
        normalized = normalizeColorArray([r,g,b])
        self.color = color(normalized[0], normalized[1], normalized[2])

    def glViewport(self, x, y, width, height):

        self.viewport_x = x
        self.viewport_y = y
        self.viewport_height = height
        self.viewport_width = width

    def point(self, x, y, color):
        self.framebuffer[y][x] = color

    def glVertex(self, x, y):
        final_x = round((x+1) * (self.viewport_width/2) + self.viewport_x)
        final_y = round((y+1) * (self.viewport_height/2) + self.viewport_y)
        self.point(final_x, final_y, self.color)

    def glCord(self, value, is_vertical):
        real_coordinate = ((value+1) * (self.viewport_height/2) + self.viewport_y) if is_vertical else ((value+1) * (self.viewport_width/2) + self.viewport_x)
        return round(real_coordinate)


    def glLine(self, A, B, C, color=None):
        if A.y > B.y:
            A, B = B, A
        if A.y > C.y:
            A, C = C, A
        if B.y > C.y:
            B, C = C, B

        dx_ac = C.x - A.x
        dy_ac = C.y - A.y

        if dy_ac == 0:
            return

        mi_ac = dx_ac/dy_ac

        dx_ab = B.x - A.x
        dy_ab = B.y - A.y

        if dy_ab != 0:
            mi_ab = dx_ab/dy_ab

            for y in range(A.y, B.y + 1):
                xi = round(A.x - mi_ac * (A.y - y))
                xf = round(A.x - mi_ab * (A.y - y))

                if xi > xf:
                    xi, xf = xf, xi
                for x in range(xi, xf + 1):
                    self.point(x, y, color)

        dx_bc = C.x - B.x
        dy_bc = C.y - B.y

        if dy_bc:

            mi_bc = dx_bc/dy_bc

            for y in range(B.y, C.y + 1):
                xi = round(A.x - mi_ac * (A.y - y))
                xf = round(B.x - mi_bc * (B.y - y))

                if xi > xf:
                    xi, xf = xf, xi
                for x in range(xi, xf + 1):
                    self.point(x, y, color)


 
    def glLoad(self, filename='default.obj', tras=[0,0], size=[1,1]):
        model = Obj(filename)

        for face in model.faces:
            vcount = len(face)

            if vcount == 3:
                face1 = face[0][0] - 1
                face2 = face[1][0] - 1
                face3 = face[2][0] - 1

                v1 = model.vertices[face1]
                v2 = model.vertices[face2]
                v3 = model.vertices[face3]

                x1 = round((v1[0] * size[0]) + tras[0])
                y1 = round((v1[1] * size[1]) + tras[1])
                z1 = round((v1[2] * size[2]) + tras[2])

                x2 = round((v2[0] * size[0]) + tras[0])
                y2 = round((v2[1] * size[1]) + tras[1])
                z2 = round((v2[2] * size[2]) + tras[2])

                x3 = round((v3[0] * size[0]) + tras[0])
                y3 = round((v3[1] * size[1]) + tras[1])
                z3 = round((v3[2] * size[2]) + tras[2])

                a = V3(x1, y1, z1)
                b = V3(x2, y2, z2)
                c = V3(x3, y3, z3)

                self.glLine(a, b, c,
                    color(
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255)
                    )
                )

            else:
                face1 = face[0][0] - 1
                face2 = face[1][0] - 1
                face3 = face[2][0] - 1
                face4 = face[3][0] - 1

                v1 = model.vertices[face1]
                v2 = model.vertices[face2]
                v3 = model.vertices[face3]
                v4 = model.vertices[face4]

                x1 = round((v1[0] * size[0]) + tras[0])
                y1 = round((v1[1] * size[1]) + tras[1])
                z1 = round((v1[2] * size[2]) + tras[2])

                x2 = round((v2[0] * size[0]) + tras[0])
                y2 = round((v2[1] * size[1]) + tras[1])
                z2 = round((v2[2] * size[2]) + tras[2])

                x3 = round((v3[0] * size[0]) + tras[0])
                y3 = round((v3[1] * size[1]) + tras[1])
                z3 = round((v3[2] * size[2]) + tras[2])

                x4 = round((v4[0] * size[0]) + tras[0])
                y4 = round((v4[1] * size[1]) + tras[1])
                z4 = round((v4[2] * size[2]) + tras[2])

                a = V3(x1, y1, z1)
                b = V3(x2, y2, z2)
                c = V3(x3, y3, z3)
                d = V3(x4, y4, z4)

                self.glLine(a, b, c,
                    color(
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255)
                    )
                )
                self.glLine(a, c, d,
                    color(
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255)
                    )
                )



    def glFinish(self, filename='out.bmp'):
        f = open(filename, 'bw')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        try:
            for x in range(self.height):
                for y in range(self.width):
                    f.write(self.framebuffer[x][y])
        except:
            print('Prueba con otro obj')

        f.close()


V2 = namedtuple('Verx2', ['x', 'y'])
V3 = namedtuple('Verx3', ['x', 'y', 'z'])
bitmap = Render()
print(bitmap.glInit())
bitmap.glColor(0.46, 0.255, 0.00)
bitmap.glLoad('./pengin.obj', tras=(200, 300, 0), size = (20, 20, 20))
bitmap.glFinish()
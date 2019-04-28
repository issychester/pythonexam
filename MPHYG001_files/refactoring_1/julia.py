from numpy import *
import matplotlib.pyplot as plt

#xsize = 100
#ysize = 100
#xspread = 1.5
#yspread = 1
#zoom = 0.5
#density=255
#A = zeros([xsize,ysize])

from argparse import ArgumentParser

def spread(directionspread, direction, size, zoom):
    output = directionspread*(direction-size/2)/(zoom*size)
    return output

def array(density, zx, zy, x, y, A):
    for density in range(density, -1, -1):
            if (zx**2)+(zy**2)>=4 or density<=1:
                break
            a=zx*zx-zy*zy-0.7
            zy=2.0*zx*zy+0.27015
            zx=a
    A[y][x]=density
    return A

def plot(A):
    plt.imshow(A)
    #plt.show()
    plt.savefig('julia.png')

def image(xsize, ysize, density, xspread, yspread, zoom):
    A = zeros([xsize,ysize])
    for x in range(ysize):
        for y in range(xsize):
            zx=spread(xspread, x, ysize, zoom)
            zy=spread(yspread, y, xsize, zoom)
            B = array(density, zx, zy, x, y, A)
    plot(B)
    
if __name__ == "__main__":
    parser = ArgumentParser(description='Plot graph')
    parser.add_argument('--xsize', '-x')
    parser.add_argument('--ysize', '-y')
    parser.add_argument('--xspread', '-xspread')
    parser.add_argument('--yspread', '-yspread')
    parser.add_argument('--zoom', '-z')
    parser.add_argument('--density', '-d')
    args = parser.parse_args()
    
    image(int(args.xsize), int(args.ysize), int(args.density), float(args.xspread), float(args.yspread), float(args.zoom))
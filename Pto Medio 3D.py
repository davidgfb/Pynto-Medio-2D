from pygame import init, QUIT, quit
from pygame.display import set_mode
from pygame.event import get
from pygame.display import flip
from pygame.time import wait

from OpenGL.GL import glClearColor, glClear, glMaterialfv,\
     GL_FRONT, GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, glMateriali,\
     GL_SHININESS, glPushMatrix, glTranslatef, glRotatef,\
     glScalef, glPopMatrix
from OpenGL.GLU import gluPerspective, gluLookAt
from OpenGL.GLUT import glutInit, glutSolidCube

from numpy import array

ptos_Linea, pos_Elem = [(0,) * 3, (4,) * 3], 0



def pp(met):
    glPushMatrix()
    met()
    glPopMatrix()

def draw_gun():
    # Setting up materials, ambient, diffuse, specular and shininess properties are all
    # different properties of how a material will react in low/high/direct light for
    # example.
    ambient_coeffsGray, diffuse_coeffsGray, specular_coeffsGray =\
                        (*(0.3,) * 3, 1), (*(0.5,) * 3, 1),\
                        (*(0,) * 3, 1)

    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient_coeffsGray)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse_coeffsGray)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular_coeffsGray)
    glMateriali(GL_FRONT, GL_SHININESS, 1)

    # OpenGL is very finicky when it comes to transformations, for all of them are global,
    # so it's good to seperate the transformations which are used to generate the object
    # from the actual global transformations like animation, movement and such.
    # The glPushMatrix() ----code----- glPopMatrix() just means that the code in between
    # these two functions calls is isolated from the rest of your project.
    # Even inside this push-pop (pp for short) block, we can use nested pp blocks,
    # which are used to further isolate code in it's entirety.
    glPushMatrix()

    for pto_Linea in ptos_Linea:
        x, y, z = pto_Linea

        pp(lambda : (glTranslatef(x, y, z), glutSolidCube(1)))
  
    glPopMatrix()

while pos_Elem + 1 < len(ptos_Linea):
    p_0, p_F = ptos_Linea[pos_Elem : pos_Elem + 2]
    ptoMedio = tuple((array(p_0) + array(p_F)) // 2)
 
    if ptoMedio in ptos_Linea:
        pos_Elem += 1
            
    else:
        ptos_Linea.insert(pos_Elem + 1, ptoMedio) #list.insert()








# Initialization of PyGame modules
init()
# Initialization of Glut library
glutInit()
# Setting up the viewport, camera, backgroud and display mode
display = (1280, 720)

set_mode(display, 1073741826)
glClearColor(*(0.1,) * 3, 0.3) 

an, al = display

gluPerspective(60, an / al, 0.1, 50) #fov, ar, zn, zf
gluLookAt(*(*(5,) * 2, 0), *(0,) * 3, *(*(0,) * 2, 1)) #rot

esta_Func = True

while esta_Func:
    # Clears the screen for the next frame to be drawn over
    glClear(16640)
    ############## INSERT CODE FOR GENERATING OBJECTS ##################
    draw_gun()
    ####################################################################
    # Function used to advance to the next frame essentially
    flip()
    wait(10) #ms 90fps

    # Listener for exit command
    for event in get():
        if event.type == QUIT:
            esta_Func = False
            quit()

import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1; width = 1; height = 1
x = 0; y = 0; z = .5
cubesx = 0
cubesy = 0
while cubesy < 5:
    y += 1
    while cubesx < 5:
        x += 1
        for c in range(9):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            z+=1
            length = length * .9
            width = width * .9
            height = height * .9
        length = 1; width = 1; height = 1
        cubesx += 1
    cubesy += 1
    cubesx = 0
    x = 0

pyrosim.End()

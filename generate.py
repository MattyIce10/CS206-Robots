import pyrosim.pyrosim as pyrosim

length = 1; width = 1; height = 1


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    x = -2; y = 2; z = .5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])           
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    x = 1.5; y = 0; z = 3.5
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,3])
    x = -.5; y = 0; z = -.5
    pyrosim.Send_Cube(name="BackLeg", pos=[x,y,z] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1,0,0])
    x = .5; y = 0; z = -.5
    pyrosim.Send_Cube(name="FrontLeg", pos=[x,y,z] , size=[length,width,height])
   
    pyrosim.End()

Create_World()
Create_Robot()

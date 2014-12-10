import time,mcpi.minecraft as minecraft #
mc = minecraft.Minecraft.create() #

#Tells the player the program is running
mc.postToChat("Program running")

#Gets the players position and sets their coordinates to x,y,z
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def si(x,y,z):
    #Space Invader Part 1

    #Main Body
    mc.setBlocks(x+1,y+6,z+10,x-1,y+3,z+10,35,5)

    #Bottom Legs
    mc.setBlocks(x+1,y+1,z+10,x+2,y+1,z+10,35,5)
    mc.setBlocks(x-1,y+1,z+10,x-2,y+1,z+10,35,5)
    #NOT SURE
    mc.setBlocks(x+3,y+2,z+10,x+3,y+6,z+10,35,5)
    mc.setBlocks(x-3,y+2,z+10,x-3,y+6,z+10,35,5)
    mc.setBlocks(x-2,y+3,z+10,x-2,y+4,z+10,35,5)
    mc.setBlocks(x-2,y+6,z+10,x-2,y+7,z+10,35,5)

    #Arms
    mc.setBlocks(x+2,y+3,z+10,x+2,y+4,z+10,35,5)
    mc.setBlocks(x+2,y+6,z+10,x+2,y+7,z+10,35,5)

    #Ears of the Space Invader
    mc.setBlock(x+3,y+8,z+10,35,5)
    mc.setBlock(x-3,y+8,z+10,35,5)

    mc.setBlocks(x-4,y+5,z+10,x-4,y+4,z+10,35,5)
    mc.setBlocks(x+4,y+5,z+10,x+4,y+4,z+10,35,5)
    mc.setBlocks(x+5,y+2,z+10,x+5,y+4,z+10,35,5)
    mc.setBlocks(x-5,y+2,z+10,x-5,y+4,z+10,35,5)

def si2(x,y,z):
    #Space Invader Part 2

    #Main Body
    mc.setBlocks(x+1,y+6,z+10,x-1,y+3,z+10,35,4)

    #Bottom Legs
    mc.setBlocks(x+1,y+1,z+10,x+2,y+1,z+10,0)
    mc.setBlocks(x-1,y+1,z+10,x-2,y+1,z+10,0)

    mc.setBlocks(x+3,y+1,z+10,x+4,y+1,z+10,35,4)
    mc.setBlocks(x-3,y+1,z+10,x-4,y+1,z+10,35,4)

    #NOT SURE
    mc.setBlocks(x+3,y+2,z+10,x+3,y+6,z+10,35,4)
    mc.setBlocks(x-3,y+2,z+10,x-3,y+6,z+10,35,4)
    mc.setBlocks(x-2,y+3,z+10,x-2,y+4,z+10,35,4)
    mc.setBlocks(x-2,y+6,z+10,x-2,y+7,z+10,35,4)

    #Arms
    mc.setBlocks(x+2,y+3,z+10,x+2,y+4,z+10,35,4)
    mc.setBlocks(x+2,y+6,z+10,x+2,y+7,z+10,35,4)

    #Ears of the Space Invader
    mc.setBlock(x+3,y+8,z+10,35,4)
    mc.setBlock(x-3,y+8,z+10,35,4)

    mc.setBlocks(x-4,y+5,z+10,x-4,y+4,z+10,35,4)
    mc.setBlocks(x+4,y+5,z+10,x+4,y+4,z+10,35,4)
    mc.setBlocks(x+5,y+2,z+10,x+5,y+4,z+10,35,4)
    mc.setBlocks(x-5,y+2,z+10,x-5,y+4,z+10,35,4)

def si3(x,y,z):
    #Space Invader Part 3

    #Main Body
    mc.setBlocks(x+1,y+6,z+10,x-1,y+3,z+10,35,6)

    #Bottom Legs
    mc.setBlocks(x+3,y+1,z+10,x+4,y+1,z+10,0)
    mc.setBlocks(x-3,y+1,z+10,x-4,y+1,z+10,0)

    mc.setBlocks(x+1,y+1,z+10,x+2,y+1,z+10,35,6)
    mc.setBlocks(x-1,y+1,z+10,x-2,y+1,z+10,35,6)

    #NOT SURE
    mc.setBlocks(x+3,y+2,z+10,x+3,y+6,z+10,35,6)
    mc.setBlocks(x-3,y+2,z+10,x-3,y+6,z+10,35,6)
    mc.setBlocks(x-2,y+3,z+10,x-2,y+4,z+10,35,6)
    mc.setBlocks(x-2,y+6,z+10,x-2,y+7,z+10,35,6)

    #Arms
    mc.setBlocks(x+2,y+3,z+10,x+2,y+4,z+10,35,6)
    mc.setBlocks(x+2,y+6,z+10,x+2,y+7,z+10,35,6)

    #Ears of the Space Invader
    mc.setBlock(x+3,y+8,z+10,35,6)
    mc.setBlock(x-3,y+8,z+10,35,6)

    mc.setBlocks(x-4,y+5,z+10,x-4,y+4,z+10,35,6)
    mc.setBlocks(x+4,y+5,z+10,x+4,y+4,z+10,35,6)
    mc.setBlocks(x+5,y+2,z+10,x+5,y+4,z+10,35,6)
    mc.setBlocks(x-5,y+2,z+10,x-5,y+4,z+10,35,6)
    
    

while True:

    time.sleep(1)

    si(x,y,z)

    time.sleep(1)

    si2(x,y,z)

    time.sleep(1)

    si3(x,y,z)
    
    time.sleep(0.5)





    

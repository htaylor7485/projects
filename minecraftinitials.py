import time,mcpi.minecraft as minecraft #
mc = minecraft.Minecraft.create() #

#Getting the players position
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z


#Telling the game that the program is running
mc.postToChat("Program running.")


#Creating the 'H'
mc.setBlocks(x,y,z+4,x,y+6,z+4,35,4)
mc.setBlocks(x-1,y+3,z+4,x-3,y+3,z+4,35,3)
mc.setBlocks(x-4,y,z+4,x-4,y+6,z+4,35,7)

#Creating the 'T'
mc.setBlocks(x-8,y,z+4,x-8,y+5,z+4,35,6)
mc.setBlocks(x-6,y+6,z+4,x-10,y+6,z+4,35,3)


#Creating a '1'
mc.setBlocks(x+2,y,z+4,x+4,y,z+4,35,8)
mc.setBlocks(x+3,y+1,z+4,x+3,y+6,z+4,35,7)
mc.setBlock(x+4,y+5,z+4,35)



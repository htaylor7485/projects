import time,mcpi.minecraft as minecraft #
mc = minecraft.Minecraft.create() #

#Tells the game that the program is running
mc.postToChat("Program running.")

#Finds player position
pos =  mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

#Sets surrounding blocks to air before the pool is created
mc.setBlocks(x,y,z-5,x+30,y+11,z+20,0)

#Creates the glass border around the pool
mc.setBlocks(x,y,z+5,x+25,y+9,z+15,20)

#Adds the water to finish the pool
mc.setBlocks(x+1,y+1,z+6,x+24,y+9,z+14,9)


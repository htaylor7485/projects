import time,mcpi.minecraft as minecraft #
mc = minecraft.Minecraft.create() #

#Creates a loop
while True:
    pos = mc.player.getPos() # Gets the player position
    x = pos.x
    y = pos.y
    z = pos.z # Sets each coordinate as a variable
    air = 0 #Sets variable as the air block
    glass = 20
    


    mc.setBlocks(x+1, y, z+1, x-1, y+3, z-1, air)
    mc.setBlocks(x+1, y, z+1, x-1, y+3, z-1, glass)
    mc.setBlocks(x+2, y, z+2, x-2, y+4, z-2, air)
    

    

    
    

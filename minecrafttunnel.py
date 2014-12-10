import time,mcpi.minecraft as minecraft #
mc = minecraft.Minecraft.create() #

#Creates a loop
while True:
    pos = mc.player.getPos() # Gets the player position
    x = pos.x
    y = pos.y
    z = pos.z # Sets each coordinate as a variable
    air = 0 #Sets variable as the air block
    gold = 41
    
    mc.setBlocks(x+2, y, z+4, x-2, y+4, z-2, air) #Sets the blocks around the player
    
    

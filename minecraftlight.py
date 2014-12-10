aimport mcpi.minecraft as minecraft,time #
mc = minecraft.Minecraft.create() #

while True:
    
    #move player close to origin
    mc.player.setPos(57,24,0)

    black=7
    red=14
    orange=1
    green=5
    fence=85

    #Setup empty lights
    mc.setBlock(62,25,0,fence)
    mc.setBlock(62,26,0,fence)
    mc.setBlock(62,27,0,35,black)
    mc.setBlock(62,28,0,35,black)
    mc.setBlock(62,29,0,35,black)



    mc.setBlock(62,27,0,35,green)
    time.sleep(10)

    mc.setBlock(62,27,0,35,black)
    mc.setBlock(62,28,0,35,orange)
    time.sleep(4)

    mc.setBlock(62,28,0,35,black)
    mc.setBlock(62,29,0,35,red)
    time.sleep(10)

    mc.setBlock(62,28,0,35,orange)
    time.sleep(3)

    mc.setBlock(62,28,0,35,black)
    mc.setBlock(62,29,0,35,black)

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

import time

mc.postToChat("Prepare to be rich!")
time.sleep(1)

while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    block = 41

    mc.setBlock(x, y, z, block)

    time.sleep(0.2)
    


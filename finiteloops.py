#Demonstration of for loops in python

import time,mcpi.minecraft as minecraft #
mc = minecraft.Minecraft.create() #

for block in (0,2,4,6,8,10):
    mc.setBlock(0,10,block,9)
    time.sleep(1)
    mc.postToChat(block)

for block in (1,3,5,7,9,11):
    mc.setBlock(0,10,block,3)
    time.sleep(1)
    mc.postToChat(block)



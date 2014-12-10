import time,mcpi.minecraft as minecraft #
mc = minecraft.Minecraft.create()

    #Start of program

while True:    
    #Counting down to teleportation

    time.sleep(3)
    mc.postToChat("Teleportation in 3")
    time.sleep(1)
    mc.postToChat("Teleportation in 2")
    time.sleep(1)
    mc.postToChat("Teleportation in 1")


    #Changing the position of the player 3 times in 3 different places, with a
    #pause of 2 seconds inbetween

    mc.player.setPos(0,10,60)
    time.sleep(2)
    mc.player.setPos(0,25,40)
    time.sleep(2)
    mc.player.setPos(0,20,85)
    time.sleep(2)


    #Telling the player in game that the teleportation has finished

    mc.postToChat("*Teleportation Complete*")

    #end of program




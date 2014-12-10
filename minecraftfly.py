import time,mcpi.minecraft as minecraft #
mc = minecraft.Minecraft.create()

#Start of program
    
#Counting down to teleportation

mc.player.setPos(-7,8,1)

time.sleep(2)
mc.postToChat("Look towards the sign!")
time.sleep(7)
mc.postToChat("Flying in 3")
time.sleep(1)
mc.postToChat("Flying in 2")
time.sleep(1)
mc.postToChat("Flying in 1")


#Changing the position of the player 3 times in 3 different places, with a
#pause of 2 seconds inbetween

mc.postToChat("Lift off!")

mc.player.setPos(1,20,0)
time.sleep(0.1)
mc.player.setPos(3,20,0)
time.sleep(0.1)
mc.player.setPos(6,20,0)
time.sleep(0.1)
mc.player.setPos(9,20,0)
time.sleep(0.1)
mc.player.setPos(12,20,0)
time.sleep(0.1)
mc.player.setPos(15,20,0)
time.sleep(0.1)
mc.player.setPos(18,20,0)
time.sleep(0.1)
mc.player.setPos(21,20,0)
time.sleep(0.1)
mc.player.setPos(24,20,0)
time.sleep(0.1)
mc.player.setPos(27,20,0)
time.sleep(0.1)
mc.player.setPos(30,20,0)
time.sleep(0.1)
mc.player.setPos(33,20,0)
time.sleep(0.1)
mc.player.setPos(36,20,0)
time.sleep(0.1)
mc.player.setPos(39,20,0)
time.sleep(0.1)
mc.player.setPos(42,20,0)
time.sleep(0.1)
mc.player.setPos(45,20,0)
time.sleep(0.1)
mc.player.setPos(48,20,0)
time.sleep(0.1)
mc.player.setPos(51,20,0)
time.sleep(0.1)
mc.player.setPos(54,20,0)
time.sleep(0.1)
mc.player.setPos(57,20,0)
time.sleep(0.1)
mc.player.setPos(60,20,0)
time.sleep(0.1)
mc.player.setPos(63,20,0)
time.sleep(0.1)
mc.player.setPos(66,20,0)
time.sleep(0.1)
mc.player.setPos(69,20,0)
time.sleep(0.1)
mc.player.setPos(72,20,0)
time.sleep(0.1)
mc.player.setPos(75,20,0)
time.sleep(0.1)
mc.player.setPos(78,20,0)
time.sleep(0.1)
mc.player.setPos(81,20,0)
time.sleep(0.1)
mc.player.setPos(84,20,0)
time.sleep(0.1)
mc.player.setPos(87,20,0)
time.sleep(0.1)
mc.player.setPos(90,20,0)
time.sleep(0.1)
mc.player.setPos(-7,8,1)
time.sleep(0.1)
    
#Telling the player in game that the teleportation has finished

mc.postToChat("Annnnd done!")

    #end of program

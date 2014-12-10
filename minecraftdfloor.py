import time,mcpi.minecraft as minecraft #
mc = minecraft.Minecraft.create()
playerTilePos = mc.player.getTilePos()
block = mc.setBlocks()

mc.setBlocks(playerTilePos.x - 25, playerTilePos.y - 1, playerTilePos.z - 25, playerTilePos.x + 25, playerTilePos.y -1, playerTilePos.z + 25, block.DIAMOND_BLOCK)
mc.postToChat("Now that's a big diamond floor!")

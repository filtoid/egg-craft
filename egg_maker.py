import mcpi.minecraft as minecraft
import mcpi.block as block
from room import Room

mc = minecraft.Minecraft.create('127.0.0.1')
room = Room()
room.draw_room(mc)
room.set_lighting(mc)


#make the egg - first create some reusable colours
orangeWool = block.Block(35,1)
greyWool = block.Block(35,8)
blueWool = block.Block(35,2)

def make_egg():
	#Insert Code Here To Draw Egg
	#BAND 1
	mc.setBlocks(-5,0,15,5,0,15, block.STONE)
	mc.setBlocks(-8,1,15,8,1,15, block.STONE)
	mc.setBlocks(-9,3,15,9,2,15, block.STONE)

	#BAND 2
	mc.setBlocks(-10,9,15,10,4,15, block.GOLD_ORE)

	#BAND 3
	mc.setBlocks(-9,14,15,9,10,15, orangeWool)
	mc.setBlocks(-9,14,15,9,10,15, blueWool)

	#BAND 4
	mc.setBlocks(-7,17,15,7,14,15, block.STONE)
        mc.setBlocks(-5,20,15,5,17,15, block.STONE)
	mc.setBlocks(-2,21,15,2,20,15, block.STONE)

make_egg()


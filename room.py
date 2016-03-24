import mcpi.block as block

class Room(object):
	def draw_room(self, mc):
		#clear the area
		mc.setBlocks(-20,0,-20,20,64,20,block.AIR)
		
		#walls
		#No walls for now

		#floor
		mc.setBlocks(-20,-2,-20,20,-2,20,block.GRASS)
		mc.setBlocks(-20,-1,-20,20,-1,20,block.GRASS)
		

	def set_lighting(self, mc):
		#We don't need any special lighting for this
		pass
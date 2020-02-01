





def findActualRect(width, height, plam_width, palm_height):
	x1 = plam_width // 2
	y1 = palm_height // 2
	x2 = width - (plam_width // 2)
	y2 = height - (palm_height // 2) 
	return x1, y1, x2, y2

def findActualRectWidth(width, height, palm_height, plam_width):
	return (width - plam_width, height - palm_height)

def convertAct(act_width, act_height, width, height, x, y):
	act_x = (act_width / width) * x
	act_y = (act_height / height) * y
	return (act_x, act_y) 

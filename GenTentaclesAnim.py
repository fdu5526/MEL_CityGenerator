import maya.cmds as cmds
import maya.mel as mel
import random
import time

#random.seed(0)

baseTentacle = "BaseTentacle"

def RandTwist ():
	twistAmount = random.uniform(100.0, 400.0)
	if (random.random() < 0.5):
		twistAmount = twistAmount * float(-1.0)
	return twistAmount


allTentacles = []
def GenTentacles (n):
	
	for i in range(0, n):
		
		# create a new cone
		cmds.select(baseTentacle)
		newTentacle = cmds.duplicate()[0]
		cmds.move(0, 0, 0)

		# vary tentacle size
		sx = random.uniform(0.1, 0.3)
		sy = random.uniform(0.5, 1.3)
		cmds.scale(sx, sy, sx)

		# create twist deformer
		twist = cmds.nonLinear(type="twist", lowBound=-1, highBound=1)[0]
		cmds.move(-11.25, 44, 0)

		# hide the deformer
		mel.eval("editDisplayLayerMembers -noRecurse hidden `ls -selection`;")

		# combine twist and model, rotate it
		rx = random.uniform(-360, 360)
		ry = random.uniform(-360, 360)
		rz = random.uniform(-360, 360)
		cmds.select(newTentacle, add=True)
		mel.eval("doGroup 0 1 1")
		cmds.rotate(rx, ry, rz);
		tentacleGroup = cmds.ls(selection=True)

		# move to frame 0
		cmds.currentTime(0)

		for j in range(0, 40): #TODO this is frames
			# do the twist
			cmds.select(twist)
			twistAmount = RandTwist()
			cmds.setAttr(twist + ".endAngle", twistAmount);
			cmds.setKeyframe(twist + ".ea")

			# rotate a bit
			cmds.select(tentacleGroup)
			rx = random.uniform(-36, 36)
			ry = random.uniform(-36, 36)
			rz = random.uniform(-36, 36)
			cmds.rotate(rx, ry, rz, relative=True)
			cmds.setKeyframe(tentacleGroup)


			# move to next key frame
			cmds.currentTime(30 * j + random.uniform(-10, 10))

			
		

		allTentacles.append(tentacleGroup)



GenTentacles(50)
cmds.select(clear=True)

# select all the tentacles, merge them
for i in range(0, len(allTentacles)):
	cmds.select(allTentacles[i], add=True)
mel.eval("doGroup 0 1 1")

print(cmds.ls(selection=True))
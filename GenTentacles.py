import maya.cmds as cmds
import maya.mel as mel
import random
import time

#random.seed(0)

baseTentacle = "BaseTentacle"


def GenTentacles (n):
	
	for i in range(0, n):
		
		# create a new cone
		cmds.select(baseTentacle)
		newTentacle = cmds.duplicate()[0]
		cmds.move(0, 0, 0)

		# vary tentacle size
		sx = random.uniform(0.1, 0.4)
		sy = random.uniform(0.5, 1.5)
		cmds.scale(sx, sy, sx)

		# create twist deformer
		twist = cmds.nonLinear(type="twist", lowBound=-1, highBound=1)[0]
		cmds.move(-11.25, 44, 0)

		# do the twist
		twistAmount = random.uniform(300.0, 443.0)
		if (random.random() < 0.5):
			twistAmount = twistAmount * float(-1.0)
		cmds.setAttr(twist + ".endAngle", twistAmount);
		mel.eval("editDisplayLayerMembers -noRecurse hidden `ls -selection`;")

		# combine twist and model, rotate it
		rx = random.uniform(-30, 30)
		#ry = random.uniform(-360, 360)
		rz = random.uniform(-30, 30)
		cmds.select(newTentacle, add=True)
		mel.eval("doGroup 0 1 1")
		cmds.rotate(rx, 0, rz);



GenTentacles(100)
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om  
import random

# http://ldunham.blogspot.com/2012/08/mayapython-querying-soft-selection.html
def softSelection():  
    selection = om.MSelectionList()  
    softSelection = om.MRichSelection()  
    om.MGlobal.getRichSelection(softSelection)  
    softSelection.getSelection(selection)  
      
    dagPath = om.MDagPath()  
    component = om.MObject()  
      
    iter = om.MItSelectionList( selection,om.MFn.kMeshVertComponent )  
    elements = []  
    while not iter.isDone():   
        iter.getDagPath( dagPath, component )  
        dagPath.pop()  
        node = dagPath.fullPathName()  
        fnComp = om.MFnSingleIndexedComponent(component)     
                  
        for i in range(fnComp.elementCount()):  
            elements.append('%s.vtx[%i]' % (node, fnComp.element(i)))  
        iter.next()  
    return elements 


random.seed(0)

# generate default sphere
#sphere = cmds.polyTorus(r=18.27411, sr=4.8)[0]
sphere = cmds.polySphere(r=20.0)[0]
cmds.polySmooth(sphere)
cmds.polySmooth(sphere)

#cmds.refresh()

numVertices = cmds.polyEvaluate(sphere)["vertex"]
numTransform = numVertices / 5

for v in range (0, numTransform):
	

	for i in range(0, 3):
		n = random.randint(0, numVertices)
		name = sphere+".vtx[" + str(n) + "]"
		coords = cmds.pointPosition(name)
		
		cmds.select(name)
		selection = softSelection()

		x = coords[0] * random.uniform(-0.2, 0.2)
		y = coords[1] * random.uniform(-0.2, 0.2)
		z = coords[2] * random.uniform(-0.2, 0.2)

		# go back, set a key frame
		cmds.currentTime(v - 20)
		cmds.select(selection)
		cmds.setKeyframe()

		# move the point we chose
		cmds.currentTime(v + 2)
		cmds.select(name)
		cmds.move(x, y, z, relative=True)

		# key frame all the soft selection
		cmds.select(selection)
		cmds.setKeyframe()


print(numTransform)
# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Test():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    mdb.models['Model-1'].sections['variable'].setValues(preIntegrate=OFF, 
        material='acier', thicknessType=UNIFORM, thickness=0.2, 
        thicknessField='', nodalThicknessField='', 
        idealization=NO_IDEALIZATION, integrationRule=SIMPSON, numIntPts=5)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.Job(name='Job-3', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
        multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)


def Genererpiece():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    pass


def Generermodele():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=1000.0)
    g, v1, d1, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=830.052, 
        farPlane=1055.57, width=1198.06, height=627.502, cameraPosition=(
        42.0414, 16.3534, 942.809), cameraTarget=(42.0414, 16.3534, 0))
    s1.rectangle(point1=(-260.0, 0.0), point2=(260.0, 205.0))
    s1.ObliqueDimension(vertex1=v1[0], vertex2=v1[1], textPoint=(-314.93408203125, 
        65.5632095336914), value=300.0)
    s1.ObliqueDimension(vertex1=v1[3], vertex2=v1[0], textPoint=(-156.108673095703, 
        -160.267944335938), value=410.0)
    p = mdb.models['Model-1'].Part(name='Modele', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Modele']
    p.BaseSolidExtrude(sketch=s1, depth=1.7)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Modele']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']



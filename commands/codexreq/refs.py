"""
Create a gear
"""
sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
gear = sketch.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 1)
gear.isConstruction = True
gear.name = 'Gear'


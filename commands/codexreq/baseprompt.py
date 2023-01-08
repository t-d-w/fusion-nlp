"""
The following are natural language commands (comments) and the code needed to accomplish them using the Fusion 360 API. 
"""

"""
Get the active design
"""
design = adsk.fusion.Design.cast(app.activeProduct)

"""
Get the root component of the active design
"""
rootComp = design.rootComponent

"""
The following are natural language commands (comments) and the code needed to accomplish them using the Fusion 360 API. 
The API reference manual can be found at this link: https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-7B5A90C8-E94C-48DA-B16B-430729B734DC 
A chm file can be found here https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/ExtraFiles/FusionAPI.chm
"""

"""
Get the active design
"""
design = adsk.fusion.Design.cast(app.activeProduct)

"""
Get the root component of the active design
"""
rootComp = design.rootComponent

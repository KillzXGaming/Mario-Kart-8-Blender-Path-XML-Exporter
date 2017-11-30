bl_info = {
    "name": "A MK8 Path Tool",
    "author": "KillzXGaming, Lots of help from AboodXD, Wexos helped me figure out tan/norms",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "A tool that has premade paths that can be exported into XML for yamlconv",
    "warning": "",
    "wiki_url": "",
    "category": "Mario Kart 8 Tools",
    }

if "bpy" in locals():
    import importlib
    if "MK8_export_paths" in locals():
        importlib.reload(MK8_export_paths)

	
import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
from bl_operators.presets import AddPresetBase
from MK8_export_paths import *
# import idproperty


from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       AddonPreferences,
                       PropertyGroup,
                       )


					   
# def HeadlightsToggle
    # scene = bpy.context.scene
    # unhide_objects()
    # for ob in bpy.context.screen.scene.objects:
        # if ob.name.startswith(str(scene.TestStringProp)):
            # ob.hide = True
        # else:
            # ob.hide = False
    # if not scene.TestBool:
        # unhide_objects()

# def initproplights():
    # bpy.types.Scene.TestBool = bpy.props.BoolProperty(
        # name="Hide", 
        # description="", 
        # default=False, 
        # subtype='NONE', 
        # update=HeadlightsToggle)


#Hide/Unhide Lap Paths
def ToggleHide(self, context): 
    scene = bpy.context.scene
    if scene.TestStringProp: #Hide all paths if checked
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.TestStringProp)):
                ob.hide = True
    if not scene.TestBool: #Unhide all paths if unchecked!
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.TestStringProp)):
                ob.hide = False

#Hide/Unhide Gravity Paths
def ToggleHideGravity(self, context):
    scene = bpy.context.scene
    if scene.StringPropGravity: #Hide all paths if checked
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropGravity)):
                ob.hide = True
    if not scene.BoolGravity: #Unhide all paths if unchecked!
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropGravity)):
                ob.hide = False

#Hide/Unhide Enemy Paths				
def ToggleHideEnemy(self, context):
    scene = bpy.context.scene
    if scene.StringPropEnemy: #Hide all paths if checked
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropEnemy)):
                ob.hide = True
    if not scene.BoolEnemy: #Unhide all paths if unchecked!
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropEnemy)):
                ob.hide = False

#Hide/Unhide Intro Camera Paths				
def ToggleHideIntro(self, context):
    scene = bpy.context.scene
    if scene.StringPropIntro: #Hide all paths if checked
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropIntro)):
                ob.hide = True
    if not scene.BoolIntro: #Unhide all paths if unchecked!
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropIntro)):
                ob.hide = False			
	
#Hide/Unhide Replay Camera Paths				
def ToggleHideReplay(self, context):
    scene = bpy.context.scene
    if scene.StringPropReplay: #Hide all paths if checked
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropReplay)):
                ob.hide = True
    if not scene.BoolReplay: #Unhide all paths if unchecked!
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropReplay)):
                ob.hide = False	
	
#Hide/Unhide Glider Paths				
def ToggleHideGlide(self, context):
    scene = bpy.context.scene
    if scene.StringPropGlide: #Hide all paths if checked
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropGlide)):
                ob.hide = True
    if not scene.BoolGlide: #Unhide all paths if unchecked!
        for ob in bpy.context.screen.scene.objects:
            if ob.name.startswith(str(scene.StringPropGlide)):
                ob.hide = False
	


	
def initprop():
    bpy.types.Scene.TestBool = bpy.props.BoolProperty(
        name="Hide Lap Paths", 
        description="", 
        default=False, 
        subtype='NONE', 
        update=ToggleHide)

    bpy.types.Scene.TestStringProp = bpy.props.StringProperty(
        name="TestStringProp", 
        description="", 
        default="Lap", 
        subtype='NONE')

    bpy.types.Scene.BoolGravity = bpy.props.BoolProperty(
        name="Hide Gravity Paths", 
        description="", 
        default=False, 
        subtype='NONE', 
        update=ToggleHideGravity)

    bpy.types.Scene.StringPropGravity = bpy.props.StringProperty(
        name="StringPropGravity", 
        description="", 
        default="Gravity", 
        subtype='NONE')	
		
    bpy.types.Scene.BoolEnemy = bpy.props.BoolProperty(
        name="Hide Enemy Paths", 
        description="", 
        default=False, 
        subtype='NONE', 
        update=ToggleHideEnemy)

    bpy.types.Scene.StringPropEnemy = bpy.props.StringProperty(
        name="StringPropEnemy", 
        description="", 
        default="Enemy", 
        subtype='NONE')	
		
    bpy.types.Scene.BoolGlide = bpy.props.BoolProperty(
        name="Hide Glder Paths", 
        description="", 
        default=False, 
        subtype='NONE', 
        update=ToggleHideGlide)

    bpy.types.Scene.StringPropGlide = bpy.props.StringProperty(
        name="StringPropGlide", 
        description="", 
        default="Glide", 
        subtype='NONE')
		
    bpy.types.Scene.BoolIntro = bpy.props.BoolProperty(
        name="Hide Intro Camera Paths", 
        description="", 
        default=False, 
        subtype='NONE', 
        update=ToggleHideIntro)

    bpy.types.Scene.StringPropIntro = bpy.props.StringProperty(
        name="StringPropIntro", 
        description="", 
        default="Intro", 
        subtype='NONE')	
	
    bpy.types.Scene.BoolReplay = bpy.props.BoolProperty(
        name="Hide Replay Camera Paths", 
        description="", 
        default=False, 
        subtype='NONE', 
        update=ToggleHideReplay)

    bpy.types.Scene.StringPropReplay = bpy.props.StringProperty(
        name="StringPropReplay", 
        description="", 
        default="Replay", 
        subtype='NONE')	
		
	#props of lap path flags

    bpy.types.Object.IntCheckpoint = bpy.props.IntProperty(
	name="Check Point",
	description="Checkpoints to prevent skipping paths to count a lap",
	min=-1, max=99999,
	default=-1)

    bpy.types.Object.IntLapCheck = bpy.props.IntProperty(
	name="Lap Check",
	description="Counts a lap passed. Looped track uses 0 for first path!",
	min=-1, max=7,
	default=-1)

    bpy.types.Object.IntClipIndx = bpy.props.IntProperty(
	name="Clip Index",
	description="Clip index used for culling (NOT DONE)",
	min=-1, max=99999,
	default=-1)

    bpy.types.Object.IntReturnPosition = bpy.props.IntProperty(
	name="Return Position",
	description="Index for Return Posiion",
	min=-1, max=99999,
	default=-1)
	
    bpy.types.Object.IntSoundSW = bpy.props.IntProperty(
	name="SoundSW Index",
	description="Index for SoundSW",
	min=-1, max=99999,
	default=-1)
	
    bpy.types.Object.IntMapCameraY = bpy.props.IntProperty(
	name="Map Camera Y axis",
	description="Map Camera Y axis",
	min=0, max=99999,
	default=320)
	
    bpy.types.Object.IntMapCameraFovy = bpy.props.IntProperty(
	name="Map Camera Fov on Y Axis",
	description="Map Camera Fov on Y Axis",
	min=-0, max=120,
	default=65)
	
    bpy.types.Object.HeadlightsEnum = EnumProperty(
        name="",
        description="Apply Data to attribute.",
        items=[ ('False', "Headlights Off", ""),
                ('True', "Headlights On", ""),
               ]
        )
	#props of gravity path flags

    bpy.types.Object.IntCameraHeight = bpy.props.IntProperty(
	name="Camera Height",
	description="Height of Anti Gravity Camera",
	min=1, max=5,
	default=1)
		
    bpy.types.Object.GlideOnlyEnum = EnumProperty(
        name="",
        description="Only enable anti gravity if gliding",
        items=[ ('False', "Do not only active while gliding", ""),
                ('True', "Active only while gliding", ""),
               ]
        )	

    bpy.types.Object.GTransformEnum = EnumProperty(
        name="",
        description="Enable the anti gravity tranformation or disable. This is generally on true",
        items=[ ('True', "Transform", ""),
                ('False', "Do not transform", ""),
               ]
        )	
	#props of glider path flags
		
    bpy.types.Object.CannonEnum = EnumProperty(
        name="",
        description="Enable/disable cannon where you are shot in a direction. Last glider path is often false!",
        items=[ ('False', "Cannon Disabled", ""),
                ('True', "Cannon Enabled", ""),
               ]
        )	

	#props of enemy path flags
		
    bpy.types.Object.PriorityEnum = EnumProperty(
        name="",
        description="Determinie item necessary to use path",
        items=[ ('1', "No item Needed", ""),
                ('2', "Mushroom Needed", ""),
               ]
        )	
		
    bpy.types.Object.IntPathDir = bpy.props.IntProperty(
	name="Path Directory",
	description="IDK what this does",
	min=1, max=5,
	default=1)
	
    bpy.types.Object.IntBattleFlag = bpy.props.IntProperty(
	name="Battle Flag",
	description="IDK what this does",
	min=1, max=5,
	default=1)
	
	#props of item path flags
	
    bpy.types.Object.HoverEnum = EnumProperty(
        name="",
        description="Determinie hover???",
        items=[ ('0', "No hover", ""),
                ('1', "IDK", ""),
                ('2', "IDK", ""),
               ]
        )
		
    bpy.types.Object.ItemPriorityEnum = EnumProperty(
        name="",
        description="Determinie item for some reason???",
        items=[ ('1', "No item", ""),
                ('2', "Mushroom", ""),
               ]
        )	
		
    bpy.types.Object.SearchAreaEnum = EnumProperty(
        name="",
        description="IDK",
        items=[ ('0', "Do not search area", ""),
                ('1', "IDK", ""),
                ('2', "IDK", ""),
               ]
        )	
		
    #Replay Camera
    bpy.types.Object.AutoFovyEnumReplay = EnumProperty(
        name="",
        description="Enable/disable auto fov on y axis",
        items=[ ('False', "No Auto Fov on Y axis", ""),
                ('True', "Auto Fov on Y axis", ""),
               ]
        )

    bpy.types.Object.CameraTypeEnumReplay = EnumProperty(
        name="",
        description="Type of camera",
        items=[ ('0', "Default camera type", ""),
                ('1', "IDK", ""),
                ('2', "IDK", ""),
               ]
        )
		
    bpy.types.Object.FollowEnumReplay = EnumProperty(
        name="",
        description="Follow player",
        items=[ ('False', "Do not follow player", ""),
                ('True', "Follow player", ""),
               ]
        )
	
    bpy.types.Object.IntAngleXReplay = bpy.props.IntProperty(
	name="Angle X axis",
	description="",
	min=-180, max=180,
	default=0)
	
    bpy.types.Object.IntAngleYReplay = bpy.props.IntProperty(
	name="Angle Y axis",
	description="",
	min=-180, max=180,
	default=0)
	
    bpy.types.Object.IntCamera_PathReplay = bpy.props.IntProperty(
	name="Camera Path",
	description="",
	min=-1, max=60,
	default=-1)
	
    bpy.types.Object.IntDepthOfFieldReplay = bpy.props.IntProperty(
	name="Depth Of Field",
	description="",
	min=-0, max=45,
	default=0)
	
    bpy.types.Object.IntDistanceReplay = bpy.props.IntProperty(
	name="Distance",
	description="",
	min=-0, max=45,
	default=0)

    bpy.types.Object.IntFovyReplay = bpy.props.IntProperty(
	name="Fov Y axis",
	description="",
	min=0, max=90,
	default=45)
	
    bpy.types.Object.IntFovy2Replay = bpy.props.IntProperty(
	name="Fov Y2 axis",
	description="",
	min=0, max=90,
	default=15)
	
    bpy.types.Object.IntFovySpeedReplay = bpy.props.IntProperty(
	name="Fovy speed",
	description="",
	min=0, max=25,
	default=20)
	
    bpy.types.Object.IntGroupReplay = bpy.props.IntProperty(
	name="Group",
	description="",
	min=0, max=10,
	default=0)
	
    bpy.types.Object.IntPitchReplay = bpy.props.IntProperty(
	name="Pitch",
	description="",
	min=-90, max=-90,
	default=0)
	
    bpy.types.Object.IntRollReplay = bpy.props.IntProperty(
	name="Roll",
	description="",
	min=-90, max=-90,
	default=0)
	
    bpy.types.Object.IntUnitIdNumReplay = bpy.props.IntProperty(
	name="UnitIdNum",
	description="",
	min=-131000, max=-131120,
	default=131096)
	
    bpy.types.Object.IntYawReplay = bpy.props.IntProperty(
	name="Yaw",
	description="",
	min=-90, max=-90,
	default=0)
	
    bpy.types.Object.Intprm1Replay = bpy.props.IntProperty(
	name="prm1",
	description="",
	min=0, max=99,
	default=0)
	
    bpy.types.Object.Intprm2Replay = bpy.props.IntProperty(
	name="prm2",
	description="",
	min=0, max=99,
	default=0)
	
	
    #Intro Camera

    bpy.types.Object.FollowCameraTypeIntro =  EnumProperty(
        name="",
        description="Camera Type",
        items=[ ('6', "Default Camera type", ""),
                ('6', "Default Camera type", ""),
               ]
        )
	
    bpy.types.Object.IntCameraNumIntro = bpy.props.IntProperty(
	name="Camera Number",
	description="",
	min=1, max=3,
	default=1)
	
    bpy.types.Object.IntCameraTimeIntro = bpy.props.IntProperty(
	name="Camera Time",
	description="",
	min=0, max=600,
	default=200)
	
    bpy.types.Object.IntCamera_AtPathIntro = bpy.props.IntProperty(
	name="Camera_AtPath",
	description="",
	min=-1, max=30,
	default=-1)
	
    bpy.types.Object.IntCamera_PathIntro = bpy.props.IntProperty(
	name="Camera_Path",
	description="",
	min=-1, max=30,
	default=-1)
	
    bpy.types.Object.IntFovyIntro = bpy.props.IntProperty(
	name="Fov Y axis",
	description="",
	min=0, max=90,
	default=45)
	
    bpy.types.Object.IntFovy2Intro = bpy.props.IntProperty(
	name="Fov Y2 axis",
	description="",
	min=0, max=90,
	default=15)
	
    bpy.types.Object.IntFovySpeedIntro = bpy.props.IntProperty(
	name="Fovy speed",
	description="",
	min=0, max=25,
	default=20)
	
    bpy.types.Object.IntUnitIdNumIntro = bpy.props.IntProperty(
	name="UnitIdNum",
	description="",
	min=-131000, max=-131120,
	default=131096)
	
def delprop():
    del bpy.types.Scene.TestBool
    del bpy.types.Scene.TestStringProp	    
    del bpy.types.Scene.BoolGravity
    del bpy.types.Scene.StringPropGravity	    
    del bpy.types.Scene.BoolEnemy
    del bpy.types.Scene.StringPropEnemy	
    del bpy.types.Scene.BoolGlide
    del bpy.types.Scene.StringPropGlide	
    del bpy.types.Scene.BoolIntro
    del bpy.types.Scene.StringPropIntro
    del bpy.types.Scene.BoolReplay
    del bpy.types.Scene.StringPropReplay
	#Deletion of lap path flags
    del bpy.types.bpy.types.Object.HeadlightsEnum
    del bpy.types.Object.IntCheckpoint
    del bpy.types.Object.IntLapCheck
    del bpy.types.Object.IntReturnPosition
    del bpy.types.Object.IntClipIndx
    del bpy.types.Object.IntSoundSW
    del bpy.types.Object.IntMapCameraY
    del bpy.types.Object.IntMapCameraFovy
	#Deletion of gravity path flags
    del bpy.types.Object.IntCameraHeight
    del bpy.types.Object.GlideOnlyEnum
    del bpy.types.Object.GTransformEnum
	#Deletion of glider path flags
    del bpy.types.Object.CannonEnum
	#Deletion of enemy path flags
    del bpy.types.Object.PriorityEnum
    del bpy.types.Object.IntPathDir
    del bpy.types.Object.IntBattleFlag
	#Deletion of item path flags
    del bpy.types.Object.HoverEnum
    del bpy.types.Object.ItemPriorityEnum
    del bpy.types.Object.SearchAreaEnum
	#Deletion of replay path flags
    del bpy.types.Object.AutoFovyEnumReplay
    del bpy.types.Object.CameraTypeEnumReplay
    del bpy.types.Object.FollowEnumReplay
    del bpy.types.Object.IntAngleXReplay
    del bpy.types.Object.IntAngleYReplay
    del bpy.types.Object.IntCamera_PathReplay
    del bpy.types.Object.IntDepthOfFieldReplay
    del bpy.types.Object.IntDistanceReplay
    del bpy.types.Object.IntFovyReplay
    del bpy.types.Object.IntFovy2Replay
    del bpy.types.Object.IntFovySpeedReplay
    del bpy.types.Object.IntGroupReplay
    del bpy.types.Object.IntPitchReplay
    del bpy.types.Object.IntRollReplay
    del bpy.types.Object.IntUnitIdNumReplay
    del bpy.types.Object.IntYawReplay
    del bpy.types.Object.Intprm1Replay
    del bpy.types.Object.Intprm2Replay	
	#Deletion of intro path flags
    del bpy.types.Object.FollowCameraTypeIntro
    del bpy.types.Object.IntCameraNumIntro
    del bpy.types.Object.IntCameraTimeIntro
    del bpy.types.Object.IntCamera_AtPathIntro
    del bpy.types.Object.IntCamera_PathIntro
    del bpy.types.Object.IntFovyIntro
    del bpy.types.Object.IntFovy2Intro
    del bpy.types.Object.IntFovySpeedIntro
    del bpy.types.Object.IntUnitIdNumIntro


	
class gliderselect(bpy.types.Operator):
    bl_idname = "glider.select"
    bl_label = "glideselect"

 
    def execute(self, context):	
        scene = context.scene
        		
        for ob in scene.objects:
            if ob.name.startswith("Glide"):
                ob.select = True				   

				
				

			
        return{'FINISHED'}
		
class gravityselect(bpy.types.Operator):
    bl_idname = "gravity.select"
    bl_label = "gravityselect"

 
    def execute(self, context):	
        scene = context.scene
        		
        for ob in scene.objects:
            if ob.name.startswith("Gravity"):
                ob.select = True				   

				
				

			
        return{'FINISHED'}

class enemyselect(bpy.types.Operator):
    bl_idname = "enemy.select"
    bl_label = "enemyselect"

 
    def execute(self, context):	
        scene = context.scene
        		
        for ob in scene.objects:
            if ob.name.startswith("Enemy"):
                ob.select = True				   

				
				

			
        return{'FINISHED'}
		
class lapselect(bpy.types.Operator):
    bl_idname = "lap.select"
    bl_label = "lapselect"


    def execute(self, context):	
        scene = context.scene
        		
        for ob in scene.objects:
            if ob.name.startswith("Lap"):
                ob.select = True				   

				
				

			
        return{'FINISHED'}
		
class replayselect(bpy.types.Operator):
    bl_idname = "replay.select"
    bl_label = "replayselect"

 
    def execute(self, context):	
        scene = context.scene
        		
        for ob in scene.objects:
            if ob.name.startswith("Replay"):
                ob.select = True				   

				
				

			
        return{'FINISHED'}
		
class introselect(bpy.types.Operator):
    bl_idname = "intro.select"
    bl_label = "introselect"

 
    def execute(self, context):	
        scene = context.scene
        		
        for ob in scene.objects:
            if ob.name.startswith("Intro"):
                ob.select = True				   

				
				

			
        return{'FINISHED'}

class OBJECT_OT_HEMI(bpy.types.Operator):
    bl_idname = "my.hemisphere"
    bl_label = "hemisphere"

 
    def execute(self, context):				   
        lamp_data = bpy.data.lamp.new(name="hemisphere",type='HEMI')
        lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)			   
        scene.objects.link(lamp_object)
        lamp_object.location = (0, 0, 0)					   

        return{'FINISHED'}


class LaptoGravity(bpy.types.Operator):
    bl_idname = "lap.gravity"
    bl_label = "LaptoGravity"

 
    def execute(self, context):	



        
        
        selected_objects = sorted(bpy.context.selected_objects, key=lambda obj: obj.name)

        for ob in context.selected_objects:
            if ob.name.startswith("Lap"):
                bpy.ops.object.duplicate(linked=True)
                bpy.ops.mesh.add_gravity() #Adds a temporary gravity path for replacing
                mesh = bpy.data.meshes["Gravity Path"]
                context.object.name = "TEMP"
                ob.data = mesh
                ob.name = ob.name.replace("Lap", "Gravity")
				
                objs = bpy.data.objects
                objs.remove(objs["TEMP"], True) #Removes a temporary gravity path for replacing
                              
        return {'FINISHED'} 
		
class ObjectPanel(bpy.types.Panel):
    bl_label = "MK8 Path Settings"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
 
    def draw(self, context):
        scene = context.scene
        obj = context.object
        layout = self.layout
        layout.label("Path Settings")
        # ob = ctx.object
        # idproperty.layout_id_prop(row, ob, "some_related_object")
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row = layout.row()
        col = layout.column(align=True)
        scn = bpy.context.scene
        col.scale_y = 2
        if context.object.name.startswith("Lap"):
            col.prop(obj, "HeadlightsEnum")
        col = layout.column(align=True)
        col = layout.column(align=True)
        col.scale_y = 1.5
        if context.object.name.startswith("Lap"):
            col.prop(obj, "IntCheckpoint")
            row = layout.row()
            col.prop(obj, "IntLapCheck")
            col.prop(obj, "IntReturnPosition")
            col.prop(obj, "IntSoundSW")
            col.prop(obj, "IntMapCameraY")
            col.prop(obj, "IntMapCameraFovy")
            col.prop(obj, "IntClipIndx")
        if context.object.name.startswith("Gravity"):
            col.prop(obj, "GlideOnlyEnum")
            col.prop(obj, "GTransformEnum")
            col.scale_y = 1.5
            col.prop(obj, "IntCameraHeight")
        if context.object.name.startswith("Glide"):
            col.prop(obj, "CannonEnum")
        if context.object.name.startswith("Enemy"):
            col.prop(obj, "PriorityEnum")
            col.prop(obj, "IntPathDir")
            col.prop(obj, "IntBattleFlag")	
        if context.object.name.startswith("Item"):
            col.prop(obj, "HoverEnum")
            col.prop(obj, "ItemPriorityEnum")
            col.prop(obj, "SearchAreaEnum")	
        if context.object.name.startswith("Replay"):
            col.prop(obj, "AutoFovyEnumReplay")
            col.prop(obj, "CameraTypeEnumReplay")
            col.prop(obj, "FollowEnumReplay")	
            col.prop(obj, "IntAngleXReplay")
            col.prop(obj, "IntAngleYReplay")	
            col.prop(obj, "IntCamera_PathReplay")
            col.prop(obj, "IntDepthOfFieldReplay")
            col.prop(obj, "IntDistanceReplay")
            col.prop(obj, "IntFovyReplay")	
            col.prop(obj, "IntFovy2Replay")	
            col.prop(obj, "IntFovySpeedReplay")
            col.prop(obj, "IntPitchReplay")
            col.prop(obj, "IntGroupReplay")
            col.prop(obj, "IntRollReplay")	
            col.prop(obj, "IntYawReplay")	
            col.prop(obj, "Intprm1Replay")
            col.prop(obj, "Intprm2Replay")
            col.prop(obj, "IntUnitIdNumReplay")	
        if context.object.name.startswith("Intro"):
            col.prop(obj, "FollowCameraTypeIntro")
            col.prop(obj, "IntCameraNumIntro")
            col.prop(obj, "IntCameraTimeIntro")	
            col.prop(obj, "IntCamera_AtPathIntro")
            col.prop(obj, "IntCamera_PathIntro")	
            col.prop(obj, "IntFovyIntro")
            col.prop(obj, "IntFovy2Intro")	
            col.prop(obj, "IntFovySpeedIntro")
            col.prop(obj, "IntUnitIdNumIntro")	
			

 
		
class VIEW3D_PT_Blank1_Blank2(Panel):
    bl_idname = "OBJECT_PT_my_panel"
    bl_label = "Mario Kart 8 Path Tools"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "TOOLS"    
    bl_category = "Mario Kart 8"



    def draw(self, context):
        obj = context.object
        layout = self.layout
        scene = context.scene
        layout.label("Path Selection")
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row = layout.row()
        row = layout.row()
        row.scale_y = 1.5
        row.operator("lap.select" , text="Select Lap Paths")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("enemy.select" , text="Select Enemy Paths")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("glider.select" , text="Select Glider Paths")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("gravity.select" , text="Select Gravity Paths")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("intro.select" , text="Select Intro Camera Paths")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("replay.select" , text="Select Replay Camera Paths")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("lap.gravity" , text="Lap2Gravity")
        row = layout.row()
       # row.operator("object.lamp_add(type='HEMI'), text="Add Hemisphere")
        row = layout.row()
        col = layout.column(align=True)
        scn = bpy.context.scene
        col.label(text="Path Toggle")
        col.prop(scene, "TestBool")
        col.prop(scene, "BoolEnemy")
        col.prop(scene, "BoolGlide")
        col.prop(scene, "BoolGravity")
        col.prop(scene, "BoolIntro")
        col.prop(scene, "BoolReplay")

		
		
#Lap Paths
def add_object(self, context):


    verts = [Vector((-1.0, 0, -1.0)),
             Vector((-1.0, 0, 1.0)), 
             Vector((1.0, 0, -1.0)), 
             Vector((1.0, 0, 1.0)), 
             Vector((-1.0, 0.01, -1.0)), 
             Vector((-1.0, 0.01, 1.0)), 
             Vector((1.0, 0.01, -1.0)), 
             Vector((1.0, 0.01, 1.0))]
    
    edges = []
    faces = [(2, 3, 1, 0), (6, 7, 5, 4), (7, 3, 1, 5)]
	
    mesh = bpy.data.meshes.new(name="Lap Path")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)


	
#Gravity Paths
def add_object1(self, context):


    verts = [Vector((-1.0, 0, -1.0)),
             Vector((-1.0, 0, 1.0)), 
             Vector((1.0, 0, -1.0)), 
             Vector((1.0, 0, 1.0)), 
             Vector((-1.0, 0.01, -1.0)), 
             Vector((-1.0, 0.01, 1.0)), 
             Vector((1.0, 0.01, -1.0)), 
             Vector((1.0, 0.01, 1.0))]
    
    edges = []
    faces = [(2, 3, 1, 0), (6, 7, 5, 4), (7, 3, 1, 5)]

    mesh = bpy.data.meshes.new(name="Gravity Path")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
			
#Glider Paths
def add_object2(self, context):


    verts = [Vector((-1.0, 0, -1.0)),
             Vector((-1.0, 0, 1.0)), 
             Vector((1.0, 0, -1.0)), 
             Vector((1.0, 0, 1.0)), 
             Vector((-1.0, 0.01, -1.0)), 
             Vector((-1.0, 0.01, 1.0)), 
             Vector((1.0, 0.01, -1.0)), 
             Vector((1.0, 0.01, 1.0))]
    
    edges = []
    faces = [(2, 3, 1, 0), (6, 7, 5, 4), (7, 3, 1, 5)]

    mesh = bpy.data.meshes.new(name="Glide Path")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)		
	

class Add_LapPath(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_lap"
    bl_label = "Lap Path"
    bl_options = {'REGISTER', 'UNDO'}


    



    def execute(self, context):
        
        add_object(self, context)
		
        scene = context.scene
        obj = scene.objects.active
		
        activeObject = scene.objects.active #Set active object to variable
        mat = bpy.data.materials.new(name="Front") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (1, 0.006883, 0) #Color Red 
        bpy.context.object.active_material.use_transparency = True
        bpy.context.object.active_material.alpha = (0.4) #Transparent Amount
        activeObject.data.polygons[1].select = True  #Active polygon
        
        me = obj.data
        
        for f in me.polygons:
         f.material_index = f.index % 3

        mat1 = bpy.data.materials.new(name="Back") #set new material to variable
        activeObject.data.materials.append(mat1) #add the material to the object  
        bpy.context.object.active_material_index = 1 #Active the second material
        bpy.context.object.active_material.diffuse_color = (0, 1, 0.076676) #Color Green
        bpy.context.object.active_material.use_transparency = True
        bpy.context.object.active_material.alpha = (0.4) #Transparent Amount
		

        

    
        return {'FINISHED'}
	
class Add_GravityPath(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_gravity"
    bl_label = "Gravity Path"
    bl_options = {'REGISTER', 'UNDO'}


    



    def execute(self, context):
        
        add_object1(self, context)
		
        scene = context.scene
        obj = scene.objects.active
		
        activeObject = scene.objects.active #Set active object to variable
        mat = bpy.data.materials.new(name="Front1") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (1, 0.006883, 0) #Color Red 
        bpy.context.object.active_material.use_transparency = True
        bpy.context.object.active_material.alpha = (0.4) #Transparent Amount
        activeObject.data.polygons[1].select = True  #Active polygon
        
        me = obj.data
        
        for f in me.polygons:
         f.material_index = f.index % 3

        mat1 = bpy.data.materials.new(name="Back1") #set new material to variable
        activeObject.data.materials.append(mat1) #add the material to the object  
        bpy.context.object.active_material_index = 1 #Active the second material
        bpy.context.object.active_material.diffuse_color = (0.225547,0, 1) #Color Green
        bpy.context.object.active_material.use_transparency = True
        bpy.context.object.active_material.alpha = (0.4) #Transparent Amount
		
        activeObject.data.polygons[2].select = True  #Active polygon
        
        me = obj.data
        
        for f in me.polygons:
         f.material_index = f.index % 3

        mat1 = bpy.data.materials.new(name="Back") #set new material to variable
        activeObject.data.materials.append(mat1) #add the material to the object  
        bpy.context.object.active_material_index = 1 #Active the second material
        bpy.context.object.active_material.diffuse_color = (0.225547,0, 1) #Color Green
        bpy.context.object.active_material.use_transparency = True
        bpy.context.object.active_material.alpha = (0.4) #Transparent Amount
        
    
        return {'FINISHED'}

class Add_GlidePath(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_glide"
    bl_label = "Glide Path"
    bl_options = {'REGISTER', 'UNDO'}

    scale = FloatVectorProperty(
            name="scale",
            default=(0.25, 0.25, 0.5),
            subtype='TRANSLATION',
            description="scaling",
            )
    



    def execute(self, context):
        
        add_object2(self, context)
		
        scene = context.scene
        obj = scene.objects.active
		
        activeObject = scene.objects.active #Set active object to variable
        mat = bpy.data.materials.new(name="Front") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (1, 0.006883, 0) #Color Red 
        bpy.context.object.active_material.use_transparency = True
        bpy.context.object.active_material.alpha = (0.4) #Transparent Amount
        activeObject.data.polygons[1].select = True  #Active polygon
        
        me = obj.data
        
        for f in me.polygons:
         f.material_index = f.index % 3

        mat1 = bpy.data.materials.new(name="Back") #set new material to variable
        activeObject.data.materials.append(mat1) #add the material to the object  
        bpy.context.object.active_material_index = 1 #Active the second material
        bpy.context.object.active_material.diffuse_color = (1,0.311029, 0) #Color Orange
        bpy.context.object.active_material.use_transparency = True
        bpy.context.object.active_material.alpha = (0.4) #Transparent Amount
		
        activeObject.data.polygons[2].select = True  #Active polygon
        
        me = obj.data
        
        for f in me.polygons:
         f.material_index = f.index % 3

        mat1 = bpy.data.materials.new(name="Back") #set new material to variable
        activeObject.data.materials.append(mat1) #add the material to the object  
        bpy.context.object.active_material_index = 1 #Active the second material
        bpy.context.object.active_material.diffuse_color = (1,0.311029, 0) #Color Orange
        bpy.context.object.active_material.use_transparency = True
        bpy.context.object.active_material.alpha = (0.4) #Transparent Amount
        
    
        return {'FINISHED'}	



	



# Registration




def add_object_button(self, context):
    self.layout.operator(
        Add_LapPath.bl_idname,
        text="Lap Path",
        icon='PLUGIN')
    self.layout.operator(
        Add_GravityPath.bl_idname,
        text="Gravity Path",
        icon='PLUGIN')
    self.layout.operator(
        Add_GlidePath.bl_idname,
        text="Glide Path",
        icon='PLUGIN')
		
		
# This allows you to right click on a button and link to the manual
def add_object_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/dev/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object", "editors/3dview/object"),
        )
    return url_manual_prefix, url_manual_mapping


	
	
def register():
    bpy.utils.register_module(__name__)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.INFO_MT_mesh_add.append(add_object_button)
    bpy.utils.register_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.append(menu_func_export)
    # bpy.types.Object.some_related_object = idproperty.ObjectIDProperty(name="something related")
    initprop()


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)
    bpy.utils.unregister_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)
    # del bpy.types.Object.some_related_object
    delprop()
    


if __name__ == "__main__":
    register()

	
	


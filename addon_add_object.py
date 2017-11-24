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


def common_update(self, context, origin):

    obj = context.object
    scene = context.scene

    for ob in scene.objects:
        if (scene.my_prop == True):
            if ob.name.startswith("Glide"):
                ob.hide = True
            else:
                ob.unhide = True
    else:
            ob.hide = False		    


			
			
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
            if ob.select:
                ob.data = mesh
                bpy.context.object.name = bpy.context.object.name.replace("Lap", "Gravity")
				
				

			
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

class MySettings(PropertyGroup):

    bpy.types.Scene.my_prop = bpy.props.BoolProperty(update=lambda self, context: common_update(self, context, 'my_bool_one'))

    def execute(self, context):	
        scene = context.scene	
	


		
    bpy.types.Scene.my_enum = EnumProperty(
        name="Dropdown:",
        description="Apply Data to attribute.",
        items=[ ('OP1', "Headlights Off", ""),
                ('OP2', "Headlights On", ""),
               ]
        )

		
		
class ObjectPanel(bpy.types.Panel):
    bl_label = "Hello from Object context"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
 
    def draw(self, context):
        scene = context.scene
        obj = context.object
        layout = self.layout
        layout.label("First row")
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row = layout.row()
        row.operator("object.lamp_add" , text="Add Lamp", icon='LAMP_AREA')
		
        
		
class PathSETTINGS(Panel):
    bl_idname = "OBJECT_PT_my_panel"
    bl_label = "My Panel"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "TOOLS"    
    bl_category = "MK8"



    def draw(self, context):
        obj = context.object
        layout = self.layout
        scene = context.scene
        layout.label("First row")
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
       # row.operator("object.lamp_add(type='HEMI'), text="Add Hemisphere")
        row = layout.row()
        row.prop(scene, "my_prop", text="Hide Object")
        row = layout.row()
        row = layout.row()
        row.prop(scene, "my_enum")	


#Lap Paths
def add_object(self, context):


    verts = [Vector((-0.25, 0.0, -0.25)), Vector((-0.25, 0.0, 0.25)), Vector((0.25, 0.0, -0.25)), Vector((0.25, 0.0, 0.25)), Vector((-0.25, 0.0024999999441206455, -0.25)), Vector((-0.25, 0.0024999999441206455, 0.25)), Vector((0.25, 0.0024999999441206455, -0.25)), Vector((0.25, 0.0024999999441206455, 0.25)), Vector((0.009097770787775517, 0.037538301199674606, -0.011082690209150314)), Vector((0.009097770787775517, 0.037538301199674606, 0.008303677663207054)), Vector((0.010442008264362812, 0.0007872602436691523, -0.012137915939092636)), Vector((0.010442008264362812, 0.0007872602436691523, 0.009358905255794525)), Vector((-0.007850013673305511, 0.03718690574169159, -0.011082690209150314)), Vector((-0.007850013673305511, 0.03718690574169159, 0.008303677663207054)), Vector((-0.008350776508450508, 0.00039761816151440144, -0.012137915939092636)), Vector((-0.008350776508450508, 0.00039761816151440144, 0.009358905255794525)), Vector((0.01586453802883625, 0.03408169001340866, -0.018775926902890205)), Vector((0.01586453802883625, 0.03408169001340866, 0.015996914356946945)), Vector((-0.01453429739922285, 0.033451423048973083, 0.015996914356946945)), Vector((-0.01453429739922285, 0.033451423048973083, -0.018775926902890205)), Vector((0.0018669702112674713, 0.07865209132432938, -0.003352719359099865)), Vector((0.0018669702112674713, 0.07865209132432938, 0.0005737065803259611)), Vector((-0.001565549522638321, 0.07858095318078995, 0.0005737065803259611)), Vector((-0.001565549522638321, 0.07858095318078995, -0.003352719359099865))]
    
	
	
    edges = []
    faces = [[2, 3, 1, 0], [6, 7, 5, 4], [7, 3, 1, 5], [8, 9, 11, 10], [10, 11, 15, 14], [14, 15, 13, 12], [12, 13, 18, 19], [10, 14, 12, 8], [15, 11, 9, 13], [16, 19, 23, 20], [9, 8, 16, 17], [8, 12, 19, 16], [13, 9, 17, 18], [23, 22, 21, 20], [17, 16, 20, 21], [18, 17, 21, 22], [19, 18, 22, 23]]

    mesh = bpy.data.meshes.new(name="Lap Path")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)

#Gravity Paths
def add_object1(self, context):


    verts = [Vector((-0.25, 0.0, -0.25)), Vector((-0.25, 0.0, 0.25)), Vector((0.25, 0.0, -0.25)), Vector((0.25, 0.0, 0.25)), Vector((-0.25, 0.0024999999441206455, -0.25)), Vector((-0.25, 0.0024999999441206455, 0.25)), Vector((0.25, 0.0024999999441206455, -0.25)), Vector((0.25, 0.0024999999441206455, 0.25)), Vector((0.009097770787775517, 0.037538301199674606, -0.011082690209150314)), Vector((0.009097770787775517, 0.037538301199674606, 0.008303677663207054)), Vector((0.010442008264362812, 0.0007872602436691523, -0.012137915939092636)), Vector((0.010442008264362812, 0.0007872602436691523, 0.009358905255794525)), Vector((-0.007850013673305511, 0.03718690574169159, -0.011082690209150314)), Vector((-0.007850013673305511, 0.03718690574169159, 0.008303677663207054)), Vector((-0.008350776508450508, 0.00039761816151440144, -0.012137915939092636)), Vector((-0.008350776508450508, 0.00039761816151440144, 0.009358905255794525)), Vector((0.01586453802883625, 0.03408169001340866, -0.018775926902890205)), Vector((0.01586453802883625, 0.03408169001340866, 0.015996914356946945)), Vector((-0.01453429739922285, 0.033451423048973083, 0.015996914356946945)), Vector((-0.01453429739922285, 0.033451423048973083, -0.018775926902890205)), Vector((0.0018669702112674713, 0.07865209132432938, -0.003352719359099865)), Vector((0.0018669702112674713, 0.07865209132432938, 0.0005737065803259611)), Vector((-0.001565549522638321, 0.07858095318078995, 0.0005737065803259611)), Vector((-0.001565549522638321, 0.07858095318078995, -0.003352719359099865))]
    
	
	
    edges = []
    faces = [[2, 3, 1, 0], [6, 7, 5, 4], [7, 3, 1, 5], [8, 9, 11, 10], [10, 11, 15, 14], [14, 15, 13, 12], [12, 13, 18, 19], [10, 14, 12, 8], [15, 11, 9, 13], [16, 19, 23, 20], [9, 8, 16, 17], [8, 12, 19, 16], [13, 9, 17, 18], [23, 22, 21, 20], [17, 16, 20, 21], [18, 17, 21, 22], [19, 18, 22, 23]]

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
        
        bpy.ops.transform.resize(value=(0.25, 0.25, 0.25))
    
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


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportSomeData.bl_idname, text="Mario Kart 8 XML Path Exporter")

	
	
def register():


    bpy.utils.register_class(Add_LapPath)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.INFO_MT_mesh_add.append(add_object_button)
    bpy.utils.register_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.append(menu_func_export)
    bpy.utils.register_class(Add_GravityPath)
    bpy.utils.register_class(Add_GlidePath)
    bpy.utils.register_class(OBJECT_OT_HEMI)
    bpy.utils.register_class(ObjectPanel)
    bpy.utils.register_class(MySettings)
    bpy.utils.register_class(PathSETTINGS)
    bpy.utils.register_class(gliderselect)
    bpy.utils.register_class(gravityselect)
    bpy.utils.register_class(lapselect)
    bpy.utils.register_class(replayselect)
    bpy.utils.register_class(introselect)
    bpy.utils.register_class(enemyselect)
    bpy.types.Scene.my_prop
    bpy.utils.register_class(Laptogravity)



def unregister():
    bpy.utils.unregister_class(Add_LapPath)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)
    bpy.utils.unregister_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)
    bpy.utils.unregister_class(Add_GravityPath)
    bpy.utils.unregister_class(Add_GlidePath)
    bpy.utils.unregister_class(OBJECT_OT_HEMI)
    bpy.utils.unregister_class(ObjectPanel)
    bpy.utils.unregister_class(MySettings)
    bpy.utils.unregister_class(PathSETTINGS)
    bpy.utils.unregister_class(gliderselect)
    bpy.utils.unregister_class(gravityselect)
    bpy.utils.unregister_class(lapselect)
    bpy.utils.unregister_class(replayselect)
    bpy.utils.unregister_class(introselect)
    bpy.utils.unregister_class(enemyselect)
    del bpy.types.Scene.my_prop
    bpy.utils.unregister_class(Laptogravity)

    


if __name__ == "__main__":
    register()



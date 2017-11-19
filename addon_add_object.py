bl_info = {
    "name": "A MK8 Path Tool",
    "author": "KillzXGaming, Lots of help from MasterVermilli0n",
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


			
			
	

class Add_LapPath(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_object"
    bl_label = "Lap Path"
    bl_options = {'REGISTER', 'UNDO'}

    scale = FloatVectorProperty(
            name="scale",
            default=(0.25, 0.25, 0.5),
            subtype='TRANSLATION',
            description="scaling",
            )
    



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
		
        activeObject.data.polygons[2].select = True  #Active polygon
        
        me = obj.data
        
        for f in me.polygons:
         f.material_index = f.index % 3

        mat1 = bpy.data.materials.new(name="Back") #set new material to variable
        activeObject.data.materials.append(mat1) #add the material to the object  
        bpy.context.object.active_material_index = 1 #Active the second material
        bpy.context.object.active_material.diffuse_color = (0, 1, 0.076676) #Color Green
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


    


def unregister():
    bpy.utils.unregister_class(Add_LapPath)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)
    bpy.utils.unregister_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

    


if __name__ == "__main__":
    register()



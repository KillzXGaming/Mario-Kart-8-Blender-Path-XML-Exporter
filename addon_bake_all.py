bl_info = {
    "name": "Bake All",
    "author": "Alfonso Annarumma",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "location": "Toolshelf > Layers Tab",
    "description": "Bake All the selected Mesh to a new textures",
    "warning": "",
    "wiki_url": "",
    "category": "Bake",
    }


import bpy
import os
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import StringProperty, BoolProperty, IntProperty, CollectionProperty, BoolVectorProperty, PointerProperty

class BakeAllProp(PropertyGroup):
    
    float = BoolProperty (name="32 bit Float")
    
    res_x = IntProperty (name="X",
     description="X Resolution of the image", 
     default=1024, 
     min=1, 
     max=2**31-1, 
     soft_min=1, 
     soft_max=1024*4, 
     step=1, 
     subtype='PIXEL')
     
    res_y = IntProperty (name="Y",
     description="Y Resolution of the image", 
     default=1024, 
     min=1, 
     max=2**31-1, 
     soft_min=1, 
     soft_max=1024*4, 
     step=1, 
     subtype='PIXEL')
     
    #name = StringProperty(name="Layer Name")
    save_image = BoolProperty(name="Save Image", default=False)

    image_dir_path = StringProperty(
    name="Directory Path", 
    description="The directory to save the baked image", 
    subtype="DIR_PATH",
    default="//")




class BakeAll(bpy.types.Operator):
    bl_idname = "object.bake_all"
    bl_label = "Bake All"

    def execute(self, context):
        scn = context.scene
        
        materials = set()
        #bake_pass = 'AO'
        #scn.cycles.samples = bake_pass.samples
        res_x = scn.bakeallprop.res_x
        res_y = scn.bakeallprop.res_y
        float = scn.bakeallprop.float
        
        image_dir_path = scn.bakeallprop.image_dir_path
        save_image = scn.bakeallprop.save_image
        
        directory = bpy.path.abspath(image_dir_path)
        if not os.path.exists(directory) and save_image:
            os.makedirs(directory)
        for o in context.selected_objects:
            
            if o.type == 'MESH':
                #controllo che ci siano degli slot pieni
                if o.material_slots.items():
                    
                    
                    #controllo se c'è un materiale assegnato al primo slot
                    if o.material_slots[0].material == False:
                        
                        #se non c'è un materiale lo creo e lo assegno allo slot 0
                        mat = bpy.data.materials.new(name=o.name+"Material_bake")
                        o.material_slots[0].material = mat
                    
                    #se c'è un materiale lo prelevo e lo metto nella variabile mat
                    else:
                        if o.material_slots[0].material.users >1:
                            mat = o.material_slots[0].material.copy()    
                            o.material_slots[0].material = mat
                        else:
                            mat = o.material_slots[0].material
                             
                
                else:
                    #se non c'è neanche uno slot, creo un material e lo appendo all'oggetto
                                   
                    mat = bpy.data.materials.new(name=o.name+"Material_bake")
                    o.data.materials.append(mat)
                    
                
                
                #setto come materiale attivo il primo
                o.active_material_index = 0
                
                #abilito i nodi nel materiali e assegno l'immagine ad un nodo
                bpy.data.materials[mat.name].use_nodes = True
                bake_type = context.scene.cycles.bake_type
                node_tree = bpy.data.materials[mat.name].node_tree
                
                img_name = bake_type+"_"+o.name+"_bake"
                node_name = bake_type+"bake_all_image_jxk"
                filepath = image_dir_path+img_name
                print(filepath)
                print(float)
                if node_name in node_tree.nodes:
                    node = node_tree.nodes[node_name]
                    node.image.filepath = filepath+"."+node.image.file_format
                    if not node.image.has_data:
                        node.image = bpy.data.images.new(img_name, res_x, res_y, float_buffer=float)
                        node.image.filepath = filepath+"."+node.image.file_format
                    #image = bpy.data.images[img_name]
                else:
                    node = node_tree.nodes.new("ShaderNodeTexImage")
                    
                    node.name = node_name
                    
                    image = bpy.data.images.new(img_name, res_x, res_y)
                    image.filepath = filepath+"."+image.file_format
                    node.image = image
                    
                
                    
                   
                        
                
                node.select = True
                node_tree.nodes.active = node
                
            else:
                o.select = False
            
            
                
            
            #materials = materials.union(set(map(lambda x: (o.name, x.name), bpy.data.objects[o.name].data.materials)))

        #bpy.ops.object.select_all("EXEC_SCREEN", action="DESELECT")
        
        bake_type = context.scene.cycles.bake_type
        
        if save_image:
            
            bpy.ops.object.bake(type = bake_type)
            bpy.ops.object.bake_all_save_image()
        
        else:    
            bpy.ops.object.bake("INVOKE_SCREEN",type = bake_type)
        
        
        
       
        
        
        return {'FINISHED'}
    
#    def execute(context):
#        if save_image:
#            bpy.ops.object.object.bake_all_save_image()
#        return {'FINISHED'}
#                    
class BakeAllSaveImage(bpy.types.Operator):
    """Save All baked image"""
    bl_idname = "object.bake_all_save_image"
    bl_label = "Save Image"

    

    def execute(self, context):
        images = bpy.data.images
        scene = context.scene
        image_dir_path = scene.bakeallprop.image_dir_path
        
        
        for img in images:
            
            if "_bake" in img.name and img.users == 1 and img.has_data:
                
                
                #ext = "."+img.file_format
                
                #img.filepath = image_dir_path+img.name+ext
                
                img.save()
            
                
                       
    

        return {'FINISHED'}
    
        
class BakeAllPanel(bpy.types.Panel):
    """Panel for Bake All"""
    bl_label = "Bake All"
    bl_idname = "RENDER_PT_Bake_All"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        obj = context.object
        prop = context.scene.bakeallprop
        
        
        row = layout.row()
        
        row.prop(scene.cycles, "samples")
        
        
        row = layout.row()
        col =row.column(align=True)
        col.label(text="Image Resolution:")
        col.prop(prop, "res_x")
        col.prop(prop, "res_y")
        col.prop(prop, "float")
        
        
        
        if bpy.data.is_saved:
            enable = True
            
        else:
            enable = False
        
        
        
        row = layout.row()
        row.operator("object.bake_all")
        
        
        
        row = layout.row()
        row.enabled = enable
        row.prop(prop, "save_image", text="Auto Save images")
        
        if prop.save_image:
            
            row = layout.row()
            row.enabled = enable
            row.prop(prop, "image_dir_path")







def register():
    bpy.utils.register_class(BakeAll)
    bpy.utils.register_class(BakeAllPanel)
    bpy.utils.register_class(BakeAllProp)
    bpy.utils.register_class(BakeAllSaveImage)
    
    bpy.types.Scene.bakeallprop = PointerProperty(type=BakeAllProp)

def unregister():
   
    bpy.utils.unregister_class(BakeAll)
    bpy.utils.unregister_class(BakeAllSaveImage)
    bpy.utils.unregister_class(BakeAllPanel)
    bpy.utils.unregister_class(BakeAllProp)
    del bpy.types.Scene.bakeallprop


if __name__ == "__main__":
    register()
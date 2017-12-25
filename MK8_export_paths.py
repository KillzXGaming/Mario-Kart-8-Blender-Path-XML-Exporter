import bpy
import mathutils
import math
import addon_add_object

 







def write_some_data(context, filepath, use_some_setting):
    print("running write_some_data...")
    f = open(filepath, 'w', encoding='utf-8')
 
    Scene = bpy.context.scene  
    
    if use_some_setting.NOLOOP == True:	
        print("Paths will not loop!")
    else:
        print("Paths will loop!")
	


    layerIndecies = []
        
    objects = sorted(bpy.context.scene.objects, key=lambda ob: ob.name)
    
	
    def Coordinates():
        if obj.type != 'EMPTY': 
             ScaleX = obj.scale.x * 2
             ScaleY = obj.scale.y * 2
             ScaleZ = obj.scale.z * 2
        else:
            ScaleX = obj.scale.x
            ScaleY = obj.scale.y
            ScaleZ = obj.scale.z
 
        zscale = round(ScaleZ, 3)
        yscale = round(ScaleX, 3)
        xscale = round(ScaleX, 3)
        XRot = round(obj.rotation_euler.x, 3)
        ZRot = round(obj.rotation_euler.z, 3)
        YRot = round(-obj.rotation_euler.y,3)  # Invert the dumb Y coords so positive is negitive, negitive is positive
        xloc = round(obj.location.x, 3)
        yloc = round(-obj.location.y, 3)  # Invert the dumb Y coords so positive is negitive, negitive is positive
        zloc = round(obj.location.z, 3)
 
        # Write Coordinates from lap paths selected
        f.write('\n          <Rotate X="')
        f.write(str(XRot) + 'f" Y="' + str(ZRot) + 'f" Z="' + str(YRot) + 'f" />')
        f.write('\n          <Scale X="')
        f.write(str(xscale) + 'f" Y="' + str(zscale) + 'f" Z="0.0f" />')
        f.write('\n          <Translate X="')
        f.write(str(xloc) + 'f" Y="' + str(zloc) + 'f" Z="' + str(yloc) + 'f" />')
        f.write('\n        </value>\n')

    def ReturnCoordinates():
        mat_rot = obj.rotation_euler.to_matrix() #matricies will write based on euler rotation!

        mat = mat_rot.to_4x4() #Lets turn this into a grid!
        
			#These are for tangents
        matXR = mat[1][0] #Write second row, first column
        matYR = mat[1][1] #Write second row, second column
        matZR = mat[1][2] #Write second row, third column
		
        matX = round(matXR, 3)
        matY = round(matYR, 3)
        matZ = round(matZR, 3)

        #These are for normals
			
        matXRN = mat[2][0] #Write second row, first column
        matYRN = mat[2][1] #Write second row, second column
        matZRN = mat[2][2] #Write second row, third column
		
        matXN = round(matXRN, 3)
        matYN = round(matYRN, 3)
        matZN = round(matZRN, 3)
        f.write('        <value JugemIndex="-1" JugemPath="-1" ReturnType="-1" hasError="0">')
 
        xloc = round(obj.location.x, 3)
        yloc = round(-obj.location.y, 3)
        zloc = round(obj.location.z, 3)
 
        # Write Coordinates from lap paths selected
        f.write('\n          <Normal X="' + str(matXN) + 'f" Y="' + str(matZN) + 'f" Z="' + str(matYN) + 'f" />')
        f.write('\n          <Position X="')
        f.write(str(xloc) + 'f" Y="' + str(zloc) + 'f" Z="' + str(yloc) + 'f" />')
        f.write('\n          <Tangent X="' + str(matX) + 'f" Y="' + str(matZ) + 'f" Z="' + str(matY) + 'f" />')
        f.write('\n        </value>\n')

    def LoopedPathPTIDS():

        f.write('          <NextPt type="array">\n')

        var = range(0, 9)

        # Write next lap path group ID
				# Use UI setting if specified!
				
				
				#Todo range these values
				
        if obj.has_GroupConnection1 == True:
            PathIDsOverride()

	
        else:
            f.write('            <value PathId="')  # write the next group ID

            if obj == selectedObjects[-1]:
                if layerIndex == layerIndecies[-1]:
                    f.write('0')
                else:
                    f.write('%d' % (groupIndex + 1))
            else:
                f.write('%d' % groupIndex)

        # Write next lap path ID
            f.write('" PtId="')

            if obj == selectedObjects[-1]:
                f.write('0" />\n')
            else:
                f.write('%d" />\n' % (objID + 1))

            f.write('          </NextPt>\n')

        # Write previous lap path group ID
				
				

        f.write('          <PrevPt type="array">\n')
        f.write('            <value PathId="')  # write the next group ID
				
        if obj == selectedObjects[0]:
            if layerIndex == layerIndecies[0]:
                f.write('%d' %  (len(layerIndecies) - 1))
            else:
                f.write('%d' % (groupIndex - 1))
        else:
            f.write('%d' % groupIndex)

    # Write previous lap path ID
        f.write('" PtId="')

        if obj == selectedObjects[0]:
                f.write('%d" />' % (len(sOIPL) - 1))
        else:
            f.write('%d" />' % (objID - 1))

        f.write('\n          </PrevPt>')
	
    def NoLoopPathPTIDS():
        if obj == selectedObjects[-1]:
             f.write('          <NextPt type="array" />\n')
        else:
            f.write('          <NextPt type="array">\n')

        if obj == selectedObjects [-1]:
                f.write('')  # Last Object does not loop so has no ID after
        else:
                f.write('            <value PathId="')  # write the next group ID
                            
        if obj == selectedObjects[-1]:
            if layerIndex == layerIndecies[-1]:
                f.write('')
            else:
                f.write('%d' % (groupIndex + 1))
        else:
            f.write('%d' % groupIndex)
 
        if obj == selectedObjects[-1]:
                f.write('')
                                    
        # Write next lap path ID
        if obj == selectedObjects[-1]:
            f.write('')  # Last Object does not loop so has no ID after
        else:
            f.write('" PtId="')
 
        if obj == selectedObjects[-1]:
            f.write('')
        else:
            f.write('%d" />' % (objID + 1))
 
        if obj == selectedObjects[-1]:
            f.write('')  # Last Object does not loop so has no ID after
        else:
            f.write('\n          </NextPt>\n')
 
        # Write previous lap path group ID
        if obj == selectedObjects[0]:
                f.write('          <PrevPt type="array" />')
        else:
                f.write('          <PrevPt type="array">')
                    
        if obj == selectedObjects [0]:
            f.write('')  # Last Object does not loop so has no ID before
        else:
            f.write('\n            <value PathId="')  # write the next group ID
 
        if obj == selectedObjects[0]:
                f.write('')
        else:
            f.write('%d' % groupIndex)
 
        # Write previous lap path ID
        if obj == selectedObjects[0]:
            f.write('')  # Last Object does not loop so has no ID before
        else:
            f.write('" PtId="')
 
        if obj == selectedObjects[0]:
            f.write('')
        else:
            f.write('%d" />' % (objID - 1))
                            
                            
        if obj == selectedObjects[0]:
            f.write('')  # Last Object does not loop so has no ID before
        else:
             f.write('\n          </PrevPt>')
 
    def PathIDsOverride():
        if obj == selectedObjects[-1]:		
            f.write('            <value PathId="' + str(obj.GroupConnection1) + '"PtId="0" />\n')  # write the next group ID

			
			
	     #If the previous group specifices the group ID, use that group's index

			
			
        if layerIndex == layerIndecies[2]:
            CustomsOIPL = [ob for ob in objects if ob.layers[layerIndecies[obj.GroupConnection2 - 1]] and  "lap" in ob.name.lower() and ob.select]
            f.write('')
            f.write('          <PrevPt type="array">\n')
            f.write('            <value PathId="')  # write the next group ID
    				
            if obj == selectedObjects[0]:
                if layerIndex == layerIndecies[0]:
                    f.write('%d' %  (len(layerIndecies) - 1))
                else:
                    f.write('%d' % (groupIndex - 1))
            else:
                f.write('%d' % groupIndex)		
		
        # Write previous lap path ID		
		
            f.write('" PtId="')

            if obj == selectedObjects[0]:
                    f.write('%d" />' % (len(CustomsOIPL) - 1))
            else:
                f.write('%d" />' % (objID - 1))

            f.write('\n          </PrevPt>')
 
 #Enemy Paths
    for layerIndex in range(20):  # loop from layer 0 to layer 19
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and  "lap" in ob.name.lower() and ob.select]
        if selectedObjects:
            layerIndecies.append(layerIndex)
 
    for groupIndex, layerIndex in enumerate(layerIndecies):  # loop from first group to last group
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and  "lap" in ob.name.lower() and ob.select] #No enemy path objects yet!
        sOIPL = [ob for ob in objects if ob.layers[layerIndecies[groupIndex - 1]] and  "lap" in ob.name.lower() and ob.select]
		
        # Write the start of enemy path group
		
        if layerIndex == layerIndecies[0]:
            f.write('  <EnemyPath type="array">\n')
		
        if layerIndex != layerIndecies[0]:
            f.write('    </value>\n')
        f.write('    <value UnitIdNum="38">')
        f.write('\n      <PathPt type="array">\n')
 
        for objID, obj in enumerate(selectedObjects):
            f.write('        <value BattleFlag="' + str(obj.IntBattleFlag) + '" PathDir="' + str(obj.IntPathDir) + '" Priority="' + str(obj.PriorityEnum) + '">\n')
	
            if use_some_setting.NOLOOP == False:
                LoopedPathPTIDS()

				#NO LOOP
            else:
                NoLoopPathPTIDS()
            
            #Write Coordinates for Translation, and Rotation
            Coordinates()

 
        f.write('      </PathPt>\n')
 

 
        if layerIndex != layerIndecies[-1]:
            f.write('')
        else:
            f.write('    </value>\n')
            f.write('  </EnemyPath>\n')
 
 
    objects = sorted(bpy.context.scene.objects, key=lambda ob: ob.name)
 
    layerIndecies = []
 #Intro Paths
    for layerIndex in range(20):  # loop from layer 0 to layer 19
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and  "intro" in ob.name.lower() and ob.select]
 
        if selectedObjects:
            layerIndecies.append(layerIndex)
 
    for groupIndex, layerIndex in enumerate(layerIndecies):  # loop from first group to last group
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and ob.select]
        sOIPL = [ob for ob in objects if ob.layers[layerIndecies[groupIndex - 1]] and  "lap" in ob.name.lower() and ob.select]

        # Write the start of intro path group
		
        if layerIndex == layerIndecies[0]:
            f.write('  <IntroCamera type="array">\n')
		
 
        for objID, obj in enumerate(selectedObjects):
            f.write('    <value CameraNum="' + str(obj.IntCameraNumIntro) + '" CameraTime="' + str(obj.IntCameraTimeIntro) + '" CameraType="' + str(obj.FollowCameraTypeIntro) + '" Camera_AtPath="' + str(obj.IntCamera_AtPathIntro) + '" Camera_Path="' + str(obj.IntCamera_PathIntro) + '" Fovy="' + str(obj.IntFovyIntro) + '" Fovy2="' + str(obj.IntFovy2Intro) + '" FovySpeed="' + str(obj.IntFovySpeedIntro) + '" UnitIdNum="' + str(obj.IntUnitIdNumIntro) + '">')
			
            
            #Write Coordinates for Scale, Translation, and Rotation
            Coordinates()
 

 
        f.write('  </IntroCamera>\n')	
 

    objects = sorted(bpy.context.scene.objects, key=lambda ob: ob.name)
 
    layerIndecies = []
 #Item Paths
    for layerIndex in range(20):  # loop from layer 0 to layer 19
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and  "lap" in ob.name.lower() and ob.select]
 
        if selectedObjects:
            layerIndecies.append(layerIndex)
 
    for groupIndex, layerIndex in enumerate(layerIndecies):  # loop from first group to last group
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and  "lap" in ob.name.lower() and ob.select]
        sOIPL = [ob for ob in objects if ob.layers[layerIndecies[groupIndex - 1]] and  "lap" in ob.name.lower() and ob.select]

        # Write the start of item path group
		
        if layerIndex == layerIndecies[0]:
            f.write('  <ItemPath type="array">\n')
		
        if layerIndex != layerIndecies[0]:
            f.write('    </value>\n')
        f.write('    <value UnitIdNum="38">')
        f.write('\n      <PathPt type="array">\n')
 
        for objID, obj in enumerate(selectedObjects):
            f.write('        <value Hover="' + str(obj.HoverEnum) + '" ItemPriority="' + str(obj.ItemPriorityEnum) + '" SearchArea="' + str(obj.SearchAreaEnum) + '">\n')

 
            if use_some_setting.NOLOOP == False:
                LoopedPathPTIDS()

				#NO LOOP
            else:
                NoLoopPathPTIDS()
            
            #Write Coordinates for Translation, and Rotation
            Coordinates()
 
        f.write('      </PathPt>\n')
 

 
        if layerIndex != layerIndecies[-1]:
            f.write('')
        else:
            f.write('    </value>\n')
            f.write('  </ItemPath>\n')

 
    objects = sorted(bpy.context.scene.objects, key=lambda ob: ob.name)
 
    layerIndecies = []
 #Lap Paths
    for layerIndex in range(20):  # loop from layer 0 to layer 19
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and  "lap" in ob.name.lower() and ob.select]
 
        if selectedObjects:
            layerIndecies.append(layerIndex)
 
    for groupIndex, layerIndex in enumerate(layerIndecies):  # loop from first group to last group
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and  "lap" in ob.name.lower() and ob.select]
        sOIPL = [ob for ob in objects if ob.layers[layerIndecies[groupIndex - 1]] and  "lap" in ob.name.lower() and ob.select]

 
        if layerIndex == layerIndecies[0]:
            f.write('  <LapPath type="array">')
            f.write('\n    <value LapPathGroup="-1" ReturnPointsError="false" UnitIdNum="62">')

 
        # Write the start of lap path group
        if layerIndex != layerIndecies[0]:
            f.write('    </value>')
		#Enable anti gravity if one is selected. 
        if obj.select and "gravity" in obj.name.lower():
                f.write('\n    <value LapPathGroup="-1" ReturnPointsError="false" UnitIdNum="62">')
                f.write('\n      <LapPath_GravityPath type="array">')
                f.write('\n        <value>0</value>') #Todo figure out what this value does???? May be group related
                f.write('\n      </LapPath_GravityPath>')
        f.write('\n      <PathPt type="array">\n')

 
 
		
        scene = context.scene
		
        for objID, obj in enumerate(selectedObjects):
		
            if use_some_setting.NOLOOP == False:
                if obj == selectedObjects[0]:
                    if layerIndex == layerIndecies[0]:
                      f.write('        <value CheckPoint="' + str(obj.IntCheckpoint) + '" ClipIdx="' + str(obj.IntClipIndx) + '" HeadLightSW="' + str(obj.HeadlightsEnum) + '" LapCheck="0" MapCameraFovy="' + str(obj.IntMapCameraFovy) + '" MapCameraY="' + str(obj.IntMapCameraY) + '" ReturnPosition="' + str(obj.IntReturnPosition) + '" SoundSW="' + str(obj.IntSoundSW) + '">\n')
                    else:
                        f.write('        <value CheckPoint="' + str(obj.IntCheckpoint) + '" ClipIdx="' + str(obj.IntClipIndx) + '" HeadLightSW="' + str(obj.HeadlightsEnum) + '" LapCheck="' + str(obj.IntLapCheck) + '" MapCameraFovy="' + str(obj.IntMapCameraFovy) + '" MapCameraY="' + str(obj.IntMapCameraY) + '" ReturnPosition="' + str(obj.IntReturnPosition) + '" SoundSW="' + str(obj.IntSoundSW) + '">\n')
                else:
                    f.write('        <value CheckPoint="' + str(obj.IntCheckpoint) + '" ClipIdx="' + str(obj.IntClipIndx) + '" HeadLightSW="' + str(obj.HeadlightsEnum) + '" LapCheck="' + str(obj.IntLapCheck) + '" MapCameraFovy="' + str(obj.IntMapCameraFovy) + '" MapCameraY="' + str(obj.IntMapCameraY) + '" ReturnPosition="' + str(obj.IntReturnPosition) + '" SoundSW="' + str(obj.IntSoundSW) + '">\n')
            else:
                  f.write('        <value CheckPoint="' + str(obj.IntCheckpoint) + '" ClipIdx="' + str(obj.IntClipIndx) + '" HeadLightSW="' + str(obj.HeadlightsEnum) + '" LapCheck="' + str(obj.IntLapCheck) + '" MapCameraFovy="' + str(obj.IntMapCameraFovy) + '" MapCameraY="' + str(obj.IntMapCameraY) + '" ReturnPosition="' + str(obj.IntReturnPosition) + '" SoundSW="' + str(obj.IntSoundSW) + '">\n')

				  

            if use_some_setting.NOLOOP == False:
                LoopedPathPTIDS()

				#NO LOOP
            else:
                NoLoopPathPTIDS()
            
            #Write Coordinates for Scale, Translation, and Rotation
            Coordinates()

        f.write('      </PathPt>\n')
        f.write('      <ReturnPoints type="array">\n')
 
        for obj in selectedObjects:
            ReturnCoordinates()
 
        f.write('      </ReturnPoints>\n')

        if layerIndex != layerIndecies[-1]:
            f.write('')
        else:
            f.write('    </value>\n')
            f.write('  </LapPath>\n')
	
	
	
    objects = sorted(bpy.context.scene.objects, key=lambda ob: ob.name)

	
    objactive = context.scene.objects.active
	
	
	
    

	
	
    # Add Extra Code here for Multiple Paths. Lap path IDs will reset for these.
 
    # So now we will search for layers in the scene and group them!
 
    objects = sorted(bpy.context.scene.objects, key=lambda ob: ob.name)
 
    layerIndecies = []
 #GCamera Paths
    for layerIndex in range(20):  # loop from layer 0 to layer 19
        selectedObjects  = [ob for ob in objects if ob.layers[layerIndex] and  "gravity" in ob.name.lower() and ob.select]
 
        if selectedObjects:
            layerIndecies.append(layerIndex)
        

 
 
    for groupIndex, layerIndex in enumerate(layerIndecies):  # loop from first group to last group
        selectedObjects  = [ob for ob in objects if ob.layers[layerIndex] and  "gravity" in ob.name.lower() and ob.select]
 
        # Write the start of lap path group
		
        if layerIndex == layerIndecies[0]:
            f.write('  <GCameraPath type="array">')


        if layerIndex != layerIndecies[-1]:
            f.write('    </value>')
                    
			
			
			
        f.write('\n    <value UnitIdNum="26">')
        f.write('\n      <PathPt type="array">\n')
 
        for objID, obj in enumerate(selectedObjects ):
            f.write('        <value>\n')

            NoLoopPathPTIDS()
            
            #Write Coordinates for Translation, and Rotation
            Coordinates()
 
        f.write('      </PathPt>\n')
 
        if layerIndex != layerIndecies[-1]:
            f.write('')
        else:
            f.write('    </value>\n')
            f.write('  </GCameraPath>\n')
	
	
	
    
 
    # Add Extra Code here for Multiple Paths. Lap path IDs will reset for these.
 
    # So now we will search for layers in the scene and group them!
 
    objects = sorted(bpy.context.scene.objects, key=lambda ob: ob.name)
 
    layerIndecies = []
 #Gravity paths
    for layerIndex in range(20):  # loop from layer 0 to layer 19
        selectedObjects  = [ob for ob in objects if ob.layers[layerIndex] and  "gravity" in ob.name.lower() and ob.select]
 
        if selectedObjects:
            layerIndecies.append(layerIndex)
        

 
 
    for groupIndex, layerIndex in enumerate(layerIndecies):  # loop from first group to last group
        selectedObjects  = [ob for ob in objects if ob.layers[layerIndex] and  "gravity" in ob.name.lower() and ob.select]
 
        # Write the start of lap path group
		
        if layerIndex == layerIndecies[0]:
            f.write('  <GravityPath type="array">')


        if layerIndex != layerIndecies[-1]:
            f.write('    </value>')
                    
			
			
			
        f.write('\n    <value UnitIdNum="70">')
        f.write('\n      <PathPt type="array">\n')
 
        for objID, obj in enumerate(selectedObjects ):
            f.write('        <value CameraHeight="' + str(obj.IntCameraHeight) + '" GlideOnly="' + str(obj.GlideOnlyEnum) + '" Transform="' + str(obj.GTransformEnum) + '">\n')

            NoLoopPathPTIDS()
            
            #Write Coordinates for Translation, and Rotation
            Coordinates()
 
        f.write('      </PathPt>\n')
 
        if layerIndex != layerIndecies[-1]:
            f.write('')
        else:
            f.write('    </value>\n')
            f.write('  </GravityPath>\n')
	
	
	
	
 
    # Add Extra Code here for Multiple Paths. Lap path IDs will reset for these.
 
    # So now we will search for layers in the scene and group them!
 
    objects = sorted(bpy.context.scene.objects, key=lambda ob: ob.name)
 
    layerIndecies = []
 #Glider Paths
    for layerIndex in range(20):  # loop from layer 0 to layer 19
        selectedObjects  = [ob for ob in objects if ob.layers[layerIndex] and  "glide" in ob.name.lower() and ob.select]
 
        if selectedObjects:
            layerIndecies.append(layerIndex)
 
    for groupIndex, layerIndex in enumerate(layerIndecies):  # loop from first group to last group
        selectedObjects  = [ob for ob in objects if ob.layers[layerIndex] and  "glide" in ob.name.lower() and ob.select]
 
        # Write the start of lap path group
        if layerIndex == layerIndecies[0]:
            f.write('  <GlidePath type="array">')
		
        if layerIndex != layerIndecies[-1]:
            f.write('    </value>')
			
			
        f.write('\n    <value GlideType="1" IsUp="true" UnitIdNum="0">')
        f.write('\n      <PathPt type="array">\n')
 
        for objID, obj in enumerate(selectedObjects ):
            f.write('        <value Cannon="' + str(obj.CannonEnum) + '">\n')

            if obj == selectedObjects [-1]:
                    f.write('          <NextPt type="array" />\n')
            else:
                    f.write('          <NextPt type="array">\n')

            NoLoopPathPTIDS()
            
            #Write Coordinates for Translation, and Rotation
            Coordinates()
 
 
        if layerIndex != layerIndecies[-1]:
            f.write('')
        else:
            f.write('    </value>\n')
            f.write('  </GlidePath>\n')

	

	
    #Look for Rays byaml tool and look for has_obj_path (Bool) and obj_path (Int) and determine what order to sort the obj paths!
	
	

	
 #ObjPaths 

    obj = (bpy.context.scene.objects)

 #These need to be per key frame! Each object seoerates the value entries!
    OBJPathEnabled = [ o for o in bpy.context.scene.objects if o.select  and "test" in o.name.lower()]
    Test = 'False'
 
    if Test == 'True':
        f.write('  <ObjPath type="array">\n')

        for obj in OBJPathEnabled:
            selectedObjectsPath  =  [key for key in keys]
                #These are for normals
    			
            LASTFRAME = keys[-1]
    	
            f.write('    <value IsClosed="false" PtNum="' + str(LASTFRAME) + '" SplitWidth="0.5f" UnitIdNum="6">')
            f.write('\n      <ObjPt type="path">')
    		
            
    		
    		#These need to be written for every frame between keyframes

            sce = bpy.context.scene
            ob = bpy.context.object
            my_frames = get_keyframes(selection)
    	
    	
            def print_details(obj_list):
                obj = bpy.context.active_object
                context = bpy.context

                mat_rot = obj.rotation_euler.to_matrix() #matricies will write based on euler rotation!

                mat = mat_rot.to_4x4() #Lets turn this into a grid!
                

                #These are for normals
    			
                matXRN = mat[2][0] #Write second row, first column
                matYRN = mat[2][1] #Write second row, second column
                matZRN = mat[2][2] #Write second row, third column
    		
                matXN = round(matXRN, 3)
                matYN = round(matYRN, 3)
                matZN = round(matZRN, 3)
    			
                XRot = round(obj_list.rotation_euler.x)
                ZRot = round(obj_list.rotation_euler.z)
                YRot = round(-obj_list.rotation_euler.y)
                xloc = round(obj_list.location.x, 2)
                yloc = round(-obj_list.location.y, 2)
                zloc = round(obj_list.location.z, 2)			
                f.write('\n        <point x="' + str(xloc) + 'f" y="' + str(zloc) + 'f" z="' + str(yloc) + 'f" nx="' + str(matXN) + 'f" ny="' + str(matZN) + 'f" nz="' + str(matYN) + 'f" val="0" />')
    		
    		
    		

            for key in range(my_frames[0], my_frames[len(my_frames)-1]+1):
                bpy.context.scene.frame_set(key)
                for obj in selection:
                    print_details(obj)

    		
    		
    		
            f.write('\n        </ObjPt>')
            f.write('\n      <PathPt type="array">\n')
    		
    		#These write for every keyframe instead!
    		
            for key in get_keyframes(selection):
                bpy.context.scene.frame_set(key)
                f.write('        <value Index="')
                f.write(str(key)) #Writes index for the flag
                f.write('" prm1="0f" prm2="0f">')
    			

    			
                XRot = round(obj.rotation_euler.x, 3)
                ZRot = round(obj.rotation_euler.z, 3)
                YRot = round(-obj.rotation_euler.y,3)
                xloc = round(obj.location.x, 3)
                yloc = round(-obj.location.y, 3)
                zloc = round(obj.location.z, 3)

    	
    		
     
                # Write Coordinates from item paths selected
                f.write('\n          <Rotate X="')
                f.write(str(XRot) + 'f" Y="' + str(ZRot) + 'f" Z="' + str(YRot) + 'f" />')
                f.write('\n          <Translate X="')
                f.write(str(xloc) + 'f" Y="' + str(zloc) + 'f" Z="' + str(yloc) + 'f" />')
                f.write('\n        </value>\n')
     
     
            f.write('      </PathPt>')
            f.write('\n    </value>\n')
        f.write('  </ObjPath>\n')



    # Add Extra Code here for Multiple Paths. Lap path IDs will reset for these.
 
    # So now we will search for layers in the scene and group them!
 
    objects = sorted(bpy.context.scene.objects, key=lambda ob: ob.name)
 
    layerIndecies = []
 #Replay Paths
    for layerIndex in range(20):  # loop from layer 0 to layer 19
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and  "replay" in ob.name.lower() and ob.select]
 
        if selectedObjects:
            layerIndecies.append(layerIndex)
 
    for groupIndex, layerIndex in enumerate(layerIndecies):  # loop from first group to last group
        selectedObjects = [ob for ob in objects if ob.layers[layerIndex] and ob.select]
 
        # Write the start of replay path group
		
        if layerIndex == layerIndecies[0]:
            f.write('  <ReplayCamera type="array">\n')
		
 
        for objID, obj in enumerate(selectedObjects):
            f.write('    <value AngleX="' + str(obj.IntAngleXReplay) + '" AngleY="' + str(obj.IntAngleYReplay) + '" AutoFovy="' + str(obj.AutoFovyEnumReplay) + '" CameraType="' + str(obj.CameraTypeEnumReplay) + '" Camera_Path="' + str(obj.IntCamera_PathReplay) + '" DepthOfField="' + str(obj.IntDepthOfFieldReplay) + '" Distance="' + str(obj.IntDistanceReplay) + '" Follow="' + str(obj.FollowEnumReplay) + '" Fovy="' + str(obj.IntFovyReplay) + '" Fovy2="' + str(obj.IntFovy2Replay) + '" FovySpeed="' + str(obj.IntFovySpeedReplay) + '" Group="' + str(obj.IntGroupReplay) + '" Pitch="' + str(obj.IntPitchReplay) + '" Roll="' + str(obj.IntRollReplay) + '" UnitIdNum="' + str(obj.IntUnitIdNumReplay) + '" Yaw="' + str(obj.IntYawReplay) + '" prm1="' + str(obj.Intprm1Replay) + '" prm2="' + str(obj.Intprm2Replay) + '">')
            
            #Write Coordinates for Scale, Translation, and Rotation
            Coordinates()
 

 
        f.write('  </ReplayCamera>\n')	

	
    f.close()
 
    return {'FINISHED'}
 
 

 
# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
 
 
class ExportSomeData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Some Data"
 
    # ExportHelper mixin class uses this
    filename_ext = "course_muunt_PATHS.xml"
 
    filter_glob = StringProperty(
        default=".xml",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
 
    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.

 
    NOLOOP =  bpy.props.BoolProperty(name="Do Not Loop Paths", description="Test2", default=False)
 
 

 
    def execute(self, context):
        return write_some_data(context, self.filepath, self.properties)
 
 
# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportSomeData.bl_idname, text="Mario Kart 8 XML Path Exporter")
 
 
def register():
    bpy.utils.register_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.append(menu_func_export)
 
 
def unregister():
    bpy.utils.unregister_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)
 
 
if __name__ == "__main__":
    register()
 
    # test call
    bpy.ops.export_test.some_data('INVOKE_DEFAULT')

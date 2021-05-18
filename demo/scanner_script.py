import bpy
import sys
sys.path.append(r"D:\git\blainder-range-scanner")
import range_scanner

def remove(target) -> None:
    if isinstance(target, bpy.types.Object):
        if isinstance(target.data, bpy.types.Mesh):
            bpy.data.meshes.remove(target.data, do_unlink=True)
        elif isinstance(target.data, bpy.types.Camera):
            bpy.data.cameras.remove(target.data, do_unlink=True)
        elif isinstance(target.data, bpy.types.PointLight):
            bpy.data.lights.remove(target.data, do_unlink=True)
        else:
            pass
    elif isinstance(target, bpy.types.ParticleSettings):
        bpy.data.particles.remove(target, do_unlink=True)
    elif isinstance(target, bpy.types.Collection):
        bpy.data.collections.remove(target, do_unlink=True)
    elif isinstance(target, bpy.types.Material):
        bpy.data.materials.remove(target, do_unlink=True)
    elif isinstance(target, bpy.types.Mesh):
        bpy.data.meshes.remove(target, do_unlink=True)
    else:
        pass


def clean() -> None:
    bpy.context.scene.cursor.location = (0, 0, 0)
    bpy.context.scene.frame_set(0)
    for data_attr in ["meshes", "objects", "cameras", "particles", "collections", "materials", ]:
        for data in getattr(bpy.data, data_attr):
            try:
                remove(data)
            except Exception as e:
                print("clean->remove(): ", e)
                

def create_camera() -> bpy.types.Object:
    camera_data = bpy.data.cameras.new(name='Camera')
    camera_object = bpy.data.objects.new('Camera', camera_data)
    bpy.context.scene.collection.objects.link(camera_object)
    bpy.context.scene.camera = camera_object
    camera_object.location = (0, -3.0, 3)
    camera_object.rotation_euler = (0.785, 0, 0)
    return camera_object
                
                
def build_scene() -> None:
    bpy.ops.mesh.primitive_monkey_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
    target = bpy.context.object
    mat = bpy.data.materials.get("Material")
    if mat is None:
        # create material
        mat = bpy.data.materials.new(name="Material")

    # Assign it to object
    if target.data.materials:
        # assign to 1st material slot
        target.data.materials[0] = mat
    else:
        # no slots
        target.data.materials.append(mat)
        
    camera = create_camera()
    bpy.context.view_layer.update()


def kinect_v1():
    try:
        range_scanner.ui.user_interface.register()
    except Exception as e:
        pass
    
    try:
        range_scanner.ui.user_interface.scan_static(
            bpy.context, 

            scannerObject=bpy.context.scene.objects["Camera"],

            resolutionX=320, fovX=57, resolutionY=240, fovY=43, resolutionPercentage=100,

            reflectivityLower=0.0, distanceLower=0.8, reflectivityUpper=0.0, distanceUpper=4, maxReflectionDepth=4,
            
            enableAnimation=False, frameStart=1, frameEnd=1, frameStep=1, frameRate=1,

            addNoise=False, noiseType='gaussian', mu=0.0, sigma=0.01, noiseAbsoluteOffset=0.0, noiseRelativeOffset=0.0,

            simulateRain=False, rainfallRate=0.0, 

            addMesh=True,

            exportLAS=False, exportHDF=False, exportCSV=False, exportYCB=False, exportSingleFrames=False,
            exportRenderedImage=False, exportSegmentedImage=False, exportPascalVoc=False, exportDepthmap=False, depthMinDistance=0.0, depthMaxDistance=5.0, 
            dataFilePath="//output", dataFileName="outputfile",
            
            debugLines=False, debugOutput=False, outputProgress=False, measureTime=False, singleRay=False, destinationObject=None, targetObject=None
        )
    except Exception as e:
        print("scan_static(): ", e)
        
    try:
        range_scanner.ui.user_interface.unregister()
    except Exception as e:
        pass
    

if __name__ == '__main__':
    clean()
    build_scene()
    kinect_v1()
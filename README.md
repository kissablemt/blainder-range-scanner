# Range scanner simulation for Blender

Forked from [ln-12/blainder-range-scanner](https://github.com/ln-12/blainder-range-scanner)

## Modification
### Better Adaptation of Script
Before modifying `range_scanner/scanners/generic.py`, running `blender -P scanner_script.py` will cause error.
> line301 ~~`mode = bpy.context.area.type`~~ 
> 
> line304 ~~`bpy.context.area.type = "VIEW_3D"`~~ 
> 
> line393 ~~`bpy.context.area.type = mode`~~ 

### Add Custom Properties
These two properties have low versatility.
> ~~`hit.categoryID`~~  
> 
> ~~`hit.partID`~~ 


Add the properties to the objects inside Blender.
For example:
> ```python
> obj = bpy.data.objects["Some Object"]
> obj["cls_index"] = "<object class>" # Semantic Segmentation
> obj["object_id"] = "<object ID>" # Instance Segmentation
> ```

The object of the hit object can be obtained through the scanned points.

`closestHit` is the hit point in `range_scanner/scanners/lidar.py`.
Use the `target` attribute to get all the attributes of the object. 
> ```python
> target = closestHit.target # getattr(closestHit, "target")
> print(target["cls_index"]) # output <object class>
> print(target["object_id"]) # output <object ID>
> ```

### Add YCB-Video Exporter
- [YoungXIAO13/ObjectPoseEstimationSummary](https://github.com/YoungXIAO13/ObjectPoseEstimationSummary)
- [PoseCNN](https://rse-lab.cs.washington.edu/projects/posecnn/)
- [yuxng/YCB_Video_toolbox](https://github.com/yuxng/YCB_Video_toolbox)
- [位姿估计数据集 YCB-Video Dataset](https://zhuanlan.zhihu.com/p/89951893)

Blender matrix transform: `range_scanner/export/matrix.py`   
YCB-Video Annotation Exporter: `range_scanner/export/export_ycb.py` 

<br /><br />

## Introduction & Usage
The detail is here 👉 [ln-12/blainder-range-scanner](https://github.com/ln-12/blainder-range-scanner/blob/main/README.md)
<br /><br />

## Demo
1. Modify the module search path in the `scanner_script.py`
2. Run `blender -P scanner_script.py`

![Emitter](images/demo.jpg)
<br /><br />

import bpy
import bmesh
import numpy
import random as rand

try:
    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
except:
    _ = ""
    
sx, sy, sz = 10, 10, 10
plane = numpy.arange(sx * sy).reshape(sy, -1)



bpy.ops.mesh.primitive_grid_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(sx, sy, sz))
context = bpy.context
if context.object:
    bpy.ops.object.mode_set()
    

ob = context.object
me = ob.data
bpy.ops.object.mode_set(mode = 'EDIT')
bm = bmesh.from_edit_mesh(me)

bm.faces.ensure_lookup_table()
for i, f in enumerate(bm.faces):
    if f.select :
        f.select = False
        
spec_a, spec_b = 3,3
x_length = numpy.median(range(sx))
y_length = numpy.median(range(sy))


# need to spit plane into 4 quadrants
quadrants = numpy.array([
    plane[:sy // 2, :sy // 2],
    plane[:sy // 2, sx // 2:],
    plane[sx // 2:, :sy // 2],
    plane[sx // 2:, sx // 2:],
])

indices = []
h_sx = sx//2
h_sy = sy//2
for i, quadrant in enumerate(quadrants):
    rot_quadrant = numpy.rot90(quadrant, i)
    if i > 1:
        rot_quadrant = numpy.rot90(quadrant, -i+1)
    zero = rot_quadrant[h_sx-3:h_sx, h_sy-3:h_sy]
    print()
    print(zero)
    print()


for indice in numpy.array(indices).flatten():
    bm.faces[indice].select = True

#done editing, restore edit mode if needed
bpy.ops.object.mode_set(mode = 'EDIT')

#bpy.ops.mesh.extrude_context_move(MESH_OT_extrude_context={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.653437), "orient_axis_ortho":'X', "orient_type":'NORMAL', "orient_matrix":((0.316228, -0.948683, 0), (0.948683, 0.316228, 0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":True, "use_accurate":False, "use_automerge_and_split":False})
#bpy.ops.mesh.extrude_context_move(MESH_OT_extrude_context={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.653437), "orient_axis_ortho":'X', "orient_type":'NORMAL', "orient_matrix":((0.316228, -0.948683, 0), (0.948683, 0.316228, 0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(True, True, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":True, "use_accurate":False, "use_automerge_and_split":False})
#bpy.ops.mesh.extrude_context_move(MESH_OT_extrude_context={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.653437), "orient_axis_ortho":'X', "orient_type":'NORMAL', "orient_matrix":((0.316228, -0.948683, 0), (0.948683, 0.316228, 0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(True, True, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":True, "use_accurate":False, "use_automerge_and_split":False})


#bpy.ops.object.mode_set(mode = 'OBJECT')
#bpy.ops.mesh.add_pipes(seed=rand.randint(0,100), number=8, support_period=4)


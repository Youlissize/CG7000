# Command to run this script (in CMD) : py "D:\Ulysse\CG7000\testUnreal.py"

import unreal as u

e = e = u.EditorLevelLibrary()

obj = e.get_selected_level_actors()[0]
other_obj = e.get_selected_level_actors()[1]
mesh = other_obj.static_mesh_component.static_mesh

obj.static_mesh_component.set_static_mesh(mesh)

new_obj = e.spawn_actor_from_object(obj,u.Vector(100,100,100))

new_obj.static_mesh_component.set_static_mesh(mesh)
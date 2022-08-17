import unreal

editor_util = unreal.EditorUtilityLibrary()
layer_sys = unreal.LayersSubsystem()
editor_filter_lib = unreal.EditorFilterLibrary()

selected_assets = editor_util.get_selected_assets()
materials = editor_filter_lib.by_class(selected_assets, unreal.Material)

if len(materials) < 1:
    unreal.log_warning("Select material")

else:
    material = materials[0]
    material_name = material.get_fname()

    actors = layer_sys.get_selected_actors()
    static_mesh_actors = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)

    for actor in static_mesh_actors:
        actor_name = actor.get_fname()

        actor_mesh_component = actor.static_mesh_component
        actor_mesh_component.set_material(0, material)

        unreal.log("Assigning material '{}' to actor {}".format(material_name, actor_name))
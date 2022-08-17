import unreal
import os

editor_util = unreal.EditorUtilityLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
removed = 0

instant_delete = True
trash_folder = os.path.join(os.sep, "Game", "Trash")
to_be_deleted = []

for asset in selected_assets:
    asset_name = asset.get_fname()
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)

    asset_references = editor_asset_lib.find_package_referencers_for_asset(asset_path)

    if len(asset_references) == 0:
        to_be_deleted.append(asset)


for asset in to_be_deleted:
    asset_name = asset.get_fname()

    if instant_delete:
        deleted = editor_asset_lib.delete_loaded_asset(asset)

        if not deleted:
            unreal.log_warning("Asset {} could not be deleted".format(asset_name))
            continue

        removed += 1

    else:
        new_path = os.path.join(trash_folder, str(asset_name))
        moved = editor_asset_lib.rename_loaded_asset(asset, new_path)

        if not moved:
            unreal.log_warning("Asset {} could not be moved to Trash".format(asset_name))
            continue

        removed += 1

output_test = "removed" if instant_delete else "moved to Trash folder"
unreal.log("{} of {} to be deleted assets, of {} selected, removed".format(removed, len(to_be_deleted), num_assets))
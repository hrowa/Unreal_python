import unreal

editor_asset_lib = unreal.EditorAssetLibrary()

source_dir = "/Game/Test"
include_subfolders = True
deleted = 0

assets = editor_asset_lib.list_assets(source_dir, recursive=include_subfolders, include_folder=True)
folders = [asset for asset in assets if editor_asset_lib.does_directory_exist(asset)]

for folder in folders:
    has_assets = editor_asset_lib.does_directory_have_assets(folder)

    if not has_assets:
        editor_asset_lib.delete_directory(folder)
        deleted += 1
        unreal.log("Folder {} without assets was deleted".format(folder))

unreal.log("Deleted {} folders without assets".format(deleted))


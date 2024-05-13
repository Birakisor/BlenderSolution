
#Write a script in Blender to create a new material which uses textures from local storage and apply it to selected mesh objects.

import bpy
import os

texture_dir = "C:\Users\Admin\OneDrive\Desktop\solutions/texture.png"

def create_material():
    material_name = "NewMaterial"
    material = bpy.data.materials.new(name=material_name)
    return material

# Load textures from local storage
def textures_load():
    textures = {}
    for filename in os.listdir(texture_dir):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            texture_name = os.path.splitext(filename)[0]
            texture_path = os.path.join(texture_dir, filename)
            textures[texture_name] = bpy.data.images.load(texture_path)
    return textures

# Apply textures to material
def apply_textures(material, textures):
    for texture_name, texture in textures.items():
        texture_node = material.node_tree.nodes.new('ShaderNodeTexImage')
        texture_node.image = texture
        texture_node.location = (-200, 200 - 200 * len(material.node_tree.nodes))
        texture_node.name = texture_name
        
        # Create a principled shader node
        principled_node = material.node_tree.nodes.get('Principled BSDF')
        if principled_node:
            material.node_tree.links.new(texture_node.outputs[0], principled_node.inputs['Base Color'])

# Apply material to selected mesh objects
def apply_material_to_selected_objects(material):
    selected_objects = bpy.context.selected_objects
    for obj in selected_objects:
        if obj.type == 'MESH':
            if obj.data.materials:
                obj.data.materials[0] = material
            else:
                obj.data.materials.append(material)

# Main function
def main():
    material = create_material()
    
    textures = textures_load()
    
    apply_textures(material, textures)
    apply_material_to_selected_objects(material)

# Run the main function
if __name__ == "__main__":
    main()
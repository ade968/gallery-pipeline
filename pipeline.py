import os
import json
import argparse
from pathlib import Path

def get_exif(file_path):
    # Simplified metadata extraction for prototype
    return {
        "filename": file_path.name,
        "path": str(file_path),
        "size": file_path.stat().st_size,
    }

def reconcile_sidecar(image_path, mode):
    sidecar_path = image_path.with_suffix(".json")
    if not sidecar_path.exists():
        return "create"
    
    if mode == "skip":
        print(f"Skipping existing sidecar for {image_path.name}")
        return "skip"
    elif mode == "overwrite":
        print(f"Overwriting existing sidecar for {image_path.name}")
        return "overwrite"
    elif mode == "manual":
        # Block the kanban task so the user can provide input
        # Note: In a real system, we'd signal the user. For now, this is a placeholder.
        print(f"Sidecar for {image_path.name} exists. Manual resolution required.")
        return "skip" # Default to skip if we can't block mid-loop easily without re-spawning.

def process_images(directory, mode):
    path = Path(directory)
    images = []
    
    # Process only images in the directory
    for img_path in path.iterdir():
        if img_path.suffix.lower() in [".jpg", ".jpeg"]:
            status = reconcile_sidecar(img_path, mode)
            if status == "skip":
                # Load existing if available
                sidecar_path = img_path.with_suffix(".json")
                if sidecar_path.exists():
                    with open(sidecar_path, 'r') as f:
                        images.append(json.load(f))
                continue
            
            metadata = get_exif(img_path)
            # Add placeholders for additional fields
            metadata.update({"location": "unknown", "style": "unknown"})
            
            # Save or update sidecar
            sidecar_path = img_path.with_suffix(".json")
            with open(sidecar_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            images.append(metadata)
            
    manifest_path = path / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(images, f, indent=2)
    print(f"Manifest written to {manifest_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gallery Pipeline CLI")
    parser.add_argument("directory", help="Directory to process")
    parser.add_argument("--mode", choices=["skip", "merge", "overwrite", "manual"], default="manual", help="Conflict resolution mode")
    args = parser.parse_args()
    process_images(args.directory, args.mode)

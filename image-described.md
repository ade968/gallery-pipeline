# Image Described

## Purpose
Describe images in detailed markdown files with YAML frontmatter for archival, search, and data-driven analysis.

## Workflow
1. User provides an image file path.
2. Read the image visually using the vision tool.
3. Extract technical metadata via `mdls` and `sips` (macOS).
4. Write a `.md` file in the **same folder** as the image, with the **same filename** but `.md` extension.

## Markdown Format

### YAML Frontmatter
Always start with a YAML block containing core metadata for the build manifest.
```yaml
---
filename: "DSCF1234.JPG"
model_used: "gemini-1.5-pro"
analysis_date: "2026-05-24"
tags: ["winter", "frost", "garden", "fujifilm", "dawn"]
technical:
  camera: "Fujifilm X-T3"
  lens: "16mm f/2.8"
  iso: 400
  dimensions: "6240x4160"
---
```

### Title
Use the original image filename as the H1 heading (e.g. `# IMG_2045.jpg`)

### Sections (omit any that don't apply)
1.  **Overview** — Quick summary
2.  **Technical Metadata** — Dimensions, file type, size, colour space, EXIF
3.  **Composition & Framing** — Layout, perspective, focal point
4.  **Lighting & Atmosphere** — Light source, quality, time of day, weather, clouds
5.  **Colour Palette** — Dominant/accent colours, contrast, temperature
6.  **People & Figures** — Clothing, facial expressions, body language, accessories
7.  **Objects & Furniture** — Items, materials, placement
8.  **Architecture & Buildings** — Style, materials, signage
9.  **Flora & Fauna** — Plants, animals, species
10. **Landscape & Environment** — Terrain, water, sky, urban/rural
11. **Text & Signage** — Any visible text transcribed verbatim
12. **Mood & Emotion** — Overall feeling and narrative impression

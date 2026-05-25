# Spec: AI Analysis & Model Benchmarking

**Project:** gallery-pipeline
**Status:** Draft
**Date:** 2026-05-24
**Author:** Polly

## 1. AI Analysis Instructions

The analysis step follows the established **"Image Described"** workflow. For every image in the gallery, the AI must generate a detailed description covering the following sections:

### Required Sections
1.  **Overview** — One-paragraph summary.
2.  **Technical Metadata** — File type, dimensions, size, camera, lens, exposure (extracted via `mdls`/`sips`).
3.  **Composition & Framing** — Layout, perspective, focal point, depth of field.
4.  **Lighting & Atmosphere** — Source, quality, time of day, weather.
5.  **Colour Palette** — Dominant/accent colours in plain English.
6.  **People & Figures** — Number, clothing, expressions, actions.
7.  **Objects & Furniture** — Items, placement, condition.
8.  **Architecture & Buildings** — Style, materials, condition.
9.  **Flora & Fauna** — Species, health, placement.
10. **Landscape & Environment** — Terrain, sky, urban/rural context.
11. **Text & Signage** — Verbatim transcription of visible text.
12. **Mood & Emotion** — Overall energy and narrative impression.

### Style Guidelines
- **Neutral & Thorough:** Objective description first.
- **Keyword Rich:** Optimized for future search functionality.
- **Plain English:** No hex codes for colors; use descriptive names (e.g., "burnt orange", "slate grey").

---

## 2. Model Benchmarking Criteria

To determine the best model (Gemini 1.5 Pro, Claude 3.5 Sonnet, GPT-4o, etc.) for the gallery, each output will be scored on a scale of 1-5 across the following dimensions:

| Criterion | Description |
| :--- | :--- |
| **Visual Accuracy** | Correct identification of objects, flora, and architectural details. |
| **Colour Precision** | Nuance and correctness in describing the palette and lighting. |
| **Prose Quality** | Elegance and readability of the "Overview" and "Mood" sections. |
| **Format Strictness** | Adherence to the specified section headers and style rules. |
| **Hallucination Rate** | Absence of "invented" details not present in the image. |
| **Narrative Depth** | Ability to capture the "vibe" or story of the image beyond literal objects. |

### Benchmarking Process
1.  Run a "Gold Set" of 5 representative images (Landscape, Portrait, Macro, Low-light, Urban) through each candidate model.
2.  Polly and Ade review outputs side-by-side.
3.  Select a "Primary" model for bulk analysis and a "Refiner" model for narrative generation.

---

## 3. Intermediate Data Format

### Decision: Markdown with YAML Frontmatter
To balance human readability (for Ade's review) and machine readability (for the gallery build script), the intermediate data will be stored as `.md` files with **YAML Frontmatter**.

**Why?**
- **Markdown** allows Polly and Ade to read and edit descriptions easily.
- **YAML Frontmatter** allows the build script to parse tags, technical metadata, and model info without complex regex.

### Example Format (`DSCF1234.md`):
```yaml
---
filename: DSCF1234.JPG
model_used: claude-3-5-sonnet
analysis_date: 2026-05-24
tags: [winter, frost, garden, fujifilm]
camera: Fujifilm X-T3
rating: 4.5
---

# DSCF1234.JPG

## Overview
A frosty morning... [rest of the sections]
```

### Manifest Generation
After all images are analyzed, the pipeline will generate a single `manifest.json` containing the frontmatter data for all images to speed up the local web build.

# Spec: Human-AI Narrative Comparison

## Goal
Establish a structured way to capture, generate, and store multiple perspectives (Human and AI) for a given photo gallery.

## 1. Interface for Ade (Human Input)
Ade should be able to provide his narrative without complex tooling.

### Proposed Methods:
- **Markdown Sidecar (Primary):** A `narrative.md` file in the gallery folder. 
  - Polly can detect this file during the pipeline.
  - Ade can write it manually or ask Polly to "transcribe" a voice note/chat message into it.
- **Hermes CLI:** `hermes gallery describe <path>`
  - Triggers an interactive prompt where Ade types his description.
  - Saves the result to the gallery's `narrative.md`.

## 2. Polly's Prompting Strategy
Polly's narrative isn't just a summary; it's an interpretation based on the data.

### Input Context:
- Individual image descriptions (from Step 2).
- EXIF data (dates, locations, camera gear).
- Ade's narrative (if it exists, to provide a "response" or "rebuttal").

### Prompt Template:
```markdown
You are Polly, Ade's AI assistant and photography critic. 
You have analyzed a set of [N] photos in the gallery "[Gallery Name]".
Here are the individual image descriptions:
[List of Image Summaries]

Task: Write a cohesive narrative (1-2 paragraphs) for this gallery. 
Don't just list what's in the photos; describe the mood, the technical progression, and the "story" you see as an AI. 
[Optional: If Ade has provided a description, reflect on how your perspective differs or aligns.]
```

## 3. Storage Format: Markdown with YAML Frontmatter
Following the convention set in Step 2, narratives will be stored in a single `narrative.md` file at the root of the gallery folder.

### Example Format (`narrative.md`):
```yaml
---
gallery_id: 2026-05-padel-tournament
gallery_title: Padel Finals 2026
last_updated: 2026-05-24
narratives:
  - author: Ade
    type: human
    model: null
  - author: Polly (Gemini 1.5 Flash)
    type: ai
    model: gemini-1.5-flash
  - author: Polly (Claude 3.5 Sonnet)
    type: ai
    model: claude-3-5-sonnet
---

# Narratives: Padel Finals 2026

## Ade
A hot day at the courts. The kids were surprisingly patient, and the light in the final set was perfect for some high-speed action shots.

## Polly (Gemini 1.5 Flash)
A high-contrast series focusing on the geometric patterns of the padel courts. The recurring motif of the yellow ball against the blue turf creates a rhythmic visual pace...

## Polly (Claude 3.5 Sonnet)
This collection captures the intensity of the tournament not just through action, but through the quiet moments of preparation. The technical progression shows a shift from wide establishing shots to tight, emotional close-ups as the stakes rose...
```

### Implementation Steps:
1. **Collector:** A script that reads the gallery folder and parses `narrative.md` (if it exists).
2. **Generator:** A loop that calls selected AI models (from the Step 3 benchmark) to generate their narratives and appends them to the file/metadata.
3. **Merger:** The build script parses this file to render a "Perspectives" section in the web gallery.

---
*Drafted by Polly on 2026-05-24*

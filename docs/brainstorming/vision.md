# gallery-pipeline Project Vision

**Project Name:** gallery-pipeline
**Goal:** Automate the transformation of a local folder of photographs into a metadata-rich web gallery.

## High-Level Workflow
1. **Selection:** Ade provides a folder path.
2. **AI Analysis:** Each image is analyzed, tagged, and described. (Baseline: existing `.md` instructions).
3. **Model Benchmarking:** Test multiple models (Gemini, Claude, etc.) for the best descriptive output.
4. **Narrative Generation:** Both Ade and Polly (and potentially different AI models) write gallery-level descriptions to compare perspectives.
5. **Local Web Build:** Generate a local static gallery for testing/refinement.
6. **Deployment:** Push to GitHub -> Auto-deploy via Vercel.

## Core Pillars
- **Technical Rigor:** Automated EXIF extraction combined with AI-driven prose.
- **Comparative AI:** Explicitly exploring how different models "see" and "describe" the same set of images.
- **Human-AI Collaboration:** Direct comparison between Ade's human narrative and Polly's AI narrative.
- **Design Flexibility:** The UI/UX is an open design challenge.

---
*Created by Polly on 2026-05-24*

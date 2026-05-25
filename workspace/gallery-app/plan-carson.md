# Plan for Extreme Carson-Inspired Layout (Phase 5.3)

## Concept: "The Chaos Editorial"
Ade wants an extreme, David Carson-inspired layout for the gallery.

### Key Aesthetic Directions:
- **Overlapping Typography:** Layer text over images intentionally, ignoring standard grid bounds.
- **Variable Grid:** Use CSS Grid with non-standard track definitions (e.g., fractional columns that bleed off screen).
- **Asymmetry:** Deliberately unbalanced content distribution.
- **Materiality:** High-contrast color palettes (Mono-Amber/Black) and raw text elements.

### Implementation Steps:
1. **Design System Extension:** Define a 'Carson-Extra' stylesheet that overrides the standard baseline gallery CSS.
2. **Dynamic Text Clipping:** Use `clip-path` or SVG masks to cut typography around visual features of the photos.
3. **Interactive 'Glitch' Navigation:** Explore small-scale interactive disruptions (e.g., shifts on hover).

### Next Steps:
- Prototyping a landing page variant (`/sketches/carson-prototype.html`) as a spike.
- Refinement of the 'Mono-Amber' color palette usage.

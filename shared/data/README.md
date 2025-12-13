# Shared Data

Structured data files used across all websites.

## Files

### `profile.json`

Complete professional profile including:
- Personal info & contact
- IDs (ORCID, Scopus, LinkedIn, GitHub)
- Education (Microsoft Research PhD Fellowship, Technion)
- Industry experience (Rhea Labs, Canotera, AKA Foods, Embryonics, Apple, Intel)
- Research positions (Technion labs)
- Publications (12+ papers: Nature, PNAS, IEEE TPAMI, etc.)
- Patents (14+ patents: Apple, Intel, Embryonics, AKA Foods)
- Projects (Unpopular Science, Embino, Kernel Keys)
- Expertise domains
- Academic references

### `unpopular_science.json`

Complete book metadata for unpop.info:
- Book info (title, chapters, status)
- Writing philosophy (anti-sensationalism, rigorous accessibility)
- Chapter structure (8 pages: title, historical, main, technical, sidenote)
- All 50 chapters organized by topic (math, physics, CS, chemistry, etc.)
- Highlight chapters with hooks
- Prologue excerpt and origin story

## Usage

```typescript
import profile from '../../shared/data/profile.json';
import book from '../../shared/data/unpopular_science.json';

// Profile
profile.personal.name.full          // "David H. Silver"
profile.publications.length         // 12
profile.patents.filter(p => p.assignee === "Apple")
profile.projects.unpopularScience   // book project info

// Book
book.chapters                       // 50
book.topics.physics.length          // 21 physics chapters
book.highlights[0].hook             // chapter teaser
book.philosophy.rules               // writing rules
```

## Source Files

- Raw/unstructured source files: `../some_info/`
- Book LaTeX source: `/Users/davidsilver/dev/private/unpopular-science-source/`


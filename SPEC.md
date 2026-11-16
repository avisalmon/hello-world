# Improvise — Product Specification

## Goal
A browser-based interactive accompaniment ensemble for piano improvisation, hosted on GitHub Pages. No piano melody in backing tracks.

## Version 1
- Three presets: Soft Evening Jazz (Cmaj9 | Am9 | Dm9 | G13 | Em9 | A7b9 | Dm9–G13 | Cmaj9), twelve-bar blues, and A-minor circle progression (Am7 x4 | Dm7 | G7 | Cmaj7 | Fmaj7 | Bm7b5 | E7 | Am7).
- Choose and edit a chord progression; custom chord selections.
- Style selector: cocktail jazz, blues, bossa nova (architecture expandable to salsa and samba).
- Instrument enable/disable toggles: bass, guitar, drums; independent instrument volume and master volume.
- Tempo adjustment, transport controls, looping, synchronized chord highlighting.
- Static site, mobile and desktop friendly, no server requirement.
- Prioritize realistic musical accompaniment, humanized rhythm, sampled acoustic sounds in subsequent sound-quality iteration.

## Future
- Web MIDI input from digital piano and MIDI output to supported instruments (permission and browser support required).
- Distinguish MIDI note messages from audio routing: MIDI does not transmit recorded audio.
- Recording and exporting performances.
- More instrument libraries, styles, and harmonic generation options.

## Implementation notes
Keep independent tracks per instrument. Avoid requiring a server. Document any sample licenses before distribution. Do not claim realistic acoustic samples until actually integrated. GitHub Pages deployment requires repository Pages configuration or a suitable workflow.

## Audio generation strategy — approved direction (2026-11-16)
- Prioritize AI-generated, natural-sounding backing tracks over the current synthesized placeholder.
- User accepts a generation wait (illustrative 20–60 seconds, **not a measured promise**).
- Pre-generate and cache a library of common progressions, styles, and tempos so most playback can start immediately.
- Keep independently mixable, synchronized bass, guitar, and drum stems. Evaluate separately generated stems versus full mix with source separation; verify musical alignment and artifact levels.
- Store audio files and metadata (progression, key, BPM, style, bar boundaries, licensing/provenance, duration) in the repository or a static asset host; GitHub Pages itself cannot run AI generation jobs.
- Custom progressions require an external generation service or offline generation/publishing pipeline; never claim arbitrary new music can be generated solely by the static page.
- Playback: instant for cached assets; show progress for uncached generation. Changing tempo within a safe range may use time stretching, with quality trade-offs.
- Before integrating a generator, verify API availability, cost, rights to distribute outputs, and feasibility of stem generation. Do not assume Suno has a usable API or provides stems.
- Current synthesized playback remains a fallback until tested AI audio assets are available.

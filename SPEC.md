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

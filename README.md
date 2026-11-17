# Improvise — Jazz Piano Play-Along

A jazz accompaniment project for a **human pianist**: no piano accompaniment.

## Current release

- [Open the GitHub Pages site](https://avisalmon.github.io/hello-world/)
- [Original Soft Evening sampled demo](https://avisalmon.github.io/hello-world/original.html) — preserved unchanged and selected as the default by `index.html`.
- [Previous experimental interface](https://avisalmon.github.io/hello-world/legacy_procedural_demo.html) — retained for reference, **not** the default.

**Musical quality comes first.** The original sampled recording is not to be replaced by simplistic synthesized accompaniment. The current original is a mixed recording; independently adjustable bass, guitar and drums will require suitable individual recordings/stems or a properly validated separation process. Do not describe synthetic controls as controlling the original mix.

## Verification

Run `python3 -m unittest discover -s tests -v` to check that the preserved HTML, embedded-audio markers, default launcher and archived experimental interface remain in place. A GitHub Actions workflow also runs these checks on pushes and pull requests.

These are **static regression checks**, not proof of musical quality, seamless looping, successful deployment, or playback on mobile/desktop. Those require actual listening and browser/device testing.

## Next work

Obtain or produce rights-cleared synchronized acoustic stems (upright bass, jazz guitar, brushed drums), implement an independent mixer, then validate synchronization, looping, chord display, and actual GitHub Pages playback before declaring completion.

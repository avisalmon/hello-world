"""Non-audio regression checks for the Improvise GitHub Pages release.

Run: python3 -m unittest discover -s tests -v
These checks cannot prove subjective audio quality or browser playback.
"""
from pathlib import Path
import hashlib
import unittest

ROOT = Path(__file__).resolve().parents[1]
# Git blob SHA of the user-approved original, verified against the recovered demo.
ORIGINAL_GIT_BLOB_SHA = "2344609b84b09c4069bb2b08be19ce56490b0db8"


class ImproviseReleaseChecks(unittest.TestCase):
    def test_original_recording_is_preserved(self):
        original = ROOT / "original.html"
        self.assertTrue(original.is_file(), "Original demo must remain available")
        data = original.read_bytes()
        self.assertGreater(len(data), 1_000_000, "Original embedded audio appears missing")
        # A size/marker check alone would accept a silently degraded recording.
        # Pin the *entire* original file, including its embedded audio, byte-for-byte.
        blob = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
        self.assertEqual(hashlib.sha1(blob).hexdigest(), ORIGINAL_GIT_BLOB_SHA,
                         "Original recording/demo changed: restore the approved original")
        self.assertIn(b"<html", data.lower(), "Original demo is not HTML")
        self.assertTrue(
            b"audio/mpeg" in data.lower() or b"audio/mp3" in data.lower()
            or b"data:audio" in data.lower(),
            "Expected embedded recorded audio marker is missing",
        )

    def test_original_remains_default(self):
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertRegex(index, r"(?i)(refresh|location\\.replace)")
        self.assertIn("./original.html", index)
        self.assertNotIn("legacy_procedural_demo.html", index,
                         "Do not silently make procedural demo the default")

    def test_experimental_demo_preserved_separately(self):
        legacy = ROOT / "legacy_procedural_demo.html"
        self.assertTrue(legacy.is_file(), "Legacy interface must be retained")
        text = legacy.read_text(encoding="utf-8")
        self.assertIn("Band mixer", text)
        self.assertIn("chords", text)

    def test_no_unexpected_piano_accompaniment_on_default(self):
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("new AudioContext", index,
                         "Default launcher should not synthesize accompaniment")


if __name__ == "__main__":
    unittest.main()

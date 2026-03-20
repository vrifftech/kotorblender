"""
test_gl_placeholder.py – PyKotor GL tests out of scope

PyKotor has OpenGL/viewport tests in Libraries/PyKotor/tests/gl/:
- test_frustum_culling.py (Camera, Frustum, culling)
- test_camera_controller.py (CameraController, InputState)

These require pykotor.gl and a display/GL context. KotorBlender has no equivalent
viewport stack; they are not ported. This file documents that and provides a
single skipped test so the test runner still sees the module.

Run with:
    blender --background --python test/blender/test_gl_placeholder.py
"""

from __future__ import annotations

import sys


def test_gl_tests_out_of_scope():
    """PyKotor camera/frustum/OpenGL tests require pykotor.gl; not ported to KotorBlender."""
    print("  SKIP test_gl_tests_out_of_scope (PyKotor GL tests require pykotor.gl; out of scope)")
    return True


def run_tests():
    print("\n=== test_gl_placeholder.py ===")
    results = [test_gl_tests_out_of_scope()]
    passed = sum(results)
    total = len(results)
    print(f"\n[OK] {passed}/{total} passed (skipped)\n")
    return True


if __name__ == "__main__":
    sys.exit(0 if run_tests() else 1)

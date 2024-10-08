# Copyright (c) Hello Robot, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the LICENSE file in the root directory
# of this source tree.
#
# Some code may be adapted from other open-source works with their respective licenses. Original
# license information maybe found below, if so.

# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np

from stretch.motion.utils.geometry import PI2, angle_difference, interpolate_angles


def _eval_angle_difference(a, b, expected, expected_step):
    print(f"{a=}, {b=}, {angle_difference(a, b)=}, {expected=}")
    result = angle_difference(a, b)
    assert np.allclose(result, expected)
    assert result >= 0
    assert result <= PI2

    step_size = 0.1
    expected_interp = (a + (expected_step * step_size)) % PI2
    interp = interpolate_angles(a, b, step_size=step_size)
    print(f"interpolating: {interp=}, {expected_interp=}")
    assert np.allclose(interp, expected_interp)
    assert interp >= 0
    assert interp <= PI2


def test1():
    print("--- 1 ---")
    _eval_angle_difference(1, 2, expected=1, expected_step=1)


def test2():
    print("--- 2 ---")
    _eval_angle_difference(0, np.pi, expected=np.pi, expected_step=1)


def test3():
    print("--- 3 ---")
    _eval_angle_difference(0, PI2, 0, expected_step=0)


def test4():
    print("--- 4 ---")
    _eval_angle_difference(np.pi, 2 * np.pi - 0.1, expected=(np.pi - 0.1), expected_step=1)


def test5():
    print("--- 5 ---")
    _eval_angle_difference(-2 * np.pi, np.pi + 0.1, expected=np.pi - 0.1, expected_step=-1)


def test6():
    print("--- 6 ---")
    _eval_angle_difference(-np.pi / 2 + 0.1, np.pi, expected=np.pi / 2 + 0.1, expected_step=-1)


def test7():
    print("--- 7 ---")
    _eval_angle_difference(-np.pi / 2, 0, expected=np.pi / 2, expected_step=1)


def test8():
    print("--- 8 ---")
    _eval_angle_difference(0.1, PI2 - 0.1, expected=0.2, expected_step=-1)


if __name__ == "__main__":
    # Angle magnitude evals
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    print("---------------------")

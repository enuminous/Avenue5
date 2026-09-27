from avenue5 import Step, dignity, next_disaster, remediation_is_unstable, simulate


def approx(a, b, eps=1e-9):
    assert abs(a - b) < eps, (a, b)


def run_tests():
    s0 = Step(3.0, 0.4, 0.5, 0.3, 0.2, 1.0)
    d1 = next_disaster(2.0, s0)
    approx(d1, 8.6)
    assert remediation_is_unstable(2.0, d1)

    s1 = Step(1.0, 0.8, 0.7, 0.2, 0.4, 0.5)
    states = simulate(2.0, [s0, s1])
    approx(states[2], 20.74)

    assert 0 < dignity(8.6) < 1

    try:
        Step(1, 1.2, 0, 0, 0, 0).validate()
        raise AssertionError("invalid competence should fail")
    except ValueError:
        pass

    print("all tests passed")


if __name__ == "__main__":
    run_tests()

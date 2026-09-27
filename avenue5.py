"""Avenue 5 Catastrophe Equation reference implementation.

Zero-dependency, satirical narrative model.
"""

from dataclasses import dataclass
from math import exp
from typing import Iterable, List


@dataclass(frozen=True)
class Step:
    engineering_failure: float
    competence: float
    panic: float
    vanity: float
    bureaucracy: float
    human_complication: float

    def validate(self) -> None:
        values = {
            "engineering_failure": self.engineering_failure,
            "panic": self.panic,
            "vanity": self.vanity,
            "bureaucracy": self.bureaucracy,
            "human_complication": self.human_complication,
        }
        for name, value in values.items():
            if value < 0:
                raise ValueError(f"{name} must be nonnegative")
        if not 0 <= self.competence <= 1:
            raise ValueError("competence must lie in [0, 1]")


def next_disaster(current: float, step: Step) -> float:
    """Compute D_(t+1)."""
    if current < 0:
        raise ValueError("current disaster level must be nonnegative")
    step.validate()
    amplification = 1 + step.panic + step.vanity + step.bureaucracy
    surviving_fault = step.engineering_failure * (1 - step.competence)
    return (current + surviving_fault) * amplification + step.human_complication


def dignity(disaster: float, initial: float = 1.0, decay: float = 0.15) -> float:
    """G(t) = G0 exp(-lambda D)."""
    if min(disaster, initial, decay) < 0:
        raise ValueError("arguments must be nonnegative")
    return initial * exp(-decay * disaster)


def simulate(initial_disaster: float, steps: Iterable[Step]) -> List[float]:
    states = [initial_disaster]
    current = initial_disaster
    for step in steps:
        current = next_disaster(current, step)
        states.append(current)
    return states


def remediation_is_unstable(before: float, after: float) -> bool:
    return after > before


def canonical_demo() -> None:
    steps = [
        Step(3.0, 0.40, 0.50, 0.30, 0.20, 1.00),
        Step(1.0, 0.80, 0.70, 0.20, 0.40, 0.50),
        Step(0.4, 0.90, 0.35, 0.15, 0.25, 0.20),
    ]
    states = simulate(2.0, steps)
    print("Avenue 5 catastrophe simulation")
    print("--------------------------------")
    for i, state in enumerate(states):
        print(f"D_{i} = {state:.3f} | dignity = {dignity(state):.4f}")
    print()
    print("One Terrible Decision -> Three New Problems")
    problems = 1
    for n in range(5):
        print(f"generation {n}: {problems} problem(s)")
        problems *= 3


if __name__ == "__main__":
    canonical_demo()

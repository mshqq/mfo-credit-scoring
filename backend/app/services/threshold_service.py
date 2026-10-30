from typing import Literal

from app.config import settings

type Decision = Literal["approve", "reject", "manual_review"]


class ThresholdService:
    def __init__(self):
        self.reject_threshold: float = settings.reject_threshold
        self.approve_threshold: float = settings.approve_threshold

        if not (0 <= self.reject_threshold < self.approve_threshold <= 1):
            raise ValueError("Значения порогов не корректные")

    def get_decision_by_probability(self, probability: float) -> Decision:
        if not (0 <= probability <= 1):
            raise ValueError("Некорректное значение вероятности")

        if probability >= self.approve_threshold:
            return "approve"
        elif probability <= self.reject_threshold:
            return "reject"
        else:
            return "manual_review"

from typing import Dict
import re

from presidio_anonymizer.operators import Operator, OperatorType
from presidio_anonymizer.entities import OperatorResult


class Initial(Operator):
    """Initial operator which converts words to initials."""

    def operate(self, text: str, **kwargs) -> OperatorResult:
        words = re.split(r"\s+", text.strip())

        initials = []
        for word in words:
            if not word:
                continue
            for char in word:
                if char.isalnum():
                    initials.append(f"{char.upper()}.")
                    break

        result_text = " ".join(initials)

        return OperatorResult(
            0,
            len(text),
            "DEFAULT",
            result_text,
            self.operator_name(),
        )

    def validate(self, params: Dict = None):
        return

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

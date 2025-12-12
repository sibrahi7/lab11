from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType
from presidio_anonymizer.entities import OperatorResult


class Initial(Operator):
    """Minimal Initial operator (stub implementation)."""

    def operate(self, text: str, **kwargs) -> OperatorResult:
        # Minimal behavior: return the text unchanged
        return OperatorResult(
            start=0,
            end=len(text),
            entity_type="",
            text=text,
            operator_name=self.operator_name(),
        )

    def validate(self, params: Dict = None):
        # Minimal validation: accept anything
        return

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

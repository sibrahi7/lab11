from presidio_anonymizer.operators.initial import Initial


def test_initial_operator_transforms_name_to_initials():
    operator = Initial()
    result = operator.operate("John Smith")

    assert result.text == "J. S."

from pytest import raises
from bugsnag import Severity


def test_severity_str():
    assert str(Severity.INFO) == 'info'
    assert str(Severity.WARNING) == 'warning'
    assert str(Severity.ERROR) == 'error'


def test_construct_severity():
    assert Severity.INFO == Severity('info')
    assert Severity.WARNING == Severity('warning')
    assert Severity.ERROR == Severity('error')


def test_invalid_severity():
    with raises(ValueError):
        Severity('inf')

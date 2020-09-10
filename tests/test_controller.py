import pytest

from DronePy.Controller import Controller
from DronePy.Devices import limeSDR
from DronePy.Models import DX2

@pytest.fixture()
def device():
    return limeSDR.LimeSDR()

@pytest.fixture()
def model():
    return DX2.DX2()


@pytest.fixture()
def controller():
    return Controller()


def test_controller(controller):
    pass

import pytest

from DronePy.Controller import Controller
from DronePy.Devices.limeSDR import LimeSDR
from DronePy.Models.DX2 import DX2

@pytest.fixture()
def device():
    return LimeSDR()

@pytest.fixture()
def model():
    return DX2()


@pytest.fixture()
def controller():
    return Controller()


def test_controller(controller):
    pass

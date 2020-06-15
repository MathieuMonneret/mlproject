import os
import mlproject
import pytest
from  mlproject.tools import haversine

def test_haversine():
    assert haversine(2.380009, 48.865070, 4.849936, 45.747985) == 393.4132747701974

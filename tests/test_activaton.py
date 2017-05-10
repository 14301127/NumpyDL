# -*- coding: utf-8 -*-

import pytest
import numpy as np


def test_activation():
    from npdl.activation import Activation

    act = Activation()

    with pytest.raises(NotImplementedError):
        act.forward((10, 10))

    with pytest.raises(NotImplementedError):
        act.derivative()


class TestActivations(object):

    @pytest.mark.parametrize('activation',
                             ['sigmoid',
                              'tanh',
                              'relu',
                              'linear',
                              'softmax',
                              'Elliot',
                              'SymmetricElliot',
                              'SoftPlus',
                              'SoftSign'])
    def test_activation(self, activation):

        input = np.arange(24).reshape((4, 6))

        if activation == 'sigmoid':
            from npdl.activation import Sigmoid

            npdl_act = Sigmoid()
            f_res = npdl_act.forward(input)

            assert 0. <= np.all(f_res) <= 1.

        elif activation == 'tanh':
            from npdl.activation import Tanh

            npdl_act = Tanh()
            f_res = npdl_act.forward(input)

            assert -1. <= np.all(f_res) <= 1.0

        elif activation == 'relu':
            from npdl.activation import ReLU

            npdl_act = ReLU()
            f_res = npdl_act.forward(input)

            assert np.all(f_res) >= 0.

        elif activation == 'linear':
            from npdl.activation import Linear

            npdl_act = Linear()
            f_res = npdl_act.forward(input)

            assert f_res == input

        elif activation == 'softmax':
            from npdl.activation import Softmax

            npdl_act = Softmax()
            f_res = npdl_act.forward(input)

            assert 0. <= np.all(f_res) <= 1.0

        elif activation == 'elliot':

            pass



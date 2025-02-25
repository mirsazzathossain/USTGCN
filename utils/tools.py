# _*_ coding: utf-8 -*-
"""
This module defines some useful functions.

Functions:
    - :py:function:`rmse` calculates root mean squared error.
    - :py:function:`mape` calculates mean absolute percentage error.
    - :py:function:`mae` calculates mean absolute error.
"""

__author__ = "Mir Sazzat Hossain"

import numpy as np
from numpy import ndarray


def rmse(y_true: list, y_pred: list) -> float:
    """
    Calculate root mean squared error.

    :param y_true: true values of shape (batch_size, out_size)
    :type y_true: list
    :param y_pred: predicted values of shape (batch_size, out_size)
    :type y_pred: list

    :return: RMSE loss
    :rtype: float
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    return np.sqrt(np.mean(np.square(y_true - y_pred)))


def mape(y_true: list, y_pred: list) -> float:
    """
    Calculate mean absolute percentage error.

    :param y_true: true values of shape (batch_size, out_size)
    :type y_true: list
    :param y_pred: predicted values of shape (batch_size, out_size)
    :type y_pred: list

    :return: MAPE
    :rtype: float
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    epsilon = 1e-7

    return np.mean(np.abs((y_true - y_pred) / (y_true + epsilon))) * 100


def mae(y_true: list, y_pred: list) -> ndarray:
    """
    Calculate mean absolute error.

    :param y_true: true values of shape (batch_size, out_size)
    :type y_true: list
    :param y_pred: predicted values of shape (batch_size, out_size)
    :type y_pred: list

    :return: MAE
    :rtype: ndarray
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    return np.mean(np.abs(y_true - y_pred))


def calculate_foodwise_errors(
        y_true: list, y_pred: list, num_foods: int) -> list:
    """
    Calculate RMSE, MSE for each food item.

    :param y_true: true values of shape (num_food*num_batches, out_size)
    :type y_true: list
    :param y_pred: predicted values of shape (num_food*num_batches, out_size)
    :type y_pred: list

    :return: RMSE, MSE for each food item
    """
    rmse_list = []
    mse_list = []

    for i in range(num_foods):
        rmse_list.append(rmse(y_true[i::num_foods], y_pred[i::num_foods]))
        mse_list.append(mae(y_true[i::num_foods], y_pred[i::num_foods]))

    return rmse_list, mse_list

# @Author : bamtercelboo
# @Datetime : 2018/8/24 15:27
# @File : test.py
# @Last Modify Time : 2018/8/24 15:27
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  test.py
    FUNCTION : None
"""
import os
import sys
import torch


def load_test_model(model, config):
    """
    :param model:  initial model
    :param config:  config
    :return:  loaded model
    """
    if config.t_model is None:
        test_model_dir = config.save_best_model_dir
        test_model_name = "{}.pt".format(config.model_name)
        test_model_path = os.path.join(test_model_dir, test_model_name)
        print("load default model from {}".format(test_model_path))
    else:
        test_model_path = config.t_model
        print("load user model from {}".format(test_model_path))
    model.load_state_dict(torch.load(test_model_path))
    return model


def load_test_data(train_iter=None, dev_iter=None, test_iter=None, config=None):
    """
    :param train_iter:  train data
    :param dev_iter:  dev data
    :param test_iter:  test data
    :param config:  config
    :return:  data for test
    """
    data, path_source, path_result = None, None, None
    if config.t_data is None:
        print("default[test] for model test.")
        data = test_iter
        path_source = config.test_file
        path_result = "{}.out".format(config.test_file)
    elif config.t_data == "train":
        print("train data for model test.")
        data = train_iter
        path_source = config.train_file
        path_result = "{}.out".format(config.train_file)
    elif config.t_data == "dev":
        print("dev data for model test.")
        data = dev_iter
        path_source = config.dev_file
        path_result = "{}.out".format(config.dev_file)
    elif config.t_data == "test":
        print("test data for model test.")
        data = test_iter
        path_source = config.test_file
        path_result = "{}.out".format(config.test_file)
    else:
        print("Error value --- t_data = {}, must in [None, 'train', 'dev', 'test'].".format(config.t_data))
        exit()
    return data, path_source, path_result


class T_Inference(object):
    """
        Test Inference
    """
    def __init__(self):
        print("test T_Inference")





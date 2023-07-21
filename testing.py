import pytest
from data import Data


def get_dict():
    data = {
        "id": "1",
        "name": "first",
        "metadata": {
            "system": {
                "size": 10.7
            },
            "user": {
                "batch": 10
            }
        }
    }
    return data


def get_attr_val(instance, keys):
    if len(keys) > 1:
        return get_attr_val(getattr(instance, keys[0]), keys[1:])
    return getattr(instance, keys[0])


def get_data_instances_with_different_initializations():
    return [Data.from_dict(get_dict()), Data(**get_dict())]


@pytest.mark.parametrize("data_class_instances, keys, expected_val",
                         [
                             (
                                     get_data_instances_with_different_initializations(),
                                     ["id"],
                                     "1",
                             ),
                             (
                                     get_data_instances_with_different_initializations(),
                                     ["metadata", "system", "size"],
                                     10.7
                             )
                         ]
                         )
def test__get_attributes(data_class_instances, keys, expected_val):
    for data_class_instance in data_class_instances:
        assert get_attr_val(data_class_instance, keys) == expected_val


@pytest.mark.parametrize("data_class_instances, attr_path",
                         [
                             (
                                     get_data_instances_with_different_initializations(),
                                     ['height'],
                             ),
                             (
                                     get_data_instances_with_different_initializations(),
                                     ['metadata', 'system', 'height']
                             )
                         ]
                         )
def test__get_default_attr(data_class_instances, attr_path):
    for data_class_instance in data_class_instances:
        assert get_attr_val(data_class_instance, attr_path) == Data.DEFAULT_VALUE


@pytest.mark.parametrize("data_class_instances",
                         [
                             (
                                     get_data_instances_with_different_initializations()
                             )
                         ]
                         )
def test__to_dict(data_class_instances):
    for data_class_instance in data_class_instances:
        assert data_class_instance.to_dict() == get_dict()

import pytest
from data import Data


def get_data():
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


@pytest.mark.parametrize("data_dict, keys, expected_val",
                         [
                             (
                                     get_data(),
                                     ["id"],
                                     "1",
                             ),
                             (
                                 get_data(),
                                 ["metadata", "system", "size"],
                                 10.7
                             )
                         ]
                         )
def test__get_attributes(data_dict, keys, expected_val):
    data_class_instance = Data.from_dict(data_dict)
    assert get_attr_val(data_class_instance, keys) == expected_val


@pytest.mark.parametrize("data_dict, attr_name",
                         [
                             (
                                 get_data(),
                                 'my_default_attr',
                             ),
                         ]
                         )
def test__get_default_attr(data_dict, attr_name):
    data_class_instance = Data.from_dict(data_dict)
    assert get_attr_val(data_class_instance, attr_name) == Data.__DEFAULT_VALUE




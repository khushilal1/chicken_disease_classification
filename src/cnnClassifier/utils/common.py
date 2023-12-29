import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


# @decorator
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type"""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loadded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e


@ensure_annotations
def created_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info("Created directory as:{path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    logger.info(f"json file is saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as load_json_file:
        content = json.load(load_json_file)
    logger.info(f"json file loaded successfully from :{path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file is loaded from:{path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return size_in_kb


@ensure_annotations
def decodeImage(imstring, fileName):
    imgdata = base64.b64decode(imstring)

    with open(fileName, "wb") as imag_file:
        imag_file.write(imgdata)
        imag_file.close()


@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as file_decoding:
        return base64.b64encode(file_decoding.read())

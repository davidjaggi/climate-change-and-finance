import os

def get_data_path():
    """
    Returns the path to the data directory.
    """
    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),"data")

def get_root_path():
    """
    Returns the path to the root directory.
    """
    # get root path
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_package_path():
    """
    Returns the path to the package directory.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_results_path():
    """
    Returns the path to the results directory.
    """
    return os.path.join(get_root_path(), "results")

if __name__ == '__main__':
    print(get_data_path())
    print(get_root_path())
    print(get_package_path())
    print(get_results_path())
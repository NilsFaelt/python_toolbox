import os 
import config

def create_scan_results_path_and_dir():
    scan_result_path = os.path.expanduser(f"{config.path_saved_scan_result}/scan_results/")
    os.makedirs(scan_result_path, exist_ok=True)
    return scan_result_path
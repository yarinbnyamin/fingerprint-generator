from configs import transforms_config
from configs.paths_config import dataset_paths


DATASETS = {
    "nist_sd14_synthesis": {
        "transforms": transforms_config.FingerprintSynthesisTransforms,
        "train_target_root": dataset_paths["nist_sd14_gt_train"],
        "test_target_root": dataset_paths["nist_sd14_gt_test"],
    },
    "nist_sd14_mnt": {
        "transforms": transforms_config.MntToFingerTransforms,
        "train_source_root": dataset_paths["nist_sd14_mnt_train"],
        "train_target_root": dataset_paths["nist_sd14_gt_train"],
        "test_source_root": dataset_paths["nist_sd14_mnt_test"],
        "test_target_root": dataset_paths["nist_sd14_gt_test"],
    },
}

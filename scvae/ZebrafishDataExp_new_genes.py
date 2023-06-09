'''
Description:
    Model running for PBMC data.
 
Author:
    Jiaqi Zhang
'''

from Running import normalAugmentation
from Py_Utils import readH5ad, getTimeStr, addDefaultArg, getDefualtLayerSize
import sys
sys.path.append("../")
sys.path.append("./")


# ------------------------------------------------------------------------------------
# Augmentation for different sampling ratios

# def clusterAugmentExp():
#     # parameters configuration
#     num_genes = 17789
#     latent_size = 32
#     num_layers = 2
#     layer_size_list = getDefualtLayerSize(num_genes, num_layers, latent_size)
#     date_str = getTimeStr()
#     config = {
#         "max_epoch": 50,
#         # "max_epoch" : 2,
#         "batch_size": 128,
#         "beta": 0.5,  # controls relative weight of reconstruction and KL loss, default = 0.5
#         "cluster_weight_type": 'sigmoid',  # vanilla (no pi), sigmoid, or softmax
#         "layer_size_list": layer_size_list,
#         "num_layers": num_layers,
#         # "learning_rate": 1e-4,
#         "learning_rate": 1e-4,
#     }
#     config = addDefaultArg(config)
#     # ------------------------------------------------
#     cluster_ls = [3]
#     cluster_size = {1:14123, 2:4716, 3:4574}
#     for c in cluster_ls:
#         print("=" * 70)
#         print("Cluster {}".format(c))
#         config["data"] = readH5ad("../../Data/PBMC/clusters/cluster{}_data-{}.h5ad".format(c, cluster_size[c]))
#         for s in [0.5, 0.25, 0.1, 0.05, 0.03, 0.01]: # different sampling ratio of training data
#             print("*" * 70)
#             print("Train data size : {}".format(s))
#             config["train_size"] = s
#             for t in range(5): # 5 trials
#                 print("#" * 70)
#                 print("TRIAL {}".format(t))
#                 config["model_save_path"] = \
#                     "../../Prediction/StructureVAE/PBMC_cluster{}-augmented-trial{}-VAE_model-{}.pt".format(
#                         c, t, s)
#                 config["prediction_save_path"] = \
#                     "../../Prediction/StructureVAE/PBMC_cluster{}-augmented-trial{}-VAE_estimation-{}.npy".format(
#                         c, t, s)
#                 clusterAugmentation(config)

# ------------------------------------------------------------------------------------
# Train, validate, test

def normalAugmentExp():
    # parameters configuration
    config = {
        "config_file": "./ZebrafishData_exp_new_genes.json",
        "need_save": True,
        # ------------------------------------------
        # "prediction_save_path": "../../Prediction/scVAE/mouse_cell-scVAE_estimation.npz",
        "test_preds_filename": "/users/srajakum/scratch/Structure_VAE_scRNA_Simulator/new_baseline_results/scvae/zebrafish/zebrafish-scVAE_test_preds.mtx",
    }
    normalAugmentation(config)


if __name__ == '__main__':
    # clusterAugmentExp()
    normalAugmentExp()
    pass

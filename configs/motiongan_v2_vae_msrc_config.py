{
    # Datasets: MSRC12, NTURGBD
    'data_set': 'MSRC12',
    'data_set_version': '',
    # Model version to train
    'model_version': 'v2',
    # Final epoch
    'num_epochs': 200,
    # Multiplies length of epoch, useful for tiny datasets
    'epoch_factor': 10,
    # Use pose VAE
    'use_pose_vae': True,
    # Path to pretrained pose VAE
    'pose_vae_save_path': 'save/pose_vae_v1_msrc',
}
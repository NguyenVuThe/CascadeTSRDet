# Table Recognition with Object Detection

## Objectives
This repo was created to learn and run experiments on Colab. Moreover, the repo is also for noting my requirements, settings and guides to run TSRDet smoothly.
## Requirements
1. Follow the official [Detectron2 installation guide](https://detectron2.readthedocs.io/en/latest/tutorials/install.html) that matches your CUDA version.

2. For clearer guide, please check the [guide.txt](https://github.com/NguyenVuThe/CascadeTSRDet/blob/master/guide.txt) file. This file shows how I setup the environment for the model on conda Windows 10, CUDA 11.8.

## Datasets and Pretrained Model

|Dataset | Weights|
|--------|--------|
|[PubTables1M](https://huggingface.co/datasets/bsmock/pubtables-1m) | [PubTables1M](https://drive.google.com/drive/folders/1BTB3aWw7R1xeztAp7NPrwpV75sejbxtb?usp=sharing)|
|[FinTabNet](https://huggingface.co/datasets/bsmock/FinTabNet.c)|[FinTabNet](https://drive.google.com/drive/folders/1lM8ydqVo9Ksje1-L2UDXCN62Vst4Mu2e?usp=sharing)|
|[SciTSR](https://huggingface.co/datasets/uobinxiao/SciTSR_Detection)|[SciTSR](https://drive.google.com/drive/folders/1IogkVxQ1IkOpvqtieYYoTir-NrXHsNdg?usp=sharing)|

## Configuration and Training

### 1. Setting the COCO Dataset

Check the [config.yaml](https://github.com/NguyenVuThe/CascadeTSRDet/blob/master/config.yaml) file and update the image and JSON paths to match your preferred dataset.

Set `Resume: True` if you want to continue training.  
Make sure to specify the path to the pretrained weight file under `OUTPUT_DIR` in the YAML files inside the [model_config](https://github.com/NguyenVuThe/CascadeTSRDet/tree/master/model_config) directory.

The training setting is also set in the the YAML files inside the [model_config](https://github.com/NguyenVuThe/CascadeTSRDet/tree/master/model_config)


### 2. Training
Check train_net.py and comment the unused datasets. Example here I'm using FinTabNet
```
#publaynet_args = argparse.Namespace(**args.PubTables1M)
publaynet_args = argparse.Namespace(**args.FinTabNet)
#publaynet_args = argparse.Namespace(**args.SciTSR)
```
Then run
```
python train_net.py
```

## Inference and Evaluation
Check the inference.py and test.sh for the inference. A sample inference command could be:
```
python inference.py --mode recognize --structure_config_path <path of config.yaml> --structure_model_path <path of weight> --structure_device cuda --image_dir <dir of table images> --out_dir <output dir> --html --visualize --csv --crop_padding 0
```

Check the teds.py for calculating the TEDS score.

## Citing
```
@article{xiao2025rethinking,
  title={Rethinking detection based table structure recognition for visually rich document images},
  author={Xiao, Bin and Simsek, Murat and Kantarci, Burak and Alkheir, Ala Abu},
  journal={Expert Systems with Applications},
  pages={126461},
  year={2025},
  publisher={Elsevier}
}
```
## Paper Link
### Rethinking Detection Based Table Structure Recognition for Visually Rich Document Images
This paper has been published in Expert Systems with Applications, checkout the link below for the full version:
https://www.sciencedirect.com/science/article/pii/S0957417425000831


## Acknowledgement
This project heavily relys on [Table-Transformer](https://github.com/microsoft/table-transformer), especially for the post-processing part. We thank the authors for sharing their implementations and related resources.

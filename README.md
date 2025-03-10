# Winter School 2025 Workshop: The Machine Learning behind PlantSeg

## Abstract

This workshop will introduce PlantSeg 2.0, the latest version of the popular tool for segmenting large volumetric images. Together, we will walk through the machine learning models powering PlantSeg, learn how to use its new napari-based GUI, select pre-trained networks, adjust parameters, correct results, and launch headless jobs.
After this introduction, the workshop will split into two tracks. Participants interested in applying PlantSeg to their own data can do so. At the same time, those keen to explore the underlying machine learning can follow a hands-on Python tutorial showing how the method works under the hood.

## Workshop Structure

- Introduction to PlantSeg
- Follow Along Demo:
  - Running PlantSeg as a Napari plugin
  - Proofreading Segmentation
- Hands On Exercises:
  - Advanced Usage
  - Implement a PlantSeg pipeline from Scratch

## Material

- [Slides](https://docs.google.com/presentation/d/1gx8NNpPcyrKZP3_UGGO0uBX21oGf7Xu5H7WO3UbF7E8/edit?usp=sharing)
- [Download Sample Data](https://drive.google.com/drive/folders/1djDf4TwTfQaxLKoLOvHG0zWRWZ76yhCY?usp=sharing)

## Installation

To create a new conda environment with PlantSeg, you can use the following command:

```bash
mamba create -n plant-seg -c pytorch -c nvidia -c conda-forge pytorch cpuonly plant-seg --no-channel-priority
```

This will create a new environment called `plant-seg` with all the necessary dependencies. To activate the environment, use the following command:

```bash
conda activate plant-seg
```

If you have a GPU, or you need more detailed instructions, please refer to the [Plantseg Installation](https://kreshuklab.github.io/plant-seg/chapters/getting_started/installation/).

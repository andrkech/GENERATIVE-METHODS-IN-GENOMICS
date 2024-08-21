**GENERATIVE-METHODS-IN-GENOMICS**

**Abstract**

This project tackles the challenge of data scarcity in bioinformatics by exploring the use of generative methods for synthetic data creation in genomics. We focus on generating in silico FASTQ files with specific properties, employing a Generative Adversarial Network (GAN) model trained on a custom dataset of quality scores extracted from real FASTQ files. 

Although encountering common GAN training challenges, the model manages to capture some distinctive features and patterns of the  training data. This shows the potential of GANs for this task, particularly when suitable techniques are applied or if  more advanced methods are integrated, like attention-based models. 

This dissertation aims to serve as a stepping stone for further exploration and wider adoption of deep generative models in bioinformatics, in order to address the ongoing issue of data limitations.

**Framework**

The overall framework of the complete algorithm is illustrated below:
![image](https://github.com/user-attachments/assets/ce45287a-fe6e-48ce-b702-94f9f615421f)

**Scripts Overview**

Following is an overview of the scripts. Note that whle access has been provided for the directories used, they need to be adjusted for other users, as the files should be located to the "Shared with me" folder in Google Drive.

1.FASTQ_Data_Miner

The Data Miner module gathers FASTQ files from a specified source. It accepts an XML file from the European Nucleotide Archive (ENA) as input and extracts FASTQ files from one or multiple experiments, ensuring dataset diversity. However, in this particular use case, a specific project has been chosen to ensure homogeneity of the data. 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lTVYho1DjXxlDX304Kd6xIDXjlq4s_lu)

2.FASTQ_Dataset_Organizer

The Dataset Organizer has been developed as a toolkit mainly for an extension of the script. In the currect project, only the functionality that creates a signle group is utilized. Other methods included in this script could be used in order to categorize and structure collected FASTQ files based on metadata information, handling unevenly distributed data, such as sequences with varying lengths, offering scalability and adaptability.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OI6jSo-3v7y64IhycxfoN9LSK3XQI0gY?usp=sharing)

3.FASTQ_DataLoader

Responsible for preprocessing, the Data Loader formats and prepares the dataset to suit the input requirements of the GAN model, ensuring seamless integration into the training pipeline.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aFsMNGM69FfGGLU0lyLsa6G3YTgu0Alj)

4.PHRED_GAN

The GAN architecture is specifically designed to generate synthetic quality scores, mirroring the characteristics of PHRED scores of authentic FASTQ files.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1b99S9syvNVy8yta9YlL3uZ30KrEGQ_Qz?usp=sharing)

5.VARIANT_READS_GENERATOR

The Variant Reads Generator component enriches the synthetic data generation process by allowing users to define genetic variations such as SNPs, insertions, and deletions.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OI6jSo-3v7y64IhycxfoN9LSK3XQI0gY#scrollTo=MLiiBeYtyj73)

By integrating these modules, this thesis aims to contribute to advancing generative methods in genomics via deep learning implementation, offering a novel framework for generating synthetic genomic data crucial for various bioinformatics and genomics applications.

**Results**

Information about the resulting FASTQ file, in comparison with real ones, is demonstrated in the plots below:

Generated FASTQ file:

![image](https://github.com/user-attachments/assets/0616bb50-11b7-4742-b8e3-e2d0ca9a5204)

Real FASTQ files:

![image](https://github.com/user-attachments/assets/df8b5406-fc51-4f5b-8135-a196be45124c)

Observations:

The generated file shows both similarities and areas of improvement. For instance, while it mimics the general quality score distribution and GC content of real data, it exhibits distinct peaks in the middle and a higher frequency of lower quality scores. This suggests the model captures the overall trend but struggles with finer details of quality score distribution and nucleotide composition.

**Discussion**

This study demonstrates the potential of GANs for generating synthetic FASTQ files, but further exploration is needed. Hyperparameter tuning, alternative GAN architectures, and attention-based models could lead to improved performance. Expanding the scope to include diverse genomic variations and handling various sequence lengths would enhance the framework's applicability. Additionally, incorporating error profiles would further increase the realism of the generated FASTQ files.

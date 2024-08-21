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

**1. Data Miner**

The Data Miner module focuses on gathering FASTQ files essential for training the GAN model. It accepts an XML file from the European Nucleotide Archive (ENA) as input and extracts FASTQ files from one or multiple experiments, ensuring dataset diversity.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lTVYho1DjXxlDX304Kd6xIDXjlq4s_lu)

**2. Dataset Organizer**

The Dataset Organizer categorizes and structures collected FASTQ files based on metadata information. This component paves the way for handling unevenly distributed data, such as sequences with varying lengths, offering scalability and adaptability.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]
(https://colab.research.google.com/drive/1OI6jSo-3v7y64IhycxfoN9LSK3XQI0gY#scrollTo=MLiiBeYtyj73)

**3. Data Loader**

Responsible for preprocessing, the Data Loader formats and prepares the dataset to suit the input requirements of the GAN model, ensuring seamless integration into the training pipeline.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aFsMNGM69FfGGLU0lyLsa6G3YTgu0Alj)

**4. Generative Adversarial Network (GAN)**

The GAN architecture, known as FASTQ GAN, is specifically designed to generate synthetic DNA sequences paired with quality scores, mirroring the characteristics of authentic FASTQ files.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]
(https://colab.research.google.com/drive/1OI6jSo-3v7y64IhycxfoN9LSK3XQI0gY#scrollTo=MLiiBeYtyj73)

**5. Variant Generator**

The Variant Generator component enriches the synthetic data generation process by allowing users to define genetic variations such as single nucleotide polymorphisms (SNPs), insertions, and deletions.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]
(https://colab.research.google.com/drive/1OI6jSo-3v7y64IhycxfoN9LSK3XQI0gY#scrollTo=MLiiBeYtyj73)

By integrating these modules, this thesis aims to contribute to advancing generative methods in genomics via deep learning implementation, offering a novel framework for generating synthetic genomic data crucial for various bioinformatics and genomics applications.

**Results**

Information about the resulting FASTQ file, in comparison with real ones, is demonstrated in the plots below:

Generated FASTQ file:

![image](https://github.com/user-attachments/assets/2cc9c5b7-89dc-48b3-8a58-7e6ceaf498a1)
![image](https://github.com/user-attachments/assets/399e93a1-c7a0-48fc-84ba-2a1591de0580)
![image](https://github.com/user-attachments/assets/7f012dae-8688-4994-b568-5ab0d71acc15)

Real FASTQ files:

![image](https://github.com/user-attachments/assets/b89113d8-c6c5-42d0-9dcc-45c4ba114fa2)
![image](https://github.com/user-attachments/assets/15a6299f-dc4d-4e81-8405-7925202ac36a)
![image](https://github.com/user-attachments/assets/fc9d5dba-5db5-4158-9448-8015991b2ee4)

![image](https://github.com/user-attachments/assets/cb9d600a-7e0d-404e-b2aa-a438a492e211)
![image](https://github.com/user-attachments/assets/6346ae07-0a48-4c3e-a635-45689d6b9453)
![image](https://github.com/user-attachments/assets/b5c329ec-2be6-46dc-8087-0ef8ef546d10)

Observations:

The generated file shows both similarities and areas of improvement. For instance, while it mimics the general quality score distribution and GC content of real data, it exhibits distinct peaks in the middle and a higher frequency of lower quality scores. This suggests the model captures the overall trend but struggles with finer details of quality score distribution and nucleotide composition.

**Discussion**

This study demonstrates the potential of GANs for generating synthetic FASTQ files, but further exploration is needed. Hyperparameter tuning, alternative GAN architectures, and attention-based models could lead to improved performance. Expanding the scope to include diverse genomic variations and handling various sequence lengths would enhance the framework's applicability. Additionally, incorporating error profiles would further increase the realism of the generated FASTQ files.

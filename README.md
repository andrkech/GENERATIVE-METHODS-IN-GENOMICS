GENERATIVE-METHODS-IN-GENOMICS

**0. Abstract**
This thesis presents an innovative approach for synthesizing FASTQ files using Generative Adversarial Networks (GANs), aiming to create realistic and diverse genomic datasets. The methodology comprises several integral components including data mining, organization, loading, GAN architecture design (FASTQ GAN), and variant generation, forming a novel pipeline for synthetic genomic data generation.

**1. Data Miner**

The Data Miner module focuses on gathering FASTQ files essential for training the GAN model. It accepts an XML file from the European Nucleotide Archive (ENA) as input and extracts FASTQ files from one or multiple experiments, ensuring dataset diversity.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lTVYho1DjXxlDX304Kd6xIDXjlq4s_lu)

**2. Dataset Organizer**

The Dataset Organizer categorizes and structures collected FASTQ files based on metadata information. This component paves the way for handling unevenly distributed data, such as sequences with varying lengths, offering scalability and adaptability.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OI6jSo-3v7y64IhycxfoN9LSK3XQI0gY#scrollTo=MLiiBeYtyj73)

**3. Data Loader**

Responsible for preprocessing, the Data Loader formats and prepares the dataset to suit the input requirements of the GAN model, ensuring seamless integration into the training pipeline.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aFsMNGM69FfGGLU0lyLsa6G3YTgu0Alj)

**4. Generative Adversarial Network (GAN)**

The GAN architecture, known as FASTQ GAN, is specifically designed to generate synthetic DNA sequences paired with quality scores, mirroring the characteristics of authentic FASTQ files.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OI6jSo-3v7y64IhycxfoN9LSK3XQI0gY#scrollTo=MLiiBeYtyj73)

**5. Variant Generator**

The Variant Generator component enriches the synthetic data generation process by allowing users to define genetic variations such as single nucleotide polymorphisms (SNPs), insertions, and deletions.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OI6jSo-3v7y64IhycxfoN9LSK3XQI0gY#scrollTo=MLiiBeYtyj73)

By integrating these modules, this thesis aims to contribute to advancing generative methods in genomics via deep learning implementation, offering a novel framework for generating synthetic genomic data crucial for various bioinformatics and genomics applications.

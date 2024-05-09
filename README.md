GENERATIVE-METHODS-IN-GENOMICS

Abstract:
The thesis aims to develop a novel approach for generating synthetic FASTQ files leveraging Generative Adversarial Networks (GANs). The process involves several key components, including data mining, organization, loading, GAN architecture design (FASTQ GAN), and variant generation. The integration of these components forms a comprehensive pipeline for the generation of realistic and diverse synthetic genomic data.

Data Miner: The Data Miner component is responsible for collecting Fastq files in order to build the dataset needed to train the GAN model. In the cases used, it takes an XML file from ENA as input and extracts the FASTQ files contained in one or more experiments, allowing for variance in the dataset.
[![Open in Colab](https://colab.research.google.com/drive/1lTVYho1DjXxlDX304Kd6xIDXjlq4s_lu)]

Organizer: Once the Fastq files are collected, the Organizer component categorizes and organizes them based on metadata information such as sample identifiers, experimental conditions, or sequence characteristics. This ensures efficient management and retrieval of data during subsequent analysis steps.

Data Loader: The Data Loader component reads and preprocesses the Fastq files, extracting important sequence information such as read length, quality scores, and nucleotide composition. It prepares the data for downstream analysis tasks, including machine learning and variant calling.

Generative Adversarial Network (GAN): The GAN component employs deep learning techniques to generate synthetic DNA sequences that mimic the characteristics of real Fastq files. By learning from the patterns and distributions present in the training data, the GAN can produce realistic synthetic sequences for augmenting datasets or testing algorithms.

Variant Generator: The Variant Generator component introduces genetic variations into existing DNA sequences to simulate mutagenesis or evolutionary processes. It can generate single nucleotide polymorphisms (SNPs), insertions, deletions, or other types of mutations based on user-defined parameters.

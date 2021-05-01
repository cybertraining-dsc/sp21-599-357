# Project: Structural Protein Sequences Classification

[![Check Report](https://github.com/cybertraining-dsc/sp21-599-357/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/sp21-599-357/actions)
[![Status](https://github.com/cybertraining-dsc/sp21-599-357/workflows/Status/badge.svg)](https://github.com/cybertraining-dsc/sp21-599-357/actions)
Status: in progress, Type: Project



* :o2: Refernces shoudl be defined by now

Jiayu Li, [sp21-599-357](https://github.com/cybertraining-dsc/sp21-599-357/), [Edit](https://github.com/cybertraining-dsc/sp21-599-357/blob/main/project/index.md)

{{% pageinfo %}}

## Abstract

The goal of this project is to classify protein families based on their sequence of aminoacids. 
In the protein structure data set, each protein is classified according to its function. Categories include: HYDROLASE, OXYGEN TRANSPORT, VIRUS, SIGNALING PROTEIN, etc. dozens of kinds. In this project, we will use nucleic acid sequences to predict the type of protein.


Related research includes BLAST, which is a protein search engine.

**Keywords:** Protein Sequences, Deep learning

## 1. Introduction

The structure and function of a protein are determined by the amino acid sequence that composes it. The amino acid sequence can be regarded as a language composed of 4 different characters. In recent years, due to the development of deep learning, the ability of deep neural networks to process natural language has reached or even surpassed humans in some areas. In this project, we tried to treat the amino acid sequence as a language and use the existing deep learning model to analyze it to achieve the purpose of inferring its function.


The data sets used in the project come from Research Collaboratory for Structural Bioinformatics (RCSB) and Protein Data Bank (PDB).

The data set contains approximately 400,000 amino acid sequences and has been labeled. The label is the family to which the protein belongs.

The data set contains approximately 400,000 amino acid sequences and has been labeled. The label is the family to which the protein belongs. The protein family includes HYDROLASE, HYDROLASE/HYDROLASE INHIBITOR, IMMUNE SYSTEM, LYASE, OXIDOREDUCTASE, etc. Therefore this problem can be regarded as a classification problem. The input of the model is a sequence, the length of the sequence is uncertain, and the output of the model is one of several categories.
By comparing DNN, CNN, LSTM and other common models, we have achieved effective prediction of protein energy supply.


## 2. Dataset

PDB is a data set dedicated to the three-dimensional structure of proteins and nucleic acids. It has a very long history, dating back to 1971. In 2003, PDB developed into an international organization wwPDB. Other members of wwPDB, including PDBe (Europe), RCSB (United States), and PDBj (Japan) also provide PDB with a center for data accumulation, processing and release. Although PDB data is submitted by scientists from all over the world, each piece of data submitted will be reviewed and annotated by wwPDB staff, and whether the data is reasonable or not. The PDB and the software it provides are now free and open to the public.
In the past few decades, the number of PDB structures has grown at an exponential rate.

Structural biologists around the world use methods such as X-ray crystallography, NMR spectroscopy, and cryo-electron microscopy to determine the position of each atom relative to each other in the molecule. Then they will submit this structural information, wwPDB will annotate it and publish it to the database publicly.

You can search for ribosomes, oncogenes, drug targets, and even the structure of the entire virus in the PDB data set. However, the number of structures archived in the PDB is huge, and finding the information you need may be a difficult task.

The information in the PDB data set mainly includes: protein/nucleic acid source, protein/nucleic acid molecule composition, atomic coordinates, experimental methods used to determine the structure.
Structural Protein Sequences Dataset: https://www.kaggle.com/shahir/protein-data-set/code

Protein dataset classification: https://www.kaggle.com/rafay12/anti-freeze-protein-classification

RCSB PDB: https://www.rcsb.org/

## 3. Deep learning algorithm
Possible candidate algorithms include LSTM, CNN, SVM, etc. In actual problems, it may be necessary to combine multiple algorithms to achieve higher accuracy.


  

## 4. Benchmark

Your project must include a benchmark. The easiest is to use cloudmesh-common [^2]
 
## 5. Conclusion

A convincing but not fake conclusion should summarize what the conclusion of the project is.

## 6. Acknowledgments

Please add acknowledgments to all that contributed or helped on this project.  

## 7. References

[^1]: Use of energy explained - Energy use in homes, [Online resource] 
      <https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php>


[^2]: Gregor von Laszewski, Cloudmesh StopWatch and Benchmark from the Cloudmesh Common Library, [GitHub] 
      <https://github.com/cloudmesh/cloudmesh-common>


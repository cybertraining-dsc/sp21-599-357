# Project: Structural Protein Sequences Classification

[![Check Report](https://github.com/cybertraining-dsc/sp21-599-357/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/sp21-599-357/actions)
[![Status](https://github.com/cybertraining-dsc/sp21-599-357/workflows/Status/badge.svg)](https://github.com/cybertraining-dsc/sp21-599-357/actions)
Status: in progress, Type: Project


* :o2: Introduction missing

* :o2: Abstract should be defined by now
* :o2: Refernces shoudl be defined by now

Jiayu Li, [sp21-599-357](https://github.com/cybertraining-dsc/sp21-599-357/), [Edit](https://github.com/cybertraining-dsc/sp21-599-357/blob/main/project/index.md)

{{% pageinfo %}}

## Abstract

The goal of this project is to classify protein families based on their sequence of aminoacids. 
In the protein structure data set, each protein is classified according to its function. Categories include: HYDROLASE, OXYGEN TRANSPORT, VIRUS, SIGNALING PROTEIN, etc. dozens of kinds. In this project, we will use nucleic acid sequences to predict the type of protein.


Related research includes BLAST, which is a protein search engine.

**Keywords:** tensorflow, example. 

## 1. Introduction

Please not ethat an up to date version of these instructions is available at

* <https://github.com/cybertraining-dsc/hid-example/blob/main/project/index.md>

Here comes a convincing introduction to the problem
## 2. Dataset
Structural Protein Sequences Dataset: https://www.kaggle.com/shahir/protein-data-set/code

Protein dataset classification: https://www.kaggle.com/rafay12/anti-freeze-protein-classification

RCSB PDB: https://www.rcsb.org/

## 3. Deep learning algorithm
Possible candidate algorithms include LSTM, CNN, SVM, etc. In actual problems, it may be necessary to combine multiple algorithms to achieve higher accuracy.


## 4. Timeline
* Week 1: Collect data, understand the data.
* Week 2: Data preprocessing, data visualization.
* Week 3: Find related works and test existing algorithms.
* Week 4: Protein structure prediction or classification based on existing work.
* Week 5: Continue the previous experiment. Complete project report
## 2. Report Format

The report is written in (hugo) markdown and not commonmark. As such some features are not visible in GitHub. You can 
set up hugo on your local computer if you want to see how it renders or commit and wait 10 minutes once your report is 
bound into cybertraining.

It is to be noted that markdown works best if you include an empty line before and after each context change. 
Thus the following is wrong:

```
# This is My Headline
This author does ignore proper markdown while not using empty lines between context changes
1. This is because this author ignors all best practices
```

Instead, this should be 

```
# This is My Headline

We do not ignore proper markdown while using empty lines between context changes

1. This is because we encourage best practices to cause issues.
```

## 2.1. GitHub Actions

When going to GitHub Actions you will see a report is autmatically generated with some help on improving your markdown. 
We will not review any document that does not pass this check.

## 2.2. PAst Copy from Word or other Editors is a Disaster!

We recommend that you sue a proper that is integrated with GitHub or you use the commandline tools. We may include 
comments into your document that you will have to fix, If you juys past copy you will 

1. Not learn how to use GitHub properly and we deduct points
2. Overwrite our coments that you than may miss and may result in point deductions as you have not addressed them.

## 2.3. Report or Project

You have two choices for the final project. 

1. Project, That is a final report that includes code.
2. Report, that is a final project without code.
   
YOu will be including the type of the project as a prefix to your title, as well as in the Type tag
at the beginning of your project.

## 3. Using Images

![Figure 1](https://github.com/cybertraining-dsc/fa20-523-314/raw/main/project/images/chart.png)

**Figure 1:** Images can be included in the report, but if they are copied you must cite them [^1].

## 4. Using itemized lists only where needed

Remember this is not a powerpoint presentation, but a report so we recommend

1. Use itemized or enumeration lists sparingly
2. When using bulleted lists use * and not - 
   
## 5. Datasets

PDB is a data set dedicated to the three-dimensional structure of proteins and nucleic acids. It has a very long history, dating back to 1971. In 2003, PDB developed into an international organization wwPDB. Other members of wwPDB, including PDBe (Europe), RCSB (United States), and PDBj (Japan) also provide PDB with a center for data accumulation, processing and release. Although PDB data is submitted by scientists from all over the world, each piece of data submitted will be reviewed and annotated by wwPDB staff, and whether the data is reasonable or not. The PDB and the software it provides are now free and open to the public.
In the past few decades, the number of PDB structures has grown at an exponential rate.

Structural biologists around the world use methods such as X-ray crystallography, NMR spectroscopy, and cryo-electron microscopy to determine the position of each atom relative to each other in the molecule. Then they will submit this structural information, wwPDB will annotate it and publish it to the database publicly.

You can search for ribosomes, oncogenes, drug targets, and even the structure of the entire virus in the PDB data set. However, the number of structures archived in the PDB is huge, and finding the information you need may be a difficult task.

The information in the PDB data set mainly includes: protein/nucleic acid source, protein/nucleic acid molecule composition, atomic coordinates, experimental methods used to determine the structure.


## 6. Benchmark

Your project must include a benchmark. The easiest is to use cloudmesh-common [^2]
 
## 6. Conclusion

A convincing but not fake conclusion should summarize what the conclusion of the project is.

## 8. Acknowledgments

Please add acknowledgments to all that contributed or helped on this project.  

## 9. References

Your report must include at least 6 references. Please use customary academic citation and not just URLs. As we will at 
one point automatically change the references from superscript to square brackets it is best to introduce a space before 
the first square bracket.

[^1]: Use of energy explained - Energy use in homes, [Online resource] 
      <https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php>


[^2]: Gregor von Laszewski, Cloudmesh StopWatch and Benchmark from the Cloudmesh Common Library, [GitHub] 
      <https://github.com/cloudmesh/cloudmesh-common>


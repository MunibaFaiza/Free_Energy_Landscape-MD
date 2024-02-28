# Free_Energy_Landscape-MD: A Python package to generate free energy landscape (FEL) of molecular dynamics (MD) simulations obtained from GROMACS.

A Python package to generate Free Energy Landscape (FEL) based in Principal Component Analysis (PCA) of the Molecular Dynamics (MD) trajectory.
This package provides a 3D FEL plot showing the minima points. It utilizes principal components of the MD trajectory to generate the FEL. Additionally, it offers specific time frames corresponding to the minima regions in the FEL.

Before using the script to generate the FEL, PCA must be performed. The complete process, from performing PCA to extracting the time frames corresponding to the minima regions, is explained in [this article](). 

The package includes two main files:

+ FEL_Time_Frame_Extractor_CaseI.ipynb,
+ FEL_Time_Frame_Extractor_CaseII.ipynb,

along with other required input files such as the MD trajectory file and example output files. The CaseI file is designed for long normal MD simulations without any significant noise or artifacts. On the other hand, the CaseII file is intended for simulations where the time frames are not readily identifiable in the PCA output file (PC1PC2.xvg). Further details are provided in the above-mentioned article.

## Usage:
Doownload this package and unzip all files. Generate input files as explained in the article. Use the script to generate the FEL and extract time frames. Finally, in the last step, take snapshots of the time frames as shown in the article.

### How to cite:
Faiza, M., 2024. Free_Energy_Landscape-MD: Python package to create Free Energy Landscape using PCA from GROMACS., 10(2): page 8-12. https://bioinformaticsreview.com/20240228/free_energy_landscape-md-python-package-to-create-free-energy-landscape-using-pca-from-gromacs/
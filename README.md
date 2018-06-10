# Visualizations on transcription factor data in different cell-types

The original excel sheet and an exported .csv file are located in the `input_data` folder. Each of the remaining folders contain a visualization and the recipe for the data-transformation in the form of a Makefile (go to the directory and run `make`).


## Gene co-expression flareplot

The flareplot file and the script to generate it can be found in the `flareplot` folder. This repo has "pages" enabled, so the flareplot can be seen directly here:

* [Flareplot link](https://rasmusfonseca.github.io/TranscriptionFactors/flareplot/index.html)

An issue with using gene co-expression as the definition for a flareplot edge is that all genes expressed in a particular cell type will form cliques and hence the graph will become very dense. I managed to pull it up and interact with it on my workstation, but my laptop seems to break down for now (I'll keep playing to find a workaround). 


## Heatmap clustered on both genes and cell types

The `clustermap` folder contains a heatmap visualization of the entire matrix with rows and columns ordered according to single-linkage hierarchical clustering:

* [Clustermap png](https://raw.githubusercontent.com/RasmusFonseca/TranscriptionFactors/master/clustermap/clustermap.png)

Theres a number of observations about related genes and cell types that can be made by looking for blocks in this map. 

* Neurod1, Isl1, and Pax6 are all strongly present in the pancreas (pancreatic D cell, type B pancreatic cell, pancreatic A cell and pancreatic PP cell).
* E2f2 and Ikzf1 have fairly similar but weak cell-type dependencies.
* Ets1, Tbx21, and Txk are present together in several cell types but especially in killer cells and endothelial cells. 
* Sox18 and Tcf15 seem to be related through multiple cell types as well.
* A couple of T-cells cluster together (`T cell_fat`, `immature T cell_Thymus`, `T cell_Spleen`) but others seem very different in their transcription factor profiles (e.g. `regulatory T cell_Marrow`, `T cell_lung`, and `T cell_Limb_Muscle`).

## Tensorflow projection

Dimensionality reduction can be useful to verify clustering and get a sense for the ratio of outliers. Using tensorflows "Embedding projector" these projections can be explored interactively:

* [PCA/tSNE on cell types](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/RasmusFonseca/TranscriptionFactors/master/tensor_projection/celltype_config.json)
* [PCA/tSNE on genes](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/RasmusFonseca/TranscriptionFactors/master/tensor_projection/gene_config.json)

I found it useful to switch to 2D (disable the checkbox in lower left corner next to "Component #3"), and then click the "A" button near the top to see labels. For the cell type projection, colors can be enabled. 

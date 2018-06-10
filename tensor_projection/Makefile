
all: gene_data.tsv celltype_data.tsv gene_metadata.tsv celltype_metadata.tsv

gene_data.tsv: ../input_data/Extended_Data_Table_4.csv
	tail -n +2 $< | cut -f 2- -d ',' | tr ',' '\t' | sed 's/NA/0/g' > $@

celltype_data.tsv: gene_data.tsv
	python -c "import numpy as np; d = np.loadtxt('$<'); np.savetxt('$@', d.T, fmt='%.6f', delimiter='\t')"

gene_metadata.tsv: ../input_data/Extended_Data_Table_4.csv
	cut -f 1 -d ',' $< > $@

Col_headers.txt: ../input_data/Extended_Data_Table_4.csv
	head -n 1 $< | cut -f 2- -d ',' | tr ',' '\n' > $@

celltype_metadata.tsv: Col_headers.txt
	echo "Cell type\tTissue" > $@
	cat $< | sed 's/\([^_]*\)_\(.*\)/\1_\2	\2/' >> $@

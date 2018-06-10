

clustermap.png: Extended_Data_Table_4_norowheaders.csv Row_headers.txt
	python table_to_clustermap.py $^ $@

Extended_Data_Table_4_norowheaders.csv: ../input_data/Extended_Data_Table_4.csv
	cut -f 2- -d ',' $< > $@

Row_headers.txt: ../input_data/Extended_Data_Table_4.csv
	cut -f 1 -d ',' $< | tail -n +2 > $@

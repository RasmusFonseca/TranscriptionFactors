

Extended_Data_Table_4.json: Extended_Data_Table_4_norowheaders.csv Row_headers.txt
	python table_to_flare.py $^ $@

Extended_Data_Table_4_norowheaders.csv: ../input_data/Extended_Data_Table_4.csv
	cut -f 2- -d ',' $< > $@

Row_headers.txt: ../input_data/Extended_Data_Table_4.csv
	cut -f 1 -d ',' $< > $@

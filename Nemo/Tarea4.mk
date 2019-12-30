PuntoNemo.pdf: Plots.py Punto_Nemo.csv map_data.txt
	python Plots.py

Punto_Nemo.csv : a.out
	./a.out

a.out: GeographicPoint.c map_data.txt
	gcc GeographicPoint.c -lm

clean:
	rm  *.csv *.out

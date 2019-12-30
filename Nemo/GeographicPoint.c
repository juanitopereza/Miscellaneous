#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define rows 500
#define cols 744
#define N 2000

int EncuentraTierra(int *datos, int *Tierra);
int MenorDistancia(int x, int y, int *Tierra);
void MCMC(int *datos, int *Tierra);

int xGuess = 300;
int yGuess = 100;
int m = 0;
int x=0;
int y=0;
double r=0;


int main() {

  int i = 0, j = 0,length = 15000; // i for row, j for column

    char line_buffer[length]; // prepares a list of length chars to store a single line of the document
    char *split_buffer; // prepares a pointer of chars to store a single word or number in the line_buffer

    FILE *dataFile;
    dataFile = fopen("map_data.txt", "r");

    int *datos =(int *) malloc(rows*cols*sizeof(int));
    int *Tierra =(int *) malloc(rows*cols*sizeof(int));


    if (dataFile == NULL)
    {
        // verifies the file exists
        printf("Error Reading File\n");
        exit(0);
    }

    while(fgets(line_buffer, length, dataFile) != NULL) // reads up to length characters of the dataFile and stores them at the line_buffer
    {
        j = 0;
        split_buffer = strtok(line_buffer, " "); // first word of the line
        while (split_buffer != NULL)
        {
          datos[i*cols+j] = strtod(split_buffer, NULL); // changes a char representation of a number to the float/double representation
          //printf("fila %d, col %d = %d\n", i, j, datos[i*cols+j] );
          split_buffer = strtok(NULL, " ");
          j += 1;
        }
        i += 1;
    }

    fclose(dataFile);

    srand(time(NULL));
    m = EncuentraTierra(datos, Tierra);


    //printf("la distancia es : %f", dPrev);

    MCMC(datos, Tierra);

    printf("Las coordenadas del punto son : %lf, %lf\n", y*(-90.0/250.0) - 90.0, x*(360.0/744.0) - 180.0);

    FILE *data1;
    data1 = fopen("Punto_Nemo.csv", "w");
    fprintf(data1, "%d,%d,%lf", x, y, r);
    fclose(data1);

    return 0;
}
void MCMC(int *datos, int *Tierra){

  int l=0;
  double alpha=0, dPrev= 0, dPos = 0;
  while (l < N) {

    double a = ((double) rand()/RAND_MAX);
    double b = ((double) rand()/RAND_MAX);

    int xNew = 0;
    int yNew = 0;
    xNew = xGuess;
    yNew = yGuess;

    printf("xNew es: %d, yNew es: %d\n",xNew, yNew);

    if (a > 0.5 && b > 0.5) {
      xNew += 1;
    } else if (a > 0.5 && b < 0.5) {
      xNew -= 1;
    }
    if (a < 0.5 && b > 0.5) {
      yNew += 1;
    } else if (a < 0.5 && b < 0.5) {
      yNew -= 1;
    }

    printf("xNew--> es: %d, yNew--> es: %d\n",xNew, yNew);

    dPrev = MenorDistancia(xGuess, yGuess, Tierra);
    dPos = MenorDistancia(xNew, yNew, Tierra);
    alpha = exp(dPos - dPrev);

    if(dPos > r){
      x = xNew;
      y = yNew;
      r = dPos;
    }

    double c = ((double) (rand()/RAND_MAX));
    if (alpha > 1.0) {
      xGuess = xNew;
      yGuess = yNew;
      alpha = 1;
    } else if (alpha > c) {
      xGuess = xNew;
      yGuess = yNew;
    }
    l += 1;
}
}
int EncuentraTierra(int *datos, int *Tierra){
  int i = 0, j =0, k=0;
  for (i = 0; i < rows; i++) {
    for ( j = 0; j < cols; j++) {
      if(datos[i*cols+j] == 1){
        Tierra[k*2] = i;
        Tierra[k*2+1] = j;
        k += 1;
      }
    }
  }
  return k;
}
int MenorDistancia(int x, int y, int *Tierra){
  double D = 1000.0;
  double temp = 0.0;
  int i=0;
  for ( i = 0; i < m; i++) {
    temp = sqrt(pow(x-Tierra[i*2],2)+pow(y-Tierra[i*2+1],2));
    if (temp < D) {
      D = temp;
    }
  }
  return D;
}

#include "NativeFunctionsApi.h"

int add_two_numbers(int a, int b)
{
    return a + b;
}

float calcular_media(float* numeros, int tam) 
{
    double suma = 0;

    for (int i = 0; i < tam; i++) 
    {
        suma += numeros[i];
    }
    
    return suma / tam;
}
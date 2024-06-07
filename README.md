# GS - Computational Thinking With Python

## Integrantes 👋
<ul>
    <li>João Marcelo Furtado Romero (RM555199)</li>
    <li>Kayky Silva Stiliano (RM555148)</li>
</ul>

## Instruções
O arquivo ```c main.py``` é o arquivo principal que deve ser rodado e é recomendado usar o terminal no tamanho 75% ou tela cheia.

## Explicação do Projeto 📖
Um app em Python, com o tema de poluição marinha, que dá ao usuário escolhas de seção onde há uma simulação em formato de "mini-game" que usuário escolhe uma praia e procura por coisas, uma seção de dados capturados pelos drones que novamente é escolhida a praia desejada no qual haverá duas opções de display das informações sendo uma "opções detalhadas" com todas os resultados encontrados para aquela praia e outra "opções específicas" onde o usuário escolhe qual dado ele deseja ver tendo a possibilidade de fazer novas pesquisas também. Por fim há uma seção de doação onde o usuário pode doar uma quantia para a empresa que ajuda diretamente na salvação dos oceanos.

 
## Dependências 📦
<ul>
    <li>helpers.py</li>
    <li>simulacao.py</li>
    <li>simulacao_paths.py</li>
    <li>sysfunctions.py</li>
</ul>
 
<br>

## Explicando o <a href="path">Código</a> 🧑‍💻
 
```c
#include <LiquidCrystal.h>
#include <DHT.h>
#include <Servo.h>

// LCD
const int rs = 2, en = 3, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// DHT Sensor (simulando sensor de oxigênio no lugar do de humidade)
#define DHTPIN A0
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// LDR
float valor_ldr;

// Servo Motor
Servo servo;
const int servoPin = 9;
int pos = 0;
int increment = 1;
int startMotor = 6;
int counterRotation = 0;
unsigned long previousMillis = 0;
const long interval = 20; 
 
// Sensor de pH (Potentiometer 1)
const int pHpin = A2;
float pHValue;
float pHRead;

// Sensor de gás CO2 (Potentiometer 2)
const int gasPinCO2 = A3;
int CO2Value;

// Sensor de gás CH4 (Potentiometer 3)
const int gasPinCH4 = A4;
int CH4Value;

// Sensor de proximidade
const int trigPin = 10;
const int echoPin = 1; 
long duration;
int distance;

// Buzzer
const int buzzerPin = 8;

// LED Pins
const int ledR = 13;
const int ledY = 12;
const int ledG = 11;
```
<hr>

 ## Funções 🛠️


 
<center>Este projeto encontra sob a <a href="path">MIT License.</a></center>

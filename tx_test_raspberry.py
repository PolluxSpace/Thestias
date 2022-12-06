from time import sleep

from SX127x.LoRa import *

from SX127x.board_config import BOARD


BOARD.setup()


class LoRaRcvCont(LoRa):

    def __init__(self, verbose=False):

        super(LoRaRcvCont, self).__init__(verbose)

        self.set_mode(MODE.SLEEP)

        self.set_dio_mapping([0] * 6)


    def start(self):

        self.reset_ptr_rx()

        self.set_mode(MODE.RXCONT)

        while True:

            sleep(.5)

            rssi_value = self.get_rssi_value()

            status = self.get_modem_status()

            sys.stdout.flush()

            


    def on_rx_done(self):

        print("\nReceived: ")

        self.clear_irq_flags(RxDone=1)

        payload = self.read_payload(nocheck=True)

        print(bytes(payload).decode("utf-8",'ignore'))

        self.set_mode(MODE.SLEEP)

        self.reset_ptr_rx()

        self.set_mode(MODE.RXCONT) 


lora = LoRaRcvCont(verbose=False)

lora.set_mode(MODE.STDBY)


#  Medium Range  Defaults after init are 434.0MHz, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on 13 dBm


lora.set_pa_config(pa_select=1)


try:

    lora.start()

except KeyboardInterrupt:

    sys.stdout.flush()

    print("")

    sys.stderr.write("KeyboardInterrupt\n")

finally:

    sys.stdout.flush()

    print("")

    lora.set_mode(MODE.SLEEP)

    BOARD.teardown()


 


Lora Server Code for Arduino:


//Arduino Raspberry Pi wireless Comunnication through LoRa - SX1278

//Send 0 to 9 from Arduino through Radio head LoRa without ACK

//Code for: www.circuitdigest.com

//Dated: 19-4-20198


#include <SPI.h> //Import SPI librarey 

#include <RH_RF95.h> // RF95 from RadioHead Librarey 


#define RFM95_CS 10 //CS if Lora connected to pin 10

#define RFM95_RST 9 //RST of Lora connected to pin 9

#define RFM95_INT 2 //INT of Lora connected to pin 2


// Change to 434.0 or other frequency, must match RX's freq!

#define RF95_FREQ 434.0


// Singleton instance of the radio driver

RH_RF95 rf95(RFM95_CS, RFM95_INT);


void setup() 

{

 

//Initialize Serial Monitor

  Serial.begin(9600);

  

// Reset LoRa Module 

  pinMode(RFM95_RST, OUTPUT); 

  digitalWrite(RFM95_RST, LOW);

  delay(10);

  digitalWrite(RFM95_RST, HIGH);

  delay(10);


//Initialize LoRa Module

  while (!rf95.init()) {

    Serial.println("LoRa radio init failed");

    while (1);

  }

  


 //Set the default frequency 434.0MHz

  if (!rf95.setFrequency(RF95_FREQ)) {

    Serial.println("setFrequency failed");

    while (1);

  }


  rf95.setTxPower(18); //Transmission power of the Lora Module

}


char value = 48;


void loop()

{

  Serial.print("Send: ");

  char radiopacket[1] = char(value)};

  rf95.send((uint8_t *)radiopacket, 1);


    

  delay(1000);

  value++;

  if (value > '9')

  value = 48;

}


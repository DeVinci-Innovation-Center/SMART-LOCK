//ARDUINO CODE TO READ A RFID CARD FROM RC522 AND DISPLAY IT ON A LCD SCREEN

#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal.h>

#define SS_PIN 10
#define RST_PIN 9
const int rs = 8, en = 7, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
MFRC522 rfid(SS_PIN, RST_PIN); 
byte nuidPICC[4];

void setup() 
{ 
  Serial.begin(9600);

  SPI.begin(); 

  rfid.PCD_Init();
  lcd.begin(16, 2);
  lcd.clear();
}
 
void loop() 
{
  if ( !rfid.PICC_IsNewCardPresent())
    return;

  if ( !rfid.PICC_ReadCardSerial())
    return;

  lcd.setCursor(1,0);
  lcd.print("UID (decimal) :");
  lcd.setCursor(0,1);
    
  for (byte i = 0; i < rfid.uid.size; i++) 
  {
      lcd.print(rfid.uid.uidByte[i], DEC);
      if(i!= 3)
        lcd.print(".");
  }

  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}

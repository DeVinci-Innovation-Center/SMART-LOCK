# SMART-LOCK #

Smart Lock project consists on securing DVIC lockers, that can be unlocked only by authorised students with their student cards.

The main goals of this project are :
* Securing DVIC lockers with a full-time working system,
* Permits a modularity and an easy reproducing,
* Being able to update the system in the future and to manage student access database in back-end programmation.


## Hardware Setup ##
### Materials required for one locker ###

* Raspberry Pi 3 Model B V1.2
* a 12V solenoid lock
* a RFID reader : RC522
* a relay PCS KY-019 5 V
* a 7 inch touchpad compatible with raspberry
* a 40 pins IDE cables
* A 12V Power Supply
* SBC converter
* Hall magnet captor
* A case to support the touchscreen pad and all the cable, case that can be 3D printed

### Cable Management ###

Here is a picture that illustrate the Cable Management of the entire system : 
<p align="center">
  <img src=https://github.com/DeVinci-Innovation-Center/SMART-LOCK/blob/main/Cable_Management.png?raw=true "Cable Management of Smart Lock System">
</p>
For a proper finishing stage and to prevent from unexpected disconection, it is important to use a 40 pins IDE Cable and pluging it into the raspberry pi. This imply to solder cables into pins headers to connect them in the other components (RC522 and relay).

### Raspberry Pi Power supply

We tried different ways and current intensities to supply the raspberry pi 3, and we conclude that a 5V and 3A supply is the best way to power supply the raspberry. A current of 2A or 2.1A is not enough to power sufficiently the raspberry in our system, because the raspberry supply also the touchpad. In this case, a "low voltage indicator" appear and the application is lower.

It is eventually possible to supply the raspberry via the GPIO, with pin 2 (5V) and pin 6 (GND), but it is less safely : in case of a wrong voltage input, the raspberry could fry!
That's why we preferred use a micro-USB cable to power supply the raspberry.

See : [https://thepihut.com/blogs/raspberry-pi-tutorials/how-do-i-power-my-raspberry-pi](https://thepihut.com/blogs/raspberry-pi-tutorials/how-do-i-power-my-raspberry-pi)

## Software ##
### Read RFID tags with RC522 ###

### Program an API to communicate with a database server ###
An Application Programming Interface (API) is a set of protocols that facilitate the communication between software applications. Here, our API will be added on the DVIC website in order to manage on back-end the management of the Database.
Then, on the main program, everytime that someone scan a RFID badge, an http request with the badge and locker number is made on the API Smart Lock of the DVIC website.
According to the badge authorization, the server answer the return code :
* 200 if the badge is authorised
* 401 if the badge is registered in the database but not authorised on the locker asked
* 404 if the badge is not register in the database

For example:
Here is the database of the registered students and their locker access:
Name  | Badge | Lockers
------------- | ------------- | -------------
Maxime  | 10001 | [1,2]
Louis  | 20002 | [1,3,4]

* Maxime scan his badge in the locker n°1 : the raspberry make the requests : **https://dvic.devinci.fr/smart-lock/10001/1**. The server responds 200 to the raspberry and the locker open.
* Louis scan his badge in the locker n°2 : the raspberry make the requests : **https://dvic.devinci.fr/smart-lock/20002/2**. The server responds 401 to the raspberry and the locker remain closed.

The use of an API permits to manage and update continuously the database authorisation of the locker. It permits also to centralise the database in one software : we could add as many lockers as we want and the protocol will remain the same.

See the code of the Smart Lock API : https://github.com/DeVinci-Innovation-Center/SMART-LOCK/blob/main/API_lockersV2.py

Learn more on API on :

* REST API CRASH COURSE [https://www.youtube.com/watch?v=qbLc5a9jdXo](https://www.youtube.com/watch?v=qbLc5a9jdXo)
* API Writing and deployment [https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/)

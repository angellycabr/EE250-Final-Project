# EE250-Final-Project
Repository for final project. We'll put the write up and block diagram here: https://docs.google.com/document/d/1HCgiDMdAx9rc6X-NpooIy4Esoci7v_edLMyU_T01l5w/edit?usp=sharing
Team members: Angelly Cabrera, Emu Eghre-Bello

Instructions:
To run this program please do the following
1. Connect volume sensor to A0 and LCD to IC2 on the GrovePi shield
2. Open a terminal to SSH in your raspberry pi, clone into the project repo " git clone ..... "
3. Open a new terminal for the VM, clone into the project repo " git clone ..... "
4. On the RPI run the program souundsensor.py and make some noise!
5. Then add and commit sound.pickle to the repository for the VM to access these changes!
6. On the VM terminal pull from the respository and create a Docker with the following lines:
- docker build -t ee250:genre .
- docker run ee250:genre --net=host
- curl -XGET "http://172.17.0.3:5000/classify?w=20" #BE SURE TO MODIFY THE IP ADDRESS BASED ON THE NEW SERVER ADDRESS
7. On the VM terminal run music.py, be sure to modify line 7 with the correct IP address
8. On the RPI run _______
9. Enjoy your new song reccomendation! 

Demo: 



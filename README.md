# Music Genre Classifier with Raspberry Pi & K-Means Clustering 🎵 — EE250-Final-Project
This project explores real-time music genre classification using **volume sensor input** on a Raspberry Pi and **k-means clustering** to generate personalized song recommendations. The system communicates between a Raspberry Pi and a Dockerized virtual machine, combining embedded systems, unsupervised learning, and distributed computing.

# 🛠 Instructions:
To run this program, please do the following
1. Run sounsensor.py on the Raspberry Pi
2. Add, commit, and push to update sound.pickle 
3. Pull inside the Virtual Machine
4. In the Virtual Machine, build docker: docker build -t ee250:genre .
5. In a new terminal inside the Virtual Machine, run docker: docker run ee250:genre --net=host
6. Update the link in request.py and save (this is because the IP address will be different when you build the docker server)
7. Run request.py in the Virtual Machine
8. Add, commit, and push to update 
9. Pull in the Raspberry Pi
10. Run final_api.py on the Raspberry Pi

# Demo and Write-up
Demo: https://drive.google.com/file/d/1GkxBUSIbuP31J0M08WUspBreWrEu-XnZ/view?usp=sharing
Write-up and block diagram here: https://docs.google.com/document/d/1q0ghPdBKwWVu_WVGTgk5B0wRTVcjCwbOeJS1zmdFUdE/edit?usp=sharing

Team members: Angelly Cabrera, Emu Eghre-Bello


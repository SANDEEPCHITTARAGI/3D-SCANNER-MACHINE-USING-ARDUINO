# 3D-SCANNER-MACHINE-USING-ARDUINO
# 3D Scanner Machine Using Arduino (IR sensor based)

This is a student project for making a simple 3D scanner using Arduino, two stepper motors and an IR sensor.  
It rotates the object on a turntable and moves the sensor sideways, measuring distance and saving data to an SD card.

---

## 📌 How it works
- The turntable stepper motor rotates the object step by step.
- At each step, the second stepper motor moves the IR sensor sideways to scan.
- Arduino reads the IR distance sensor at each position.
- Data (angle, sensor position, distance) is saved to the SD card in `scan.txt`.
- We can plot the data with a Python script.

---

## 🔧 Components used
- Arduino Uno
- 2 × stepper motors (28BYJ-48) with ULN2003 drivers
- IR distance sensor (e.g., Sharp GP2Y0A21YK)
- SD card module
- 12V battery
- Wires and simple frame

---

## 📂 Folder structure
3d-scanner-arduino-ir/
├── arduino/ # Arduino sketch
├── python/ # Python script to plot data
├── data/ # Example scan data
├── hardware/ # Fritzing diagram
└── README.md


---

## ⚙️ Software
- Arduino IDE
- Python 3 (`matplotlib`)
- Fritzing (to view wiring_diagram.fzz)
- MeshLab (to visualize 3D later)

---

## ✅ Next steps
- Calibrate sensor to cm
- Export data to point cloud (`.ply`)
- Add LCD/button control

---

## 📄 License
Open source (MIT license). Feel free to use or modify.

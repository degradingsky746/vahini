# Project Vahini - Self-Driving Autonomous Vehicle for Irrigation

## Overview

Project Vahini is an autonomous electric vehicle (EV) designed to irrigate large farms by carrying and dispensing 1-1.5 tons of water. It uses sensors, a Raspberry Pi processing unit, and machine learning to detect trees, measure soil conditions, and efficiently water crops. The vehicle can self-navigate, detect obstacles, and autonomously recharge, optimizing agricultural irrigation with minimal human intervention.

## Features

- **Autonomous Navigation**: Self-driving through farms using a pre-programmed map.
- **Obstacle Detection & Avoidance**: Ultrasonic sensors detect and avoid obstacles in real-time.
- **Object Detection**: Uses an enhanced YOLO (xYOLO) model to identify trees and humans.
- **Soil Condition Analysis**: Measures soil moisture to deliver the precise amount of water.
- **Remote Control**: Flask-based web interface for manual control and monitoring.
- **Battery Management**: Monitors battery status and autonomously returns to the docking station when needed.

## System Architecture

- **Processing Unit**: Raspberry Pi 3.0
- **Sensors**:
    - Ultrasonic sensors (for obstacle detection)
    - Pi Camera (for object detection)
- **Motors**:
    - L298 Dual H-Bridge Motor Driver
    - BH86 Stepper Motor
    - Brushless DC Motor (BLDC) with Kelly Controller
- **Power Supply**: 48V 30Ah Lithium-Ion Battery

## Objectives

1. Program the EV dynamically with a tree map for accurate navigation.
2. Ensure the EV carries 1-1.5 tons of water from a loading point.
3. Detect trees, analyze soil moisture, and dispense the right amount of water.
4. Implement obstacle detection and collision avoidance.
5. Monitor battery status and return to the charging station when low.

## Installation & Usage

### 1. Clone the Repository

```
git clone https://github.com/yourusername/project-vahini.git
cd project-vahini
```
## 2. Run the Application

```
python app.py
```
## 3. Access the Web Interface
Open your browser and visit:

```
http://<raspberry-pi-ip>:5000
```
## Web Interface Controls

- **Forward/Reverse**: Control the vehicle's movement.  
- **Left/Right**: Adjust the vehicle's steering.  
- **Stop**: Halt vehicle movement immediately.  
- **Speed Control**: Adjust the vehicle's speed.  
- **Live Feed**: View a real-time video stream from the Pi Camera.  

## Circuit Design

The EV uses **Pulse Width Modulation (PWM)** for motor control. Key hardware includes:

- **L298 Dual H-Bridge Motor Driver**: Controls movement direction.  
- **BH86 Stepper Motor**: Enables precision steering.  
- **BLDC Motor**: Controls speed and movement.  

## System Block Diagram
+-------------------+
| Raspberry Pi 3.0  |
+-------------------+
      |     |     |
      |     |     +--> Ultrasonic Sensors (Obstacle Detection)
      |     +--------> Pi Camera (Object Detection)
      +-------------> Motor Driver (PWM Control)

## Object Detection

Object detection is performed using the **xYOLO** model, trained on:

- **Trees** (for irrigation targeting)  
- **Humans** (for obstacle detection)  

The model is optimized for the **Raspberry Pi** to ensure real-time performance.

## Project Roadmap

1. **Prototype Development** (Completed)  
2. **Obstacle Detection & Avoidance** (Completed)  
3. **Object Detection Integration** (Completed)  
4. **BLDC Motor Control** (Completed)  
5. **Battery Monitoring & Docking** (In Progress)  

## Key Algorithms

- **A* Search Algorithm**: Optimizes vehicle navigation using mapped terrain.  
- **xYOLO Object Detection**: Identifies trees and humans in real-time.  

## Future Improvements

- **Enhanced Navigation**: Improve path optimization using SLAM (Simultaneous Localization and Mapping).  
- **Battery Efficiency**: Optimize power consumption during extended operations.  
- **Expanded Object Detection**: Train the model to recognize additional farm-related objects.  

## References

1. **xYOLO**: A Model For Real-Time Object Detection On Low-End Hardware  
2. [A* Search Algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)  

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

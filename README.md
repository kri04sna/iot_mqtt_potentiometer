### MicroPython IoT Weather Station with Potentiometer

#### Project Overview
The MicroPython IoT Weather Station project is designed to collect sensor data and transmit it wirelessly to a remote server using MQTT (Message Queuing Telemetry Transport). Originally intended to monitor temperature and humidity using a DHT22 sensor, the project has been modified to utilize a potentiometer and keypad for input instead. This makes it a versatile example of integrating different types of sensors and controls into an IoT system.

#### Components and Configuration
- **Microcontroller**: ESP32, a powerful microcontroller with built-in Wi-Fi capabilities, is used to handle sensor data collection, processing, and communication with the MQTT broker.
- **Potentiometer**: The potentiometer, a variable resistor, is used to simulate sensor data. It is connected to an ADC (Analog-to-Digital Converter) pin on the ESP32, allowing it to read varying voltage levels, which correspond to different resistance levels. This setup effectively simulates varying environmental conditions or user inputs.
- **Keypad**: A 4x4 matrix keypad is employed to send specific input values, simulating discrete data points or control commands. This is connected to the ESP32 through a set of GPIO pins.
- **MQTT Protocol**: MQTT is a lightweight messaging protocol used for small sensors and mobile devices. It efficiently handles data transmission in environments with low bandwidth or limited resources. The project uses an MQTT broker, `broker.mqttdashboard.com`, to facilitate the communication of data between the ESP32 and a monitoring client.

#### System Functionality
1. **Wi-Fi Connection**: The ESP32 connects to a Wi-Fi network (SSID: Wokwi-GUEST) to enable internet connectivity, which is essential for communicating with the MQTT broker.
2. **Data Acquisition**:
   - The **potentiometer** continuously outputs an analog signal based on its position, representing simulated sensor data. This analog signal is converted to a digital value (ranging from 0 to 4095) using the ADC pin.
   - The **keypad** allows for specific, user-controlled inputs to be read and processed by the microcontroller.
3. **MQTT Communication**: The ESP32 publishes the sensor data (potentiometer value) and keypad inputs to specific MQTT topics (`wokwi-potentiometer` and `wokwi-keypad`) on the MQTT broker. This data can be subscribed to and viewed using a client like HiveMQ's WebSocket client.
4. **Real-Time Monitoring**: Users can monitor the potentiometer values and keypad inputs in real time via the MQTT client, providing immediate feedback and interaction with the system.

#### Applications and Use Cases
This project demonstrates how IoT systems can be designed for a wide range of applications, including:
- **Environmental Monitoring**: By substituting the potentiometer with actual environmental sensors (like temperature, humidity, or light sensors), the system can monitor real-world conditions and transmit data for analysis.
- **Remote Control Systems**: The use of a keypad allows for the development of remote control systems, where specific inputs trigger predefined actions or settings.
- **Educational Purposes**: This project serves as an excellent learning tool for students and hobbyists interested in IoT, MicroPython programming, and sensor integration.

#### Conclusion
The MicroPython IoT Weather Station project, modified with a potentiometer and keypad, is a flexible and powerful example of integrating IoT technology with sensor inputs. It showcases the capabilities of the ESP32 in handling real-time data collection and communication, making it suitable for various practical and educational applications.
![Uploading image.png…]()

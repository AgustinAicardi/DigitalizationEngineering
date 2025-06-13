# OPC UA Server with Asset Administration Shell (AAS) Integration

This project demonstrates the implementation of an OPC UA server that loads and exposes an Asset Administration Shell (AAS) model using the asyncua library. The server periodically updates property values, exposes a remote operation, and supports multiple monitoring clients.

<!--
## Project Structure:


├── AAS_rack.xml -> XML version of the AAS model (imported by the server)  
├── server.py -> Main OPC UA server with property updates and operation  
├── monitor_client.py -> Basic client that prints property values  
├── monitor_client_rich.py -> Same client with enhanced terminal UI using "rich"  
├── method_client.py -> Client that invokes the server-side operation  
├── aas_files/ -> Optional folder containing full AAS (.aasx, .json)  
│ ├── your_model.json  
│ └── your_model.aasx  
-->

## Features:

- Load and expose an AAS model from XML

- Periodically update property values

- Provide a custom method that divides an input value by a server-side property

- Validate user input and handle edge cases

- Support multiple clients simultaneously

- Display live data with a terminal UI using the "rich" library
<!--
## Requirements:

- Install dependencies using pip: `pip install asyncua rich`

Tested with Python 3.9+

## How to Run:

- Start the server:
`python server.py`

- Start a simple monitoring client:
`python monitor_client.py`

- Or run the rich UI monitoring client:
`python monitor_client_rich.py`

- Use the method invocation client:
`python method_client.py`

You will be prompted to enter a number, which is divided by the "AvailableSurface" property on the server. If the input exceeds the limit, an error message will appear and you can try again.
-->
## AAS Integration:

The AAS model is defined in AAS_rack.xml and imported automatically by the server.

Full AAS representations (.json, .aasx) are included in the AAS.

The model is based on the principles of Industry 4.0 and RAMI 4.0.

Notes:

The server starts even if there are broken references or missing parent nodes in the XML.


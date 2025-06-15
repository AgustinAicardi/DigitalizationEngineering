# OPC UA Server with Asset Administration Shell (AAS) Integration

This project demonstrates the implementation of an OPC UA server that loads and exposes an Asset Administration Shell (AAS) model using the asyncua library. The server periodically updates property values, exposes a remote operation, and supports multiple monitoring clients. The Asset Administration Shell (AAS) was created using the AAS Package Explorer.  


## Project Structure:

**AAS** : Contains the main AAS files and the individual submodels.  
├── Submodels: Folder with all the submodels exported in json format.  
├── `AAS_Digitalization.aasx`: Asset Administration Shell exported in AASX format.  
└── `AAS_Digitalization.xml`: XML representation of the AAS.

**ServerOPCUA** : OPC UA server and client implementations for interacting with the digitalized rack.  
├── `AAS_rack.xml`: XML nodeset file used by the OPC UA server.  
├── `server.py`: OPC UA server implementation.  
├── `clientOperation.py`: Client to execute the server’s remote operation.  
├── `clientValues.py`: Client to monitor and read property values from the server.  
├── `clientValuesDisplay.py`: Additional client for displaying monitored values.  
└── `serverCheck.py`: Utility client or script for server verification.


## Features:

- Load and expose an AAS model from XML

- Periodically update property values

- Provide a custom method that divides an input value by a server-side property

- Validate user input and handle edge cases

- Support multiple clients simultaneously

- Display live data with a terminal UI using the "rich" library


## How to Run

1. **Requirements**  
   - Python 3.7 or higher  
   - Install required libraries with:  
     ```bash
     pip install asyncua asyncio
     ```

2. **Prepare Files**  
   - Make sure the XML file to be used by the server (`AAS_rack.xml` or the desired nodeset) is in the same folder as the server script (`server.py`).
   - The XML was exported from the OPC UA Nodeset2.xml option of version 3.0 of the corresponding software, dated 10.06.2024.

  > **Note on XML modification:**  
  > The XML file exported from the AASX package required manual adjustments before being usable in the OPC UA server. Specifically, the "AssetAdminShell" UAObject element, originally located near the end of the XML file, was cut and moved to the beginning of the document to ensure correct object hierarchy.  
  > Additionally, the following reference line was added to maintain proper backward referencing and organize the nodes correctly:  
  > ```xml
  > <Reference ReferenceType="Organizes" IsForward="false">i=85</Reference>
  > ```  
  > These changes were necessary to enable the server to correctly load and navigate the AAS model.


3. **Run the Server**  
   - Execute the OPC UA server:  
     ```bash
     python server.py
     ```  
   - The server will start and expose the AAS model.

4. **Run the Clients**  
   - Open a new terminal window for each client you want to run.  
   - To monitor values:  
     ```bash
     python clientValuesDisplay.py
     ```  
   - To execute the remote operation:  
     ```bash
     python clientOperation.py
     ```  

The clients connect to the server at `opc.tcp://localhost:4840/` by default.


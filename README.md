# DigitalizationEngineering
# OPC UA Server with Asset Administration Shell (AAS) Integration

This project demonstrates the implementation of an **OPC UA server** that loads and exposes an **Asset Administration Shell (AAS)** model using the `asyncua` library. The server periodically updates property values, exposes a remote operation, and supports multiple monitoring clients.

---

## 📂 Project Structure
├── AAS_rack.xml # XML version of the AAS model (imported by the server)
├── server.py # Main OPC UA server with property updates and operation
├── monitor_client.py # Basic client that prints property values
├── monitor_client_rich.py # Same client with enhanced terminal UI using rich
├── method_client.py # Client that invokes the server-side operation
├── aas_files/ # Optional folder containing full AAS (.aasx, .json)
│ ├── your_model.json
│ └── your_model.aasx

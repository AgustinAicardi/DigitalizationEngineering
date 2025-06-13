# This script starts an OPC UA server using the `asyncua` library.
# It loads an AAS model from an XML file and remains active to accept client connections.
# The server starts even if there are missing parent nodes or incorrect references in the XML.

import logging
import asyncio
import sys
#sys.path.insert(0, "..")  # Only necessary if your folder structure requires it

from asyncua import Server

async def main():
    _logger = logging.getLogger('asyncua')
    
    server = Server()
    await server.init()

    # Change this to your actual IP address or leave as 'localhost' for local testing
    directory = 'opc.tcp://localhost:4840/'  # Default OPC UA port
    server.set_endpoint(directory)

    # Make sure the XML file is in the same folder as this script
    await server.import_xml("AAS_rack.xml")  # Your AAS model

    print("OPC UA server started at {}".format(directory))
    print("AAS model successfully imported")
    print("Waiting for client connections...")

    async with server:
        while True:
            await asyncio.sleep(1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

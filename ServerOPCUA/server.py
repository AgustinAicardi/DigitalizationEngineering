# This script starts an OPC UA server using the `asyncua` library, imports an AAS model from XML,
# periodically updates selected properties (e.g. product count, temperature, surface),
# and exposes a custom method to perform a calculation based on one of the properties.

import logging
import asyncio
import random
from asyncua import ua, uamethod, Server

SERVER = None

@uamethod
async def divide_input_by_property3(parent, input_a: float) -> float:
    denom_node = SERVER.get_node("ns=2;i=313")
    denom = await denom_node.read_value()
    if denom == 0:
        return 0
    return round(input_a * 100 / denom, 2)

async def main():
    global SERVER

    # logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("asyncua")

    server = Server()
    await server.init()
    SERVER = server

    directory = "opc.tcp://localhost:4840/"
    server.set_endpoint(directory)

    await server.import_xml("AAS_rack.xml")

    print("--------------------------------------------------")
    print("OPC UA server running at {}".format(directory))
    print("AAS model successfully imported")
    print("Waiting for client connections...")

    # Get property nodes
    property1 = server.get_node("ns=2;i=329")  # Number of products
    property2 = server.get_node("ns=2;i=369")  # Temperature from reference
    property3 = server.get_node("ns=2;i=313")  # SurfaceAvailable from reference
    property4 = server.get_node("ns=2;i=384")  # Usage time

    # Make properties writable
    await property1.set_writable()
    await property2.set_writable()
    await property3.set_writable()
    await property4.set_writable()

    # Set initial value for denominator
    available_surface = 5.0
    await property3.write_value(ua.Variant(available_surface, ua.VariantType.Double))

    # Link operation method
    operation_node = server.get_node("ns=2;i=361")
    server.link_method(operation_node, divide_input_by_property3)

    current_value_p1 = 0
    current_value_p4 = 0

    async with server:
        while True:
            # Increment and reset property1 (0 to 100)
            current_value_p1 = (current_value_p1 + 2) % 101
            # Increment and reset property4 (0 to 50)
            current_value_p4 = (current_value_p4 + 1) % 51

            random_value = round(random.uniform(20.0, 80.0), 2)

            await property1.write_value(ua.Variant(current_value_p1, ua.VariantType.Int32))
            await property4.write_value(ua.Variant(current_value_p4, ua.VariantType.Double))
            await property2.write_value(ua.Variant(random_value, ua.VariantType.Double))

            print(f"[Server Updated] Number of Products: {current_value_p1}, Temperature: {random_value}, "
                  f"Available Surface: {available_surface}, Usage Time: {current_value_p4}")
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())

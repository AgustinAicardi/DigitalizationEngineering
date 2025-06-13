# This script connects as a client to an OPC UA server and continuously monitors
# selected property values (product count, temperature, available surface, usage time),
# printing updated values every 2 seconds.

import asyncio
from asyncua import Client

async def monitor_properties():
    url = "opc.tcp://localhost:4840/"
    async with Client(url=url) as client:
        print("Monitor connected to OPC UA server")

        node_product_count = client.get_node("ns=2;i=329")  # Number of products
        node_temperature = client.get_node("ns=2;i=369")    # Temperature
        node_surface = client.get_node("ns=2;i=313")        # Available surface
        node_usage_time = client.get_node("ns=2;i=384")     # Usage time

        while True:
            product_count = await node_product_count.read_value()
            temperature = await node_temperature.read_value()
            surface = await node_surface.read_value()
            usage_time = await node_usage_time.read_value()

            print(f"[Monitor] Products: {product_count}, Temperature: {temperature} °C, "
                  f"Available Surface: {surface}, Usage Time: {usage_time}")
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(monitor_properties())

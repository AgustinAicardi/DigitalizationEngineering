# This script connects as a client to an OPC UA server and allows the user to input a value.
# It then remotely invokes a method on the server that calculates the percentage of this value 
# with respect to a denominator read from the server's data model. If the input is out of range, 
# the user is asked to re-enter it.

import asyncio
from asyncua import Client

async def main():
    url = "opc.tcp://localhost:4840/"
    method_node_id = "ns=2;i=361"
    denom_node_id = "ns=2;i=313"

    async with Client(url) as client:
        print("Connected to OPC UA server")

        method_node = client.get_node(method_node_id)
        parent_node = await method_node.get_parent()
        denom_node = client.get_node(denom_node_id)

        while True:
            try:
                # Read current denominator value
                denom_value = await denom_node.read_value()

                input_str = input(f"Enter input value (0 - {denom_value}) or 'exit' to quit: ")
                if input_str.lower() == "exit":
                    break

                input_value = float(input_str)

                # Validate input range
                if not (0 <= input_value <= denom_value):
                    print(f"Error: value must be between 0 and {denom_value}")
                    continue

                # Call the remote method
                result = await parent_node.call_method(method_node, input_value)

                print(f"Operation result: {result}%")

            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print(f"Error calling method: {e}")

if __name__ == "__main__":
    asyncio.run(main())

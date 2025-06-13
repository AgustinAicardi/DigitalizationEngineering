# This script acts as an OPC UA client to monitor key properties of a rack system
# (product count, temperature, available surface, usage time) in real time.
# It uses the `rich` library to provide a dynamic and visually appealing console interface.

import asyncio
from asyncua import Client
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel

console = Console()

async def monitor_properties():
    url = "opc.tcp://localhost:4840/"
    async with Client(url=url) as client:
        console.print("[green]Monitor connected to OPC UA server[/green]")

        node_product_count = client.get_node("ns=2;i=329")
        node_temperature = client.get_node("ns=2;i=369")
        node_surface = client.get_node("ns=2;i=313")
        node_usage_time = client.get_node("ns=2;i=384")

        with Live(refresh_per_second=0.5) as live:
            while True:
                product_count = await node_product_count.read_value()
                temperature = await node_temperature.read_value()
                surface = await node_surface.read_value()
                usage_time = await node_usage_time.read_value()

                table = Table(title="OPC UA Rack Monitor", expand=True)
                table.add_column("Parameter", justify="left")
                table.add_column("Value", justify="right")

                table.add_row("Products", str(product_count))
                table.add_row("Temperature (°C)", f"{temperature}")
                table.add_row("Available Surface (m²)", f"{surface}")
                table.add_row("Usage Time (d)", f"{usage_time}")

                live.update(Panel(table))

                await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(monitor_properties())

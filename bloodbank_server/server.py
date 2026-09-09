import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastmcp import FastMCP

from services.inventory_service import (
    get_inventory,
    update_inventory,
    check_availability
)

mcp = FastMCP("Blood Inventory Server")


@mcp.tool()
def view_inventory():
    """
    View all blood inventory.
    """
    return get_inventory()


@mcp.tool()
def update_blood_inventory(blood_group: str, units: int):
    """
    Update blood units.
    """
    update_inventory(blood_group, units)
    return "Inventory updated successfully."


@mcp.tool()
def blood_availability(blood_group: str):
    """
    Check available units for a blood group.
    """
    units = check_availability(blood_group)
    return {
        "blood_group": blood_group,
        "available_units": units
    }


if __name__ == "__main__":
    mcp.run()
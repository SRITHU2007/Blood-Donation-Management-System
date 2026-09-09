import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastmcp import FastMCP

# ---------------- Donor ----------------

from services.donor_service import (
    add_donor,
    get_all_donors,
    get_matching_donors,
    search_donors,
    update_donor,
    delete_donor,
    get_donor_by_id,
)

# ---------------- Blood Inventory ----------------

from services.inventory_service import (
    get_inventory,
    update_inventory,
    check_availability,
)

# ---------------- Hospital ----------------

from services.hospital_service import (
    add_hospital,
    get_all_hospitals,
    search_hospitals,
    update_hospital,
    delete_hospital,
    get_hospital_by_id,
)

mcp = FastMCP("Blood Donation MCP Server")

# ==========================================================
# DONOR TOOLS
# ==========================================================

@mcp.tool()
def register_donor_tool(
    name,
    age,
    gender,
    blood_group,
    phone,
    email,
    location,
    last_donation,
):
    add_donor(
        name,
        age,
        gender,
        blood_group,
        phone,
        email,
        location,
        last_donation,
    )
    return "Donor registered successfully."


@mcp.tool()
def view_donors():
    return get_all_donors()


@mcp.tool()
def search_donor(blood_group="", location=""):
    return search_donors(blood_group, location)


@mcp.tool()
def donor_details(donor_id):
    return get_donor_by_id(donor_id)


@mcp.tool()
def edit_donor(
    donor_id,
    name,
    age,
    gender,
    blood_group,
    phone,
    email,
    location,
):
    update_donor(
        donor_id,
        name,
        age,
        gender,
        blood_group,
        phone,
        email,
        location,
    )
    return "Donor updated successfully."


@mcp.tool()
def remove_donor(donor_id):
    delete_donor(donor_id)
    return "Donor deleted successfully."


@mcp.tool()
def matching_donors(blood_group):
    return get_matching_donors(blood_group)


# ==========================================================
# BLOOD INVENTORY TOOLS
# ==========================================================

@mcp.tool()
def view_inventory():
    return get_inventory()


@mcp.tool()
def update_blood_inventory(blood_group, units):
    update_inventory(blood_group, units)
    return "Inventory updated successfully."


@mcp.tool()
def blood_availability(blood_group):
    return check_availability(blood_group)


# ==========================================================
# HOSPITAL TOOLS
# ==========================================================

@mcp.tool()
def add_hospital_tool(name, location, phone):
    add_hospital(name, location, phone)
    return "Hospital added successfully."


@mcp.tool()
def view_hospitals():
    return get_all_hospitals()


@mcp.tool()
def search_hospital(location=""):
    return search_hospitals(location)


@mcp.tool()
def hospital_details(hospital_id):
    return get_hospital_by_id(hospital_id)


@mcp.tool()
def edit_hospital(hospital_id, name, location, phone):
    update_hospital(
        hospital_id,
        name,
        location,
        phone,
    )
    return "Hospital updated successfully."


@mcp.tool()
def remove_hospital(hospital_id):
    delete_hospital(hospital_id)
    return "Hospital deleted successfully."


# ==========================================================

if __name__ == "__main__":
    mcp.run()
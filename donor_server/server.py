import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from fastmcp import FastMCP

# ---------------- DONOR ----------------

from services.donor_service import (
    add_donor,
    get_all_donors,
    search_donors,
    update_donor,
    delete_donor,
    get_donor_by_id
)

# ---------------- INVENTORY ----------------

from services.inventory_service import (
    get_inventory,
    update_inventory,
    check_availability
)

# ---------------- HOSPITAL ----------------

from services.hospital_service import (
    add_hospital,
    get_all_hospitals,
    search_hospitals,
    update_hospital,
    delete_hospital,
    get_hospital_by_id
)

# ---------------- MCP ----------------

mcp = FastMCP("Blood Donation MCP Server")

# =====================================================
# DONOR TOOLS
# =====================================================

@mcp.tool()
def register_donor(
    name,
    age,
    gender,
    blood_group,
    phone,
    email,
    location,
    last_donation
):
    add_donor(
        name,
        age,
        gender,
        blood_group,
        phone,
        email,
        location,
        last_donation
    )

    return "Donor Registered Successfully"


@mcp.tool()
def view_donors():
    return get_all_donors()


@mcp.tool()
def search_donor(
    blood_group="",
    location=""
):
    return search_donors(
        blood_group,
        location
    )


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
    location
):
    update_donor(
        donor_id,
        name,
        age,
        gender,
        blood_group,
        phone,
        email,
        location
    )

    return "Donor Updated Successfully"


@mcp.tool()
def remove_donor(donor_id):
    delete_donor(donor_id)

    return "Donor Deleted Successfully"


# =====================================================
# INVENTORY TOOLS
# =====================================================

@mcp.tool()
def view_inventory():
    return get_inventory()


@mcp.tool()
def update_blood_inventory(
    blood_group,
    units
):
    update_inventory(
        blood_group,
        units
    )

    return "Inventory Updated Successfully"


@mcp.tool()
def blood_availability(
    blood_group
):
    return check_availability(
        blood_group
    )


@mcp.tool()
def process_request(
    blood_group,
    required_units
):
    available_units = check_availability(
        blood_group
    )

    return {
        "available": available_units >= required_units,
        "units": available_units
    }


# =====================================================
# HOSPITAL TOOLS
# =====================================================

@mcp.tool()
def add_hospital_tool(
    name,
    location,
    phone
):
    add_hospital(
        name,
        location,
        phone
    )

    return "Hospital Added Successfully"


@mcp.tool()
def view_hospitals():
    return get_all_hospitals()


@mcp.tool()
def search_hospital(
    location
):
    return search_hospitals(
        location
    )


@mcp.tool()
def hospital_details(
    hospital_id
):
    return get_hospital_by_id(
        hospital_id
    )


@mcp.tool()
def edit_hospital(
    hospital_id,
    name,
    location,
    phone
):
    update_hospital(
        hospital_id,
        name,
        location,
        phone
    )

    return "Hospital Updated Successfully"


@mcp.tool()
def remove_hospital(
    hospital_id
):
    delete_hospital(
        hospital_id
    )

    return "Hospital Deleted Successfully"


# =====================================================
# RUN SERVER
# =====================================================

if __name__ == "__main__":
    print("Blood Donation MCP Server Started...")
    mcp.run()
from services.inventory_service import check_availability


def process_request(blood_group, required_units):

    available = check_availability(blood_group)

    if available >= required_units:
        return True, available

    return False, available
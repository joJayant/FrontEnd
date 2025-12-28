import json
from datetime import datetime

# IMPLEMENT: Convert ISO timestamp to milliseconds
def iso_to_milliseconds(iso_time):
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

# IMPLEMENT: Normalize both data formats into target format
def normalize_data(data):
    result = {
        "deviceId": data["deviceId"],
        "timestamp": None,
        "telemetry": data["telemetry"]
    }

    # Case 1: timestamp already in milliseconds
    if isinstance(data["timestamp"], int):
        result["timestamp"] = data["timestamp"]

    # Case 2: timestamp in ISO format
    else:
        result["timestamp"] = iso_to_milliseconds(data["timestamp"])

    return result


def main():
    with open("data-1.json") as f:
        data1 = json.load(f)

    with open("data-2.json") as f:
        data2 = json.load(f)

    output1 = normalize_data(data1)
    output2 = normalize_data(data2)

    with open("data-result.json", "w") as f:
        json.dump([output1, output2], f, indent=2)


if __name__ == "__main__":
    main()

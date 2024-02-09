import jsonschema
import json
import sys
from pathlib import Path
# from req import connect_socket
# from convert import *

# Response data recieved from the meter

# Response for list
# response_data = "0001 0001 0030 004C C4 03 C1 08 00 09 06 0000600100FF 00 09 06 01000C0700FF 00 090601000B0700FF0009060100000200FF0009060000010000FF0009060000600200FF0009060100000804FF00090600005E5B00FF".replace(
#     " ", ""
# )
# Response for normal
# response_data = (
# "0001 0001 0010 0012 C4 01 C1 00 09 0C 0700000000000000008000FF".replace(" ", "")
# # "0001000100300016C403C1020009060100000200FF0009060000010000FF"
# )
# # Response for block
response_data = "0001 0001 0030 00D3 C4 02 C1 00 00000001 00 C9 02 00 09 0C 0700000000000000008000FF 00 01 16 020412000809060000010000FF0F0212000002041200 03090601000C0700FF0F021200000204120003090601000B0700FF0F021200000204120003090601005B0700FF0F021200000204120003090601000D0700FF0F021200000204120003090601000E0700FF0F02120000020412000309060100090700FF0F02120000020412000309060100010700FF0F02120000020412000309060100010800FF0F02120000020412000309060100090800FF0F021200000204".replace(
" ", ""
)

# Response schema path

file_path_response_schema = Path("./new_response_schema.json")

# file_path_schema = "schema.json"

# Reading schema json file


def read_json_file(file_path: str) -> dict:
    """
    Reads a JSON file and returns its content.

    Parameters:
    - file_path (str): The path to the JSON file.

    Returns:
    - dict: The content of the JSON file.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    - ValueError: If there is an error decoding the JSON in the file.
    - Exception: For any other unexpected errors.
    """
    try:
        # Open the file in read mode
        with open(file_path, "r") as file:
            # Load the JSON data from the file
            data = json.load(file)
        return data

    except FileNotFoundError:
        # Raise a specific error for file not found
        raise FileNotFoundError(f"File not found: {file_path}")

    except json.JSONDecodeError as e:
        # Raise a specific error for JSON decoding issues
        raise ValueError(f"Error decoding JSON in file {file_path}: {e}")

    except Exception as e:
        # Raise a generic exception with details for other errors
        raise Exception(
            {f"Error reading file {file_path}": e, "func": "read_json_file"}
        )


# Checking whether data successfully recieved or not


def data_success_or_not(data_result: str):
    """
    Check if the data result indicates success.

    Args:
        data_result (str): The result code to be checked.

    Returns:
        bool: True if the data result is "00," indicating success.

    Raises:
        TypeError: If `data_result` is not a string.
        ValueError: If `data_result` is not equal to "00," indicating an unsuccessful result.

    """
    try:
        # Check if data_result is a string
        if not isinstance(data_result, str):
            raise TypeError("data_result must be a string")

        # Check if data result is "00" indicating success
        if data_result == "00":
            return True
        else:
            raise ValueError(f"[Data is not received successfully] {data_result}")

    except Exception as e:
        # Print any other exceptions that might occur
        print(f"[ERROR in data_success_or_not]: {e}")


# Checking whether recieved block is last or there are some remaining


def last_block_result(last_block_or_not: str) -> bool:
    """
    Determine if the input represents the last block.

    Parameters:
    - last_block_or_not (str): A string indicating whether it's the last block or not. It should have a length of 2.

    Returns:
    - bool: True if it's not the last block (last_block_or_not != "00"), False otherwise.

    Raises:
    - ValueError: If last_block_or_not is not a string or doesn't have a length of 2.
    - Exception: If an unexpected error occurs during the process.

    Example:
    >>> last_block_result("01")
    True
    >>> last_block_result("00")
    False
    """
    # Check if last_block_or_not is a string
    if not isinstance(last_block_or_not, str):
        raise ValueError("last_block_or_not must be a string")

    # Check if the input string has a length of 2
    if len(last_block_or_not) != 2:
        raise ValueError("Input string must have a length of 2")

    try:
        # Return True if it's not the last block
        return last_block_or_not != "00"
    except Exception as e:
        # Raise an exception if an unexpected error occurs
        raise Exception(f"Error in last_block_result: {e}")


# Response data contains length or not:


def unexpected_length(data_result: str, data_type: str):
    """
    Calculate unexpected length based on data_result and data_type.

    Args:
        data_result (str): The data result to analyze.
        data_type (str): The data type to match against.
        file_path_response_schema (str): The file path to the JSON schema.

    Returns:
        int: The unexpected length based on the matched data type.

    Raises:
        ValueError: If the data type is not found in the JSON schema.
        FileNotFoundError: If the JSON schema file is not found.
        ValueError: If there's an error decoding JSON in the schema file.
        Exception: For other unexpected errors during execution.
    """
    try:
        # Check input conditions before proceeding
        if (
            data_success_or_not(data_result=data_result)
            and isinstance(data_result, str)
            and isinstance(data_type, str)
            and len(data_result) == 2
            and len(data_type) == 2
        ):
            # Load data_types from the JSON schema
            data_types = read_json_file(file_path_response_schema)["data_types"]

            # Iterate over data_types to find a match
            for item in data_types:
                if data_type in item["value"]:
                    # Return data_length, handling the case where it might be 0
                    return int(item["data_length"])

            # Raise an exception if data_type is not found
            raise ValueError(f"[Data type not found] {data_type}")
        else:
            raise ValueError(
                "[Invalid input] Check data_result and data_type lengths or type"
            )
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path_response_schema}") from e
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Error decoding JSON in file {file_path_response_schema}: {e}"
        ) from e
    except Exception as e:
        # Log the error and raise a more informative exception
        print({"[ERROR]": e, "func": "unexpected_length"})
        raise Exception(f"Error in unexpected_length: {e}") from e


# Output of json object created by response in terminal


def print_response_json(response_json: dict):
    """
    Print the key-value pairs of a dictionary.

    Args:
        response_json (dict): A dictionary to print.

    Raises:
        ValueError: If the input is not a dictionary.

    Example:
        >>> response = {'status': 'success', 'data': {'name': 'John', 'age': 30}}
        >>> print_response_json(response)
        status: success
        data: {'name': 'John', 'age': 30}
    """
    # Check if the input is a dictionary
    if not isinstance(response_json, dict):
        raise ValueError("response_json must be a dictionary")

    try:
        # Print key-value pairs
        for key, value in response_json.items():
            print(f"{key}: {value}")
    except Exception as e:
        # Handle and print any exceptions
        print({"[ERROR]": e, "func": "print_response_json"})


# Checking whether the wrapper port, source address, destination address matches with the schema


def check_address(var: str, name: str):
    """
    Check if a given variable matches any value in the list of addresses
    associated with a specific name in a JSON response schema.

    Args:
        var (str): The variable to be checked.
        name (str): The name associated with the list of addresses in the JSON schema.
        file_path_response_schema (str): The file path to the JSON response schema.

    Returns:
        bool: True if the variable matches any address value, False otherwise.

    Raises:
        ValueError: If var or name is not a string.
        FileNotFoundError: If the specified JSON file is not found.
        JSONDecodeError: If there is an error decoding the JSON file.
    """
    try:
        # Check if var and name are strings
        if not (isinstance(var, str) and isinstance(name, str)):
            raise ValueError("var and name must be strings")

        # Read the JSON file
        response_schema = read_json_file(file_path_response_schema)

        # Get the list of addresses for the given name from the response schema
        addresses = response_schema.get("address", {}).get(name, [])

        # Check if var matches any address value
        return any(var == address.get("value") for address in addresses)

    # Handle file not found error
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Error: File not found - {file_path_response_schema}"
        ) from e

    # Handle JSON decoding error
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Error decoding JSON in file {file_path_response_schema}: {e}"
        ) from e

    # Handle other exceptions
    except Exception as e:
        print({f"[{name} is invalid]": var, "[ERROR]": e, "func": "check_address"})
        return False


# Checking whether the response methode, response type, priority matches with the schema


def check_value(var: str, name: str):
    """
    Check if a specific value exists in a JSON file under the given name.

    Args:
        var (str): The value to check.
        name (str): The name corresponding to the section in the JSON file.
        file_path_response_schema (str): The path to the JSON file.

    Returns:
        bool: True if the value is found, False otherwise.

    Raises:
        ValueError: If var or name is not a string.
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If there is an error decoding the JSON file.
    """
    try:
        # Check if var and name are strings
        if not (isinstance(var, str) and isinstance(name, str)):
            raise ValueError("var and name must be strings")

        # Read the JSON file and get the values under the specified name
        values = read_json_file(file_path=file_path_response_schema).get(name, [])

        # Check if the desired value exists in the list
        return any(var == value.get("value") for value in values)

    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Error: File not found - {file_path_response_schema}"
        ) from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Error decoding JSON in file {file_path_response_schema}: {e}"
        ) from e
    except Exception as e:
        # Print an error message if an unexpected exception occurs
        print({f"[{name} is invalid]": var, "[ERROR]": e, "func": "check_value"})
        return False


# Checking the initial header of response data


def validate_response(response_data: str):
    """
    Validates the response data against a JSON schema.

    Args:
        response_data (str): The response data to be validated.
        file_path_response_schema (str): The file path to the JSON schema.

    Returns:
        dict: Parsed response data if valid.

    Raises:
        ValueError: If response_data is not a string.
        Exception: If any other unexpected error occurs during validation.
    """
    # Check if response_data is a string
    if not isinstance(response_data, str):
        raise ValueError("response_data must be a string")
    try:
        # Parse response_data into a dictionary
        response_json = {
            "wrapper_port": response_data[0:4],
            "source_address": response_data[4:8],
            "destination_address": response_data[8:12],
            "length": response_data[12:16],
            "response_method": response_data[16:18],
            "response_type": response_data[18:20],
            "priority": response_data[20:22],
        }

        # Validate parsed values against predefined checks
        if (
            check_address(response_json["wrapper_port"], "wrapper_port")
            and check_address(response_json["source_address"], "source_address")
            and check_address(
                response_json["destination_address"], "destination_address"
            )
            and check_value(response_json["response_method"], "response_method")
            and check_value(response_json["response_type"], "response_type")
            and check_value(response_json["priority"], "priority")
        ):
            # Load response schema from file
            response_schema = read_json_file(file_path=file_path_response_schema).get(
                "response_schema"
            )

            # Validate response_json against the loaded schema
            jsonschema.validate(instance=response_json, schema=response_schema)

        # Return the parsed response data if all checks pass
        return response_json

    except Exception as e:
        # Print error information in case of any unexpected error
        print(
            {
                "[Response data Invalid]": response_data,
                "[ERROR]": e,
                "func": "validate_response",
            }
        )


# Normal response validation


def validate_normal_response(response_data: str):
    """
    Validate a normal response data format.

    Args:
        response_data (str): The response data to be validated.
        file_path_response_schema (str): The file path to the response schema.

    Returns:
        dict: Validated response data in dictionary format.

    Raises:
        ValueError: If response_data is not a string.
        Exception: If data has improper length or if JSON schema validation fails.
        jsonschema.ValidationError: If JSON schema validation fails.
    """
    try:
        # Check if response_data is a string
        if not isinstance(response_data, str):
            raise ValueError("response_data must be a string")

        # Validate the overall response structure
        response_json = validate_response(response_data=response_data)

        # Extract data_result and data_type from response_data
        data_result = response_data[22:24]
        data_type = response_data[24:26]

        # Check for unexpected length and update response_json accordingly
        if unexpected_length(data_result=data_result, data_type=data_type) != 0:
            response_json.update({"data_result": data_result, "data_type": data_type})
            counter = (int(response_json["length"], 16) * 2) - 10

            response_json.update({"data": response_data[26:]})

            # Check if data length is proper
            if counter - len(response_json["data"]) == 0:
                response_schema_normal = read_json_file(
                    file_path=file_path_response_schema
                )["response_schema_normal"]
                jsonschema.validate(
                    instance=response_json, schema=response_schema_normal
                )
                # print_response_json(response_json=response_json)
                return response_json
            else:
                raise Exception({"ERROR": "Data has improper length"})

        else:
            response_json.update(
                {
                    "data_result": data_result,
                    "data_type": data_type,
                    "data_length": response_data[26:28],
                }
            )
            counter = (int(response_json["length"], 16) * 2) - 12
            response_json.update({"data": response_data[28:]})

            # Check if data length is proper
            if counter - len(response_json["data"]) == 0:
                response_schema_normal_unexpected_length = read_json_file(
                    file_path=file_path_response_schema
                )["response_schema_normal_unexpected_length"]
                jsonschema.validate(
                    instance=response_json,
                    schema=response_schema_normal_unexpected_length,
                )
                # print_response_json(response_json=response_json)
                return response_json
            else:
                raise Exception({"ERROR": "Data has improper length"})

    except jsonschema.ValidationError as e:
        print(
            {
                "[Response data invalid]": response_data,
                "[ERROR]": e,
                "func": "validate_normal_response",
            }
        )


# List response validation


def validate_list_response(response_data: str):
    try:
        if not isinstance(response_data, str):
            raise ValueError("response_data must be a string")

        response_json = validate_response(response_data=response_data)
        position = 22  # starting from number_of_objects
        number_of_objects = int(response_data[position : position + 2], 16)
        response_json.update(
            {"number_of_objects": response_data[position : position + 2]}
        )
        counter = (int(response_json["length"], 16) * 2) - 8
        # print(counter)
        position += 2  # 24
        for i in range(number_of_objects):
            data_result = response_data[position : position + 2]
            position += 2  # 26

            data_type = response_data[position : position + 2]
            position += 2  # 28

            length = unexpected_length(data_result=data_result, data_type=data_type)

            if length == None:
                print("data_type not found.")
                raise Exception("Data type not found.")

            elif length == 0:  # data came in array
                response_json.update(
                    {
                        "data_result_" + str(i + 1): data_result,
                        "data_type_" + str(i + 1): data_type,
                        "data_length_"
                        + str(i + 1): response_data[position : position + 2],
                    }
                )

                position += 2
                counter -= len(response_json["data_result_" + str(i + 1)])
                counter -= len(response_json["data_type_" + str(i + 1)])
                counter -= len(response_json["data_length_" + str(i + 1)])
                end_data = position + (
                    int(response_json["data_length_" + str(i + 1)], 16) * 2
                )
                response_json.update(
                    {"data_" + str(i + 1): response_data[position:end_data]}
                )
                counter -= len(response_json["data_" + str(i + 1)])
                position = end_data

            else:
                response_json.update(
                    {
                        "data_result_" + str(i + 1): data_result,
                        "data_type_" + str(i + 1): data_type,
                    }
                )
                counter -= len(response_json["data_result_" + str(i + 1)])
                counter -= len(response_json["data_type_" + str(i + 1)])
                end_data = position + int(length)
                response_json.update(
                    {"data_" + str(i + 1): response_data[position:end_data]}
                )
                counter -= len(response_json["data_" + str(i + 1)])
                position = end_data

        if counter == 0:
            # print_response_json(response_json=response_json)
            return response_json
        else:
            raise Exception("Data have improper length")
    except Exception as e:
        print(
            {
                "[Invalid list Response Data]": response_data,
                "[ERROR]": e,
                "func": "validate_list_response",
            }
        )


# block presponse validation


def validate_block_response(response_data: str, number_of_objects="", data_str=""):
    try:
        response_json = validate_response(response_data=response_data)
        position = 22  # starting from last_block_or_not

        last_block_or_not = response_data[position : position + 2]
        response_json.update({"last_block_or_not": last_block_or_not})
        position += 2  # 24

        block_number = response_data[position : position + 8]
        response_json.update({"block_number": block_number})
        position += 8  # 32

        data_till_block_number = response_json.copy()

        success_of_block = response_data[position : position + 2]
        response_json.update({"success_of_block": success_of_block})
        position += 2  # 34

        length_of_block = response_data[position : position + 2]
        response_json.update({"length_of_block": length_of_block})
        position += 2  # 36

        end_data = position + (int(length_of_block, 16) * 2)

        if int(block_number, 16) == 1:
            number_of_objects = response_data[position : position + 2]
            response_json.update({"number_of_objects": number_of_objects})
            position += 2  # 38
        data_str += response_data[position:end_data]
        response_json.update({"data": data_str})

        if last_block_result(last_block_or_not):
            position = 0
            i = 0
            # for i in range(int(number_of_objects, 16)):
            while True:
                data_result = response_json["data"][position : position + 2]
                position += 2  # 26
                data_type = response_json["data"][position : position + 2]
                position += 2  # 28
                length = unexpected_length(data_result=data_result, data_type=data_type)
                if length == None:
                    print("data_type not found.")
                    break
                elif length == 0:  # data came in array
                    response_json.update(
                        {
                            "data_result_" + str(i + 1): data_result,
                            "data_type_" + str(i + 1): data_type,
                            "data_length_"
                            + str(i + 1): response_json["data"][
                                position : position + 2
                            ],
                        }
                    )
                    position += 2
                    end_data = position + (
                        int(response_json["data_length_" + str(i + 1)], 16) * 2
                    )
                    response_json.update(
                        {"data_" + str(i + 1): response_json["data"][position:end_data]}
                    )
                    position = end_data
                    i += 1
                else:
                    response_json.update(
                        {
                            "data_result_" + str(i + 1): data_result,
                            "data_type_" + str(i + 1): data_type,
                        }
                    )
                    end_data = position + int(length)
                    response_json.update(
                        {"data_" + str(i + 1): response_json["data"][position:end_data]}
                    )
                    position = end_data
                    i += 1
            response_json.update({"number_of_objects": number_of_objects})
            # position += 2
            # print_response_json(response_json)
            return response_json
        else:
            new_response = block_acknowledge(data_till_block_number)
            if new_response is not None:
                return validate_block_response(
                    new_response, number_of_objects, data_str=data_str
                )
            raise Exception("Can't able to reach meter")

    except Exception as e:
        print(
            {
                "[some error occurred in block presponse]": e,
                "func": "validate_block_response",
            }
        )


# # creating Acknowledge for block response


def block_acknowledge(data_till_block_number: dict[str, str]) -> str:
    """
    Acknowledge the receipt of data up to a specific block number.

    Args:
        data_till_block_number (dict): A dictionary containing information about the received data.
            It should include the keys:
            - "wrapper_port": The wrapper port.
            - "source_address": The source address.
            - "destination_address": The destination address.
            - "response_type": The response type.
            - "priority": The priority of the request.
            - "block_number": The block number of the received data.

    Returns:
        str: The acknowledgment response after sending it to the meter and receiving the validation response.

    Example:
        >>> data = {
        ...     "wrapper_port": "1234",
        ...     "source_address": "MeterA",
        ...     "destination_address": "Server",
        ...     "response_type": "TypeA",
        ...     "priority": "High",
        ...     "block_number": "123"
        ... }
        >>> ack_response = block_acknowledge(data)
    """
    if not isinstance(data_till_block_number, dict):
        raise TypeError("data_till_block_number must be a dict")
    # Initialize an empty string to concatenate values for acknowledgment
    ack_str = ""

    # Create an acknowledgment dictionary
    ack = {
        "wrapper_port": data_till_block_number["wrapper_port"],
        "source_address": data_till_block_number["destination_address"],
        "destination_address": data_till_block_number["source_address"],
        "length": "0007",
        "request_method": "C0",  # about to work on it
        "request_type": data_till_block_number["response_type"],
        "priority": data_till_block_number["priority"],
        "block_number": data_till_block_number["block_number"],
    }

    # Concatenate values to form a string for acknowledgment
    for key, val in ack.items():
        ack_str += val

    # Convert the acknowledgment string to bytes using UTF-8 encoding
    ack_str = ack_str.encode("utf-8")

    # Print the acknowledgment for debugging purposes
    print("[Acknowledge]", ack_str)

    # Send the acknowledgment and receive the validation response
    next_block = connect_socket(ack_str, 3)
    
    if next_block is not None:
        return next_block.replace("b", "").replace("'", "")
    raise Exception("Can't able to send acknowledgment")


# Get response type


def get_response_type(response_data: str) -> str:
    """
    Extracts the response type from the given response data.

    Args:
        response_data (str): The response data from which to extract the response type.

    Returns:
        str: The extracted response type.

    Raises:
        ValueError: If response_data is not a string.
    """
    try:
        # Check if response_data is a string
        if not isinstance(response_data, str):
            # Raise a ValueError if response_data is not a string
            raise ValueError("response_data must be a string")
        else:
            # Extract the response type from a specific substring
            return response_data[18:20]

    except Exception as e:
        # Log an error message if an exception occurs
        print(
            {
                f"[Response does not contain response_type {response_data[18:20]}]": response_data,
                "[ERROR]": e,
                "func": "get_response_type",
            }
        )


# Validator for response


def call_validator(response_data: str) -> dict[str:str]:
    """
    Validates the given response data based on its response type.

    Args:
        response_data (str): The response data to be validated.

    Returns:
        dict: A dictionary containing the validation result or error information.

    Raises:
        Exception: If the response type is not supported.

    Example:
        response_data = '{"type": "01", "data": {"key": "value"}}'
        result = call_validator(response_data)
        print(result)
    """
    if not isinstance(response_data, str):
        raise ValueError("Response type must be a string")
    try:
        response_type = get_response_type(response_data=response_data)

        if response_type == "01":
            return validate_normal_response(response_data=response_data)
        elif response_type == "02":
            return validate_block_response(response_data=response_data)
        elif response_type == "03":
            return validate_list_response(response_data=response_data)
        else:
            raise Exception("Response type not supported")
    except Exception as e:
        print({"response": response_data, "ERROR": e, "func": "call_validator"})
        return None


# Data without header (only data values)


def data_without_header():
    s = call_validator(response_data=response_data)

    keys_to_keep = list(("data_" + str(x)) for x in range(1, 20))

    return {key: s[key] for key in keys_to_keep if key in s.keys()}


# From here our application  will start

if __name__ == "__main__":
    # print(data_without_header())
    try:
        resp_json = call_validator(response_data=response_data)
        print(resp_json)

        if resp_json.get("request_type") == "03":
            i = 1
            value = list()
            for num in range(int(resp_json.get("number_of_objects"), 16)):
                val = converter(
                    resp_json.get("data_type_" + str(i)), resp_json.get("data_" + str(i))
                )
                value.append(val)
                i += 1
            print(value)
        elif resp_json.get("request_type") == "01":
            print(resp_json.get("data"))
    except Exception as e:
        print(f"[ERROR] {e}")
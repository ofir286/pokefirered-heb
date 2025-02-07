import json

def reorder_json_by_reference(reference_json, target_json):
    """
    Reorders a target JSON array based on the itemId order in a reference JSON array.
    Handles Unicode text in JSON values.
    
    Args:
        reference_json (list): The reference JSON array that defines the desired order
        target_json (list): The JSON array to be reordered
        
    Returns:
        list: A new JSON array with items reordered according to the reference
    """
    
    # Create a dictionary from target_json for O(1) lookup
    target_dict = {item['itemId']: item for item in target_json}
    
    # Create the reordered list based on reference order
    reordered_json = []
    
    for ref_item in reference_json:
        item_id = ref_item['itemId']
        if item_id in target_dict:
            reordered_json.append(target_dict[item_id])
    
    # Add any remaining items that weren't in the reference JSON
    remaining_ids = set(target_dict.keys()) - {item['itemId'] for item in reference_json}
    for item_id in remaining_ids:
        reordered_json.append(target_dict[item_id])
    
    return reordered_json

def main():
    # Read the input files with UTF-8 encoding
    try:
        with open('9.txt', 'r', encoding='utf-8') as f:
            reference_json = json.load(f)
            
        with open('9_translated.txt', 'r', encoding='utf-8') as f:
            target_json = json.load(f)
            
        # Reorder the target JSON
        reordered_json = reorder_json_by_reference(reference_json, target_json)
        
        # Write the result to a new file with UTF-8 encoding
        with open('reordered.json', 'w', encoding='utf-8') as f:
            json.dump(reordered_json, f, indent=2, ensure_ascii=False)
            
        print("Successfully reordered the JSON and saved to 'reordered.json'")
        
    except FileNotFoundError as e:
        print(f"Error: Could not find input file - {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
    except KeyError as e:
        print(f"Error: Missing required 'itemId' field - {e}")
    except UnicodeError as e:
        print(f"Error: Unicode encoding/decoding error - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
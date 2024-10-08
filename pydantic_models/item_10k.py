from pydantic import BaseModel, Field
from typing import List
import json  # Importing the json module for formatting output

class Item10K(BaseModel):
    """
    Model representing a 10-K item.

    Attributes:
        item_id (str): The unique identifier for the item.
        name (str): The name of the item.
        page_start (int): The starting page number of the item (must be positive).
        page_end (int): The ending page number of the item (must be positive).
    """
    item_id: str = Field(..., description="The unique identifier for the item.")
    name: str = Field(..., description="The name of the item.")
    page_start: int = Field(
        ..., gt=0, description="The starting page number (must be positive)."
    )
    page_end: int = Field(
        ..., gt=0, description="The ending page number (must be positive)."
    )

class Item10KList(BaseModel):
    """
    Model representing a list of 10-K items.

    Attributes:
        items (List[Item10K]): A list of 10-K items.
    """
    items: List[Item10K] = Field(..., description="A list of 10-K items.")

if __name__ == "__main__":
    # Example usage with sample data
    data = {
        "items": [
            {
                "item_id": "1",
                "name": "Business",
                "page_start": 1,
                "page_end": 5
            },
            {
                "item_id": "2",
                "name": "Risk Factors",
                "page_start": 6,
                "page_end": 10
            }
        ]
    }

    # Validate the data
    item_list = Item10KList(**data)

    # Convert to JSON string with formatting
    formatted_json = item_list.json()  # Get the JSON string representation
    parsed_json = json.loads(formatted_json)  # Parse JSON string to dict
    print(json.dumps(parsed_json, indent=2))  # Pretty-print the JSON

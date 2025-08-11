# *********************************************************************
# PLACEHOLDER
# *********************************************************************
init python:
    import json
    import urllib.parse

    # Our shared game schema for the CDD. Should probably have this on the CDD frontend, not in Renpy.
    game_schema = {
        "$schema": "./schema/Causal-Decision-Model.json",
        "meta": {
            "uuid": "98f56597-75d8-441a-bd19-239db7d1b4f4",
            "name": "Dynamic Decision Model",
            "summary": "This model dynamically adapts based on player choices.",
            "documentation": {
                "content": "This CDD was dynamically generated in Ren'Py.",
                "MIMEType": "text/plain"
            },
            "version": "0.1",
            "draft": True,
            "updatedDate": "2025-02-28T15:00:00"
        },
        "diagrams": [
            {
                "meta": {
                    "uuid": "diagram-1",
                    "name": "Dynamic Decision Diagram"
                },
                "elements": [],
                "dependencies": []
            }
        ]
    }

    # Example function: Add a new element to our CDD
    def add_element(name, causal_type, x, y):
        new_element = {
            "meta": {
                "uuid": f"elem-{len(game_schema['diagrams'][0]['elements']) + 1}",
                "name": name
            },
            "causalType": causal_type,  # e.g., "Lever", "Intermediate", or "Outcome"
            "diaType": "box",
            "content": {
                "position": {"x": x, "y": y},
                "boundingBoxSize": {"width": 400, "height": 500}
            }
        }
        game_schema["diagrams"][0]["elements"].append(new_element)
        return new_element["meta"]["uuid"]

    # Example function: Add a dependency (edge) between two elements
    def add_dependency(source_uuid, target_uuid):
        new_dependency = {
            "meta": {
                "uuid": f"dep-{len(game_schema['diagrams'][0]['dependencies']) + 1}",
                "name": f"{source_uuid} → {target_uuid}"
            },
            "source": source_uuid,
            "target": target_uuid
        }
        game_schema["diagrams"][0]["dependencies"].append(new_dependency)

    # Create a nicely formatted JSON string
    def get_json_schema():
        return json.dumps(game_schema, indent=2)

    def open_website_with_json():
        data_str = get_json_schema()
        encoded_data = urllib.parse.quote(data_str)
        url = f"https://example.com?data={encoded_data}"
        renpy.open_url(url)

    def open_index_html_with_big_json(schema, site_url="https://example.com/index.html"):
        json_str = json.dumps(schema)
        encoded = urllib.parse.quote(json_str)
        url = f"{site_url}#{encoded}"
        renpy.open_url(url)
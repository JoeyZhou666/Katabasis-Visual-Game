label cdd_tool_scene:
    $ big_json = json.dumps({"msg": "Hello from Ren'Py!", "hugeData": "..."})

    "Do you want to visit our website?"

    menu:
        "Yes":
            $ open_index_html_with_big_json(game_schema)
            "Opening website..."
        "No":
            "Okay, maybe later."

    return

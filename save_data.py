import json

# The TRAINING_DATA list from Step 2
TRAINING_DATA = [
    {
        "text": "Learn Python at EasyLearn Academy.",
        "entities": [
            [6, 12, "COURSE"]
        ]
    },

    # ... your other examples
]

# Save to file
with open("training_data.json", "w") as f:
    json.dump(TRAINING_DATA, f, indent=2)

print("Saved training_data.json successfully!")
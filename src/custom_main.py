import argparse # type: ignore
import json
from tqdm import tqdm
from openai_handler import generate_use_all_icl

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--test_file", type=str, default="custom_prompts.json")
    parser.add_argument("--save_file", type=str, default="generated_diagram_plans.json")

    args = parser.parse_args()

    save_file = f"{args.save_file}"

    out = { }
    
    with open(f"{args.test_file}", "r") as f:
        data = json.load(f)
    
    test_data = []

    for x in data:
        test_data.append({
            "image": x["image"],
            "caption": x["caption"],
            "topic": x["topic"]
        })

    with open(f"{args.test_file}", "r") as f:
        test_images = json.load(f)

    for sample in tqdm(test_data, desc="Generating Diagram Plans"):
        diagram, corrections, attempts = generate_use_all_icl(sample["caption"], sample["topic"])

        out[sample["image"]] = {
            "image": sample["image"],
            "caption": sample["caption"],
            "diagram": diagram,
            "corrections": corrections,
            "attempts": attempts,
        }

        with open(save_file, "w") as f:
            json.dump(out, f, indent=2)

    with open(save_file, "w") as f:
            json.dump(out, f, indent=2)
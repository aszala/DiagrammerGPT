import openai
from in_ctx_prompts import prompts
import copy

from dotenv import dotenv_values
config = dotenv_values(".env")

openai.api_key = config['API_KEY']
openai.api_base = config['API_BASE']
openai.api_type = config['API_TYPE']
openai.api_version = config['API_VERSION']

def call_api(log, engine="gpt-4", use_azure=True):
    if use_azure:
        resp = openai.ChatCompletion.create(
            engine=engine,
            messages=log,
            temperature=0
        )
    else:
        resp = openai.ChatCompletion.create(
            model=engine,
            messages=log,
            temperature=0
        )

    resp = resp['choices'][0]['message']['content']

    return resp

def generate_use_all_icl(caption, topic):
    diagram_prompt_keys = [x for x in prompts.keys() if x.startswith("diagram_")]
    auditor_prompt_keys = [x for x in prompts.keys() if x.startswith("auditor_")]

    prompt_preamble = prompts[diagram_prompt_keys[0]].split("Here are some examples:")[0] + "Here are some examples:"
    prompt_examples = ""

    for key in diagram_prompt_keys:
        topic_icl = prompts[key].split("Here are some examples:")[1].split("\n")
        topic_icl = '\n'.join(topic_icl[:-2])

        prompt_examples += f"{topic_icl}\n"

    diagram_prompt = f"{prompt_preamble}{prompt_examples}\nCaption:\n{caption.lower()}\nTopic:\n{topic}\n"


    auditor_preamble = prompts[auditor_prompt_keys[0]].split("Here are some examples:")[0] + "Here are some examples:\n"
    auditor_examples = ""

    for key in auditor_prompt_keys:
        topic_icl = prompts[key].split("Here are some examples:")[1].split("\n")
        topic_icl = '\n'.join(topic_icl[:-2])

        auditor_examples += f"{topic_icl}\n"

    auditor_prompt = f"{auditor_preamble}{auditor_examples}\nCaption:\n{caption.lower()}\nTopic:\n{topic}"

    diagram_chatlog = [
        {"role": "user", "content": diagram_prompt},
    ]

    parsed_resp = None
    corrections = []
    diagram_attempts = []

    for i in range(5):
        diagram = call_api(diagram_chatlog, engine="gpt-4-32k")
        
        parsed_resp = parse_diagram(diagram, caption, topic, load=parsed_resp)
        diagram_attempts.append(copy.deepcopy(parsed_resp))
        
        if i == 4:
            continue

        correction_chatlog = [
            {"role": "user", "content": f"{auditor_prompt}\n{diagram}\nWhat is wrong with this diagram?\n"},
        ]

        correction = call_api(correction_chatlog, engine="gpt-4-32k")
        corrections.append(correction)

        words = correction.lower().replace(".", "").split(" ")

        if "impossible" in words or "nothing" in words or ("correct" in words and not "not correct" in correction.lower()):
            break
        
        correction = parse_correction(correction)

        diagram_chatlog.append({"role": "assistant", "content": diagram})
        diagram_chatlog.append({"role": "user", "content": correction})

        tokens = 0
        for x in diagram_chatlog:
            tokens += len(x["content"].split(" ")) * 1.333

        if tokens > 32000:
            break

    return parsed_resp, corrections, diagram_attempts

def parse_correction(correction):
    return f"{correction} Can you please fix it?"

def parse_diagram(diagram, caption, topic, load=None):
    lines = diagram.split('\n')
    lines = [x.strip() for x in lines]

    layout = ""
    entity_bounds = { }
    entity_relatonships = [ ]

    if load is not None:
        layout = load["layout"]
        entity_bounds = load["entity_bounds"]
        entity_relatonships = load["entity_relationships"]

    entity_index = -100000
    relationship_index = -100000
    location_index = -100000

    save_values = []
    
    for i, line in enumerate(lines):
        if line.startswith("Diagram Layout:"):
            layout = lines[i+1]
        if line.startswith("Required Entities:"):
            entity_index = i
        if line.startswith("Entity Relationships:"):
            relationship_index = i
            save_values.append("entity_bounds")
        if line.startswith("Entity Locations"):
            location_index = i
            save_values.append("entity_relationships")

    if entity_index > -1:
        x = relationship_index

        if x < 0:
            x = location_index

            if x < 0:
                x = len(lines)

        for line in lines[entity_index+1:x]:
            if len(line.strip()) == 0:
                continue

            if "image" in line:
                words = line.split(" image ")

                id = line.split("(")[1]
                value = words[0]
                type = "image"
                
            elif "text" in line:
                words = line.split(" text label ")

                id = line.split("(")[1]
                value = words[0].replace("\"", "")
                type = "text"

            id = id.replace("(", "").replace(")", "")
            entity_bounds[id] = {
                "id": id,
                "type": type,
                "value": value,
                "bounds": []
            }
    
    if relationship_index > -1:
        x = location_index

        if x < 0:
            x = len(lines)

        for line in lines[relationship_index+1:x]:
            ids = line.split(" ")

            passed = len(line.strip()) > 0
            count = 0
            for i, word in enumerate(ids):
                if word.startswith("T") or word.startswith("I"):
                    if not (word in entity_bounds):
                        passed = False
                        break
                    count += 1

            if count < 2:
                passed = False

            if not passed:
                print("Failed to parse relationship: ", line)
                continue
            entity_relatonships.append(line)

    if location_index > -1:
        for line in lines[location_index+1:]:
            words = line.split(" is located at ")

            try:
                id = words[0]
                words[1] = words[1][:words[1].index("]")]
                value = words[1].replace("[", "").replace("]", "").replace(", ", ",")
            except:
                print("Failed to parse location: ", line)
                continue

            if not (id in entity_bounds):
                print("Failed to parse location: ", line)
                continue

            bounds = value.split(",")
            bounds = [int(x.strip()) for x in bounds]

            entity_bounds[id]["bounds"] = bounds

        bad_ids = []
        for id in entity_bounds:
            if len(entity_bounds[id]["bounds"]) == 0:
                bad_ids.append(id)

        for id in bad_ids:
            del entity_bounds[id]

    r = {
        "caption": caption,
        "topic": topic,
        "layout": layout,
        "entity_bounds": entity_bounds,
        "entity_relationships": list(set(entity_relatonships))
    }

    return r 
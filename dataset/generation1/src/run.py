import json
import os

output_dir = "_out"

def main():
    # generate models according to content of models.json
    
    models_file_data = open("config/models.json", "r")
    models_config = json.load(models_file_data)

    color_file_data = open("config/colors.json", "r")
    color_config = json.load(color_file_data)

    template = "1 {color} 0 -24 0 1 0 0 0 1 0 0 0 1 {model}\n"
    ldr_filename_template = "{model}_{color}.ldr"

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for model in models_config["models"]:
        ld_file = model["ldfile"]
        print("generation model for {0}".format(ld_file))

        model_dir = os.path.join(output_dir, model["name"])
        if not os.path.exists(model_dir):
            os.mkdir(model_dir)
        for color_name, color_code in color_config["colors"].items():
            ldr_file_content = template.format(model=ld_file, color=color_code)

            ldr_file_name = os.path.join(model_dir, ldr_filename_template.format(model=model["name"], color=color_name))
            with open(ldr_file_name, "w") as ldr_file:
                ldr_file.write(ldr_file_content)

    return 0


if __name__ == "__main__":
    main()

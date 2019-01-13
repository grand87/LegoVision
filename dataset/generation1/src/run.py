import itertools
import json
import os
import subprocess

output_dir = "_out"
ldr_filename_template = "model.ldr"
pov_filename_template = "{zoom}-{lat}-{lon}.pov"
ldview_cmdline_template = "LDView -WindowWidth=640 -WindowHeight=480 {model} -ExportFile={pov_file} -DefaultZoom={zoom} -cg{lat},{lon}"
povray_cmdline_template = "pvengine64 /RENDER {inifile} Output_File_Name={outfolder} /EXIT"

def update_pov_file(pov_file_name, model_name):
    pov_file_lines = open(pov_file_name).readlines()

    # need to update pov file - insert floor information & light
    for i, line in enumerate(pov_file_lines):
        if line.find("// model.ldr") != -1:
            pov_file_lines.insert(i, "#include \"floor.inc\"\n")
            pov_file_lines.insert(i, "#include \"lights.inc\"\n")
            break

    for i, line in enumerate(pov_file_lines):
        if line.find("lg_3010\n") != -1:
            pov_file_lines.insert(i + 2, "\t\trotate <0, 360 * clock, 0>\n")
            break

    with open(pov_file_name+".mod.pov", "w") as target:
        target.writelines(pov_file_lines)


def main():
    # generate models according to content of models.json
    
    models_file_data = open("config/models.json", "r")
    models_config = json.load(models_file_data)

    color_file_data = open("config/colors5.json", "r")
    color_config = json.load(color_file_data)

    template = "1 {color} 0 -24 0 1 0 0 0 1 0 0 0 1 {model}\n"
    ldr_dirname_template = "{model}-{color}"

    model_ini_file_content = open("config/model.ini", "r").read()

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    b = False

    workdir = os.getcwd()

    for r in itertools.product(models_config["models"], color_config["colors"], models_config["zoom"], models_config["campos"]):
        os.chdir(workdir)

        if not b:
            b = True
#        else:
#            continue

        ld_file = r[0]["ldfile"]
        color_name = r[1]
        color_code = color_config["colors"][r[1]]
        ldr_file_content = template.format(model=ld_file, color=color_code)

        model_dir = os.path.join(output_dir, ldr_dirname_template.format(model=r[0]["name"], color=color_name))
        if not os.path.exists(model_dir):
            os.mkdir(model_dir)

        ldr_file_name = ldr_filename_template
        ldr_file_name = os.path.join(model_dir, ldr_file_name)

        with open(ldr_file_name, "w") as ldr_file:
            ldr_file.write(ldr_file_content)

        # generation POV file for model
        pov_filename = pov_filename_template.format(zoom=r[2], lat=r[3]["lat"], lon=r[3]["lon"])
        pov_filename_full = os.path.join(model_dir, pov_filename)
        pov_export_cmdline = ldview_cmdline_template.format(model=ldr_file_name, pov_file=pov_filename_full, zoom=r[2], lat=r[3]["lat"], lon=r[3]["lon"])
        print("cmdline = {0}".format(pov_export_cmdline))

        result = subprocess.call(pov_export_cmdline)

        update_pov_file(pov_filename_full, ld_file.split(".")[0])

        os.chdir(model_dir)
        # store ini file for animation
        ini_filename = pov_filename+".ini"
        with open(ini_filename, "w") as model_ini_file_content_new:
            model_ini_file_content_new.write(model_ini_file_content.format(pov_filename+".mod.pov"))

        # generate rendering frames
        povray_cmdline = povray_cmdline_template.format(inifile=ini_filename, outfolder=".")
        result = subprocess.call(povray_cmdline)

    return 0


if __name__ == "__main__":
    main()
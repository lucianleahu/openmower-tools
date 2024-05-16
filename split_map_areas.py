import json
import sys

if __name__ == '__main__':
    # print("This is the name of the script= ", sys.argv[0])
    # print("Number of arguments= ", len(sys.argv))
    # print("all args= ", str(sys.argv))
    if len(sys.argv) < 2:
        input_map_file = "maps/area0_1_2_3_4_5_6_edit8.json"
    else:
        input_map_file = sys.argv[1]
    print("Input map file: ", input_map_file)
    f = open(input_map_file, "r")
    data = json.loads(f.read())
    f.close()

    navigationAreas = list(data['NavigationAreas'])
    workingAreas = data['WorkingArea'][:]
    for i in range(len(workingAreas)):
        dict_current_area = {}
        for k in data:
            if 'WorkingArea' not in k and 'NavigationAreas' not in k:
                dict_current_area[k] = data[k]
        dict_current_area['WorkingArea'] = [workingAreas[i]]
        dict_all_other_navigation_areas = list(navigationAreas)
        # make all other working areas navigation areas
        for j in range(len(workingAreas)):
            if i != j:
                dict_all_other_navigation_areas.append(workingAreas[j])
        dict_current_area['NavigationAreas'] = dict_all_other_navigation_areas
        file_for_current_area = "split_area{}_from_{}".format(i, input_map_file.split("/")[-1])
        folder_for_output = ""
        for s in input_map_file.split("/")[:-1]:
            folder_for_output = folder_for_output + s + "/"
        full_path_file = folder_for_output + file_for_current_area
        print("Creating map for area {}\n Output file: {}\n".format(i, full_path_file))
        with open(full_path_file, "w") as f:
            json.dump(dict_current_area, f)
import re
mooncake_path = "C:/Users/Administrator/Documents/GitHub/azure-content-mooncake-pr"

include_reg = r"(?P<includeText>\s*\[AZURE\.INCLUDE\s\[[^\[|^\]]*\]\(\.\./includes/(?P<fileName>[\w|\-]+\.md)\)\])\s*"

def replaceInclude(fileRelativePath, filename):
    input = open(mooncake_path + "/" + fileRelativePath+"/"+filename, "r")
    text = input.read()
    input.close()
    includeList = list(set(re.findall(include_reg, text)))
    for include in includeList:
        includeText = include[0]
        includeFile = include[1]
        try:
            input = open(mooncake_path + "/includes/" + includeFile, "r")
            replacement = input.read().replace("./media", "../../includes/media")
            input.close()
        except IOError:
            replacement = ""
        text = text.replace(includeText, replacement)
    output = open(filename, "w")
    output.writelines(text)
    output.close()
def sliceAfterSubstr(str, substr):
    return str.split(substr, 1)[1]

def sliceBetweenSubstr(str, substr_0, substr_1):
	return str[str.index(substr_0) + len(substr_0): str.index(substr_1)]

def sliceUpToSubstr(str, substr):
    return str.split(substr, 1)[0]

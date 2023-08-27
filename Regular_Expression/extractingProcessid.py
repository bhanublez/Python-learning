import re
def extract_pid(log_line):
    regex=r"\[(\d+)]"
    result=re.search(regex,log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid("Something want wrong in process fork whose id is [29247]"))
print(extract_pid("Something want wrong in process fork whose id is [afbjb]"))# return empty string
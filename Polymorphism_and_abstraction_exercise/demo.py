import re

test = "1###5275215###District+ 3 XL Dnister Black"

pattern = r"###"

test = re.sub(pattern, " ", test, 1)
test = re.sub(pattern, "repeatable", test, 1)
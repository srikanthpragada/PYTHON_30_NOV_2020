# Display char frequency

st = "how do you do"

for ch in set(st):
    print(f"{ch} occurs {st.count(ch)} times")
